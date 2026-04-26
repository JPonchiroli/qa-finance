from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Carregar modelo e scaler
model = joblib.load("modelo_anomalia.pkl")
scaler = joblib.load("scaler.pkl")


def preprocess(df):
    # normalizar nomes das colunas
    df.columns = df.columns.str.strip()

    # tentar mapear nomes alternativos (caso venha diferente)
    col_map = {
        "timestamp": "timeStamp",
        "elapsed": "elapsed",
        "latency": "elapsed",
        "success": "success",
        "sucesso": "success"
    }

    df.rename(columns=col_map, inplace=True)

    # validar colunas essenciais
    required = ["timeStamp", "elapsed", "success"]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Coluna ausente: {col}")

    # =========================
    # Conversões robustas
    # =========================

    # timestamp (aceita vários formatos)
    df["timeStamp"] = pd.to_datetime(df["timeStamp"], errors="coerce")

    # elapsed
    df["elapsed"] = pd.to_numeric(df["elapsed"], errors="coerce")

    # success (bem flexível)
    df["success"] = (
        df["success"]
        .astype(str)
        .str.lower()
        .str.strip()
        .map({
            "true": 1, "false": 0,
            "1": 1, "0": 0,
            "yes": 1, "no": 0,
            "sucesso": 1, "falha": 0
        })
    )

    # =========================
    # DEBUG
    # =========================
    print("Antes do dropna:", len(df))

    # remover apenas linhas inválidas
    df = df.dropna(subset=["timeStamp", "elapsed", "success"])

    print("Depois do dropna:", len(df))

    # fallback inteligente
    if df.empty:
        raise ValueError(
            "CSV inválido ou formato inesperado. "
            "Verifique delimitador, colunas e valores."
        )

    # =========================
    # Features
    # =========================
    df["hour"] = df["timeStamp"].dt.hour
    df["minute"] = df["timeStamp"].dt.minute

    return df


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]

        df = pd.read_csv(file, sep=None, engine="python")
        df = preprocess(df)

        X = df[["elapsed", "success", "hour", "minute"]]
        X_scaled = scaler.transform(X)

        preds = model.predict(X_scaled)

        # IsolationForest: -1 = anomalia, 1 = normal
        df["anomaly"] = preds

        total = len(df)
        anomalies = (df["anomaly"] == -1).sum()
        perc_anomaly = (anomalies / total) * 100

        alerta = perc_anomaly > 5

        return render_template(
            "index.html",
            total=total,
            anomalies=anomalies,
            perc=round(perc_anomaly, 2),
            alerta=alerta,
            latencias=df["elapsed"].tolist()
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)