from __future__ import annotations

from pathlib import Path
import pandas as pd


def build_summary_tables(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """
    Retorna várias tabelas para escrever em abas do Excel:
    - dados_limpos: dataset final
    - resumo_por_categoria: soma do total por categoria
    - resumo_por_dia: soma do total por dia
    - top_produtos: top 10 produtos por total
    """
    dados_limpos = df.copy()

    resumo_por_categoria = (
        df.groupby("categoria", as_index=False)["total"]
        .sum()
        .sort_values("total", ascending=False)
    )

    resumo_por_dia = (
        df.assign(dia=df["data"].dt.date)
        .groupby("dia", as_index=False)["total"]
        .sum()
        .sort_values("dia", ascending=True)
    )

    top_produtos = (
        df.groupby("produto", as_index=False)["total"]
        .sum()
        .sort_values("total", ascending=False)
        .head(10)
    )

    return {
        "dados_limpos": dados_limpos,
        "resumo_por_categoria": resumo_por_categoria,
        "resumo_por_dia": resumo_por_dia,
        "top_produtos": top_produtos,
    }


def save_excel_report(tables: dict[str, pd.DataFrame], output_path: str | Path) -> Path:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for sheet_name, table in tables.items():
            safe_name = sheet_name[:31]  # limite do Excel
            table.to_excel(writer, sheet_name=safe_name, index=False)

    return output_path
