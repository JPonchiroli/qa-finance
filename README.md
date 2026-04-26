# 🧪 Sistema de Qualidade QA_AIOps

## 📌 Visão Geral

Este projeto implementa um pipeline completo de qualidade de software, combinando:

* Testes funcionais
* Testes de carga
* Análise preditiva com Machine Learning
* Monitoramento via dashboard

O objetivo é simular um ambiente de QA moderno, onde não apenas validamos funcionalidades, mas também **monitoramos e prevemos problemas de performance**.

---

# 🧩 Estrutura por Fases

## 🔹 Fase 1 — Teste Funcional

### 🎯 Objetivo

Automatizar o fluxo de cadastro de despesas em uma aplicação web.

### 🛠 Tecnologias

* Selenium WebDriver
* Java + JUnit

### 📦 Entregável

* Script automatizado validando:

  * preenchimento de formulário
  * envio de dados
  * validação de sucesso

---

## 🔹 Fase 2 — Teste de Carga

### 🎯 Objetivo

Simular múltiplos usuários executando o fluxo automatizado.

### 🛠 Tecnologias

* Apache JMeter
* WebDriver Sampler

### ⚙️ Configuração

* Thread Group (ex: 50 usuários)
* Ramp-up configurado
* Execução do script Selenium em escala

### 📦 Entregáveis

* Arquivo `.jmx` (plano de teste)
* Arquivo `.csv` com resultados (ex: `resultados_carga_normal.csv`)

---

## 🔹 Fase 3 — Linha de Base (Machine Learning)

### 🎯 Objetivo

Treinar um modelo capaz de identificar comportamento normal da aplicação.

### 🛠 Tecnologias

* Python
* Pandas
* Scikit-learn

### ⚙️ Processo

* Leitura do CSV gerado pelo JMeter
* Pré-processamento dos dados
* Seleção de features:

  * latência (`elapsed`)
  * sucesso (`success`)
  * timestamp (`timeStamp`)
* Treinamento de modelo de detecção de anomalias

### 🤖 Modelo utilizado

* Isolation Forest

### 📦 Entregáveis

* Script de treinamento
* Arquivo do modelo treinado:

  * `modelo_anomalia.pkl`
* Arquivo de normalização:

  * `scaler.pkl`

---

## 🔹 Fase 4 — Simulação de Anomalias

### 🎯 Objetivo

Gerar dados que representem comportamento anormal da aplicação.

### 🛠 Estratégia

* Execução de teste de carga mais agressivo
* Ou manipulação dos dados de latência

### 📦 Entregável

* Arquivo `.csv` com comportamento anômalo:

  * `resultados_carga_anomala.csv`

---

## 🔹 Fase 5 — Dashboard de Monitoramento

### 🎯 Objetivo

Criar uma aplicação que utilize o modelo treinado para detectar anomalias em novos dados.

### 🛠 Tecnologias

* Python
* Flask
* Chart.js

### ⚙️ Funcionalidades

* Upload de CSV do JMeter
* Processamento automático dos dados
* Classificação de cada requisição:

  * Normal
  * Anomalia
* Cálculo da taxa de anomalias
* Exibição de alerta visual (> 5%)
* Gráfico de latência

### 📦 Entregável

* Aplicação web funcional

---

# 📊 Como usar

1. Execute a aplicação
2. Faça upload de um arquivo CSV do JMeter
3. Analise:

   * Total de requisições
   * Taxa de anomalias
   * Status do sistema
   * Gráfico de latência

---

# 📁 Arquivos importantes

| Arquivo             | Descrição                           |
| ------------------- | ----------------------------------- |
| modelo_anomalia.pkl | Modelo de Machine Learning treinado |
| scaler.pkl          | Normalizador de dados               |
| app.py              | Backend da aplicação                |
| preprocess.py       | Pipeline de tratamento de dados     |

---

# 🎯 Objetivo final

Demonstrar um pipeline completo de QA moderno, integrando:

✔ Automação de testes
✔ Testes de carga
✔ Machine Learning
✔ Observabilidade

---

## 👨‍💻 Projeto acadêmico

Desenvolvido como parte de estudo em QA, performance e AIOps.
