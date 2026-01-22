from __future__ import annotations

from pathlib import Path
import pandas as pd


REQUIRED_COLUMNS = ["data", "categoria", "produto", "quantidade", "valor"]


def load_excel(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_excel(path, engine="openpyxl")

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(
            f"Colunas obrigatórias ausentes: {missing}. "
            f"Encontradas: {list(df.columns)}"
        )

    return df
