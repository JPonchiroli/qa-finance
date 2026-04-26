# 📊 Dashboard de Detecção de Anomalias com JMeter + Machine Learning

## 🧠 Sobre o projeto

Esta aplicação web tem como objetivo **analisar resultados de testes de carga do JMeter** e identificar automaticamente comportamentos anômalos utilizando técnicas de **Machine Learning**.

O sistema utiliza um modelo treinado com dados de execução "normal" para aprender o padrão esperado da aplicação. A partir disso, ele consegue classificar novas execuções como:

* ✅ **Normal**
* 🚨 **Anômala**

Além disso, a aplicação fornece um **dashboard visual** com métricas e gráfico de latência para facilitar a análise.

---

## ⚙️ Tecnologias utilizadas

* Python
* Flask (backend web)
* Pandas (manipulação de dados)
* Scikit-learn (modelo de ML - Isolation Forest)
* Chart.js (visualização de dados)

---

## 🚀 Funcionalidades

* Upload de arquivos CSV gerados pelo JMeter
* Pré-processamento automático dos dados
* Classificação de cada requisição como normal ou anômala
* Cálculo da taxa de anomalias
* Exibição de alerta visual caso a taxa ultrapasse 5%
* Gráfico de latência ao longo do tempo

---

## 📦 Pré-requisitos

* Python 3.8+
* pip

---

## 🛠️ Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

---

### 2. Crie e ative uma virtualenv

```bash
python -m venv venv
```

#### Windows:

```bash
venv\Scripts\activate
```

#### Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install flask pandas scikit-learn joblib
```

---

## ▶️ Como executar

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## 📁 Arquivos necessários

Para o funcionamento correto da aplicação, é necessário que os seguintes arquivos estejam presentes na raiz do projeto:

### 🧠 `modelo_anomalia.pkl`

* Modelo de Machine Learning treinado
* Responsável por classificar os dados como normais ou anômalos

### ⚖️ `scaler.pkl`

* Objeto de normalização dos dados
* Garante que os dados de entrada tenham o mesmo padrão usado no treinamento

> ⚠️ Ambos os arquivos devem ser gerados previamente no processo de treinamento e colocados na raiz do projeto.

---

## 📊 Como usar

1. Execute a aplicação
2. Faça upload de um arquivo CSV gerado pelo JMeter
3. Visualize:

   * Total de requisições
   * Quantidade e % de anomalias
   * Status do sistema (estável ou alerta)
   * Gráfico de latência

---

## 🚨 Critério de alerta

* Se a taxa de anomalias for **maior que 5%**, o sistema exibe:

  **🚨 ALERTA: Alta taxa de anomalias detectada**

* Caso contrário:

  **✅ Sistema estável**

---

## 💡 Observações

* O modelo deve ser treinado com dados representando um cenário **normal da aplicação**
* Diferenças no formato do CSV podem impactar o preprocessamento
* A aplicação tenta lidar com diferentes formatos de CSV automaticamente

---

## 📌 Melhorias futuras

* Destacar pontos anômalos no gráfico
* Comparação com baseline histórico
* Deploy em nuvem
* Integração com alertas (Slack, e-mail, etc.)

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo e prática em:

* Testes de carga
* Machine Learning aplicado a QA
* Observabilidade de sistemas

---
