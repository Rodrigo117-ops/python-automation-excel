from __future__ import annotations

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Regras de limpeza/validação:
    - Remove linhas com nulos nas colunas essenciais
    - Normaliza textos (categoria/produto)
    - Converte data para datetime
    - Remove quantidade <= 0 e valor <= 0
    - Cria coluna 'total' = quantidade * valor
    """
    df = df.copy()

    essential = ["data", "categoria", "produto", "quantidade", "valor"]
    df = df.dropna(subset=essential)

    # Normaliza strings
    df["categoria"] = df["categoria"].astype(str).str.strip().str.title()
    df["produto"] = df["produto"].astype(str).str.strip()

    # Datas
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df = df.dropna(subset=["data"])

    # Números
    df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df = df.dropna(subset=["quantidade", "valor"])

    df = df[(df["quantidade"] > 0) & (df["valor"] > 0)]

    df["total"] = df["quantidade"] * df["valor"]

    # Ordena por data (bom para relatório)
    df = df.sort_values(by="data").reset_index(drop=True)
    return df
