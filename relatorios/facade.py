"""
Facade para relatórios.
Centraliza geração em múltiplos formatos e integração externa (Adapter).
"""

import json
import csv
from fpdf import FPDF  # certifique-se de instalar com `pip install fpdf`
from relatorios.adapter import ExternalRankingAdapter


class ReportFacade:
    """
    Facade para exportar relatórios em diferentes formatos.
    """

    def export_all(self, data: dict, prefix: str = "report"):
        """
        Exporta dados em JSON, CSV e PDF.
        :param data: Dicionário com dados do relatório
        :param prefix: Prefixo do nome dos arquivos
        """
        self.export_json(data, f"{prefix}.json")
        self.export_csv(data, f"{prefix}.csv")
        self.export_pdf(data, f"{prefix}.pdf")
        self.send_to_external(data)

    def export_json(self, data: dict, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"[Relatório] JSON exportado: {filename}")

    def export_csv(self, data: dict, filename: str):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # cabeçalho
            writer.writerow(data.keys())
            # linha de valores
            writer.writerow(data.values())
        print(f"[Relatório] CSV exportado: {filename}")

    def export_pdf(self, data: dict, filename: str):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Relatório", ln=True, align="C")
        pdf.ln(10)
        for key, value in data.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
        pdf.output(filename)
        print(f"[Relatório] PDF exportado: {filename}")

    def send_to_external(self, data: dict):
        """
        Simula envio de dados para ranking externo via Adapter.
        """
        adapter = ExternalRankingAdapter()
        adapter.send(data)
