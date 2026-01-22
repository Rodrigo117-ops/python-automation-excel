from __future__ import annotations

import argparse
from pathlib import Path

from loader import load_excel
from cleaner import clean_data
from report import build_summary_tables, save_excel_report
from logger import get_logger
from sample_data import generate_sample_excel


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Automação: limpa planilha Excel e gera relatório em abas."
    )

    parser.add_argument(
        "--input",
        type=str,
        default="data/input_example.xlsx",
        help="Caminho do Excel de entrada (default: data/input_example.xlsx)",
    )

    parser.add_argument(
        "--output",
        type=str,
        default="data/output_report.xlsx",
        help="Caminho do Excel de saída (default: data/output_report.xlsx)",
    )

    parser.add_argument(
        "--make-sample",
        action="store_true",
        help="Gera um Excel de exemplo em --input e sai",
    )

    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        help="Nível de log: DEBUG, INFO, WARNING, ERROR (default: INFO)",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = get_logger(level=args.log_level)

    input_path = Path(args.input)
    output_path = Path(args.output)

    try:
        if args.make_sample:
            logger.info(f"Gerando planilha de exemplo em: {input_path}")
            generate_sample_excel(input_path, rows=80)
            logger.info("OK! Agora rode sem --make-sample para gerar o relatório.")
            return 0

        logger.info(f"Lendo entrada: {input_path}")
        df_raw = load_excel(input_path)
        logger.info(f"Linhas carregadas: {len(df_raw)}")

        logger.info("Limpando e validando dados...")
        df_clean = clean_data(df_raw)
        logger.info(f"Linhas após limpeza: {len(df_clean)}")

        logger.info("Construindo tabelas de relatório...")
        tables = build_summary_tables(df_clean)

        logger.info(f"Salvando relatório em: {output_path}")
        save_excel_report(tables, output_path)

        logger.info("Concluído ✅")
        return 0

    except Exception as e:
        logger.error(f"Erro: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
