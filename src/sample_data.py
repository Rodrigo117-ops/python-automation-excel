from __future__ import annotations

from pathlib import Path
import random
import pandas as pd


def generate_sample_excel(path: str | Path, rows: int = 60) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    categorias = ["Armas", "Poções", "Comida", "Tecidos", "Minérios"]
    produtos = {
        "Armas": ["Espada", "Machado", "Arco"],
        "Poções": ["Cura", "Mana", "Antídoto"],
        "Comida": ["Pão", "Carne", "Frutas"],
        "Tecidos": ["Algodão", "Seda", "Lã"],
        "Minérios": ["Ferro", "Prata", "Ouro"],
    }

    data_base = pd.Timestamp("2026-01-01")
    records = []
    for _ in range(rows):
        cat = random.choice(categorias)
        prod = random.choice(produtos[cat])
        dia_offset = random.randint(0, 20)

        # coloca alguns erros de propósito (para mostrar limpeza)
        qtd = random.choice([1, 2, 3, 5, 10, -1, 0, None])
        val = random.choice([9.9, 15.0, 25.5, 60.0, -5.0, 0, None])

        records.append(
            {
                "data": (data_base + pd.Timedelta(days=dia_offset)).date(),
                "categoria": cat,
                "produto": prod,
                "quantidade": qtd,
                "valor": val,
            }
        )

    df = pd.DataFrame(records)
    df.to_excel(path, index=False, engine="openpyxl")
    return path
