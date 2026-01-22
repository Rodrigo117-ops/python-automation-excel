# Automação de Relatórios com Python (Excel)

Projeto em Python que automatiza a limpeza, validação e consolidação de dados
a partir de uma planilha Excel, gerando um relatório final com múltiplas abas.

## ✅ Funcionalidades
- Leitura de arquivos Excel (.xlsx)
- Limpeza e validação de dados
- Normalização de datas e valores
- Cálculo automático de totais
- Geração de relatório Excel com múltiplas abas:
  - dados_limpos
  - resumo_por_categoria
  - resumo_por_dia
  - top_produtos

## 🛠️ Tecnologias
- Python
- pandas
- openpyxl

## 🚀 Como executar

### 1️⃣ Criar ambiente virtual (recomendado)
```bash
python -m venv .venv
.venv\Scripts\activate

### 2️⃣ Instalar dependências
```bash
pip install -r requirements.txt

### 3️⃣ Gerar planilha de exemplo
```bash
python src/main.py --make-sample

### 4️⃣ Gerar relatório
```bash
python src/main.py

O relatório será gerado em:
data/output_report.xlsx

📄 Formato esperado do Excel

data, categoria, produto, quantidade, valor

📌 Observação

Os arquivos Excel são gerados automaticamente e não são versionados no GitHub.

