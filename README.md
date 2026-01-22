# Automação de Relatórios com Python (Excel → Limpeza → Relatório)

Este projeto automatiza o processamento de uma planilha Excel:
- valida e limpa dados
- calcula totais
- gera um relatório em Excel com múltiplas abas (resumos e top produtos)

## ✅ Funcionalidades
- Leitura de `.xlsx`
- Limpeza/validação:
  - remove nulos essenciais
  - corrige tipos (data/números)
  - remove valores inválidos (<= 0)
  - cria coluna `total = quantidade * valor`
- Relatório em Excel com abas:
  - `dados_limpos`
  - `resumo_por_categoria`
  - `resumo_por_dia`
  - `top_produtos`

## 🛠️ Tecnologias
- Python
- pandas
- openpyxl

## 🚀 Como executar

### 1) Instalar dependências
```bash
pip install -r requirements.txt
