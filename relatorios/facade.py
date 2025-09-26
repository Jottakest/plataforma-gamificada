import json
import csv
import os
from typing import Union, List, Dict
from fpdf import FPDF
from relatorios.adapter import ExternalRankingAdapter


class ReportFacade:
    """
    Facade para exportar relatórios em diferentes formatos e integrar com sistemas externos.
    """

    def export_all(self, data: Union[Dict, List[Dict]], prefix: str = "report") -> None:
        """
        Exporta dados em JSON, CSV e PDF, e envia para sistema externo.
        :param data: Dicionário ou lista de dicionários com dados do relatório
        :param prefix: Prefixo do nome dos arquivos
        """
        try:
            self.export_json(data, f"{prefix}.json")
            self.export_csv(data, f"{prefix}.csv")
            self.export_pdf(data, f"{prefix}.pdf")
            self.send_to_external(data)
        except Exception as e:
            print(f"[Erro] Falha ao exportar relatório: {e}")

    def export_json(self, data: Union[Dict, List[Dict]], filename: str) -> None:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"[Relatório] JSON exportado: {os.path.abspath(filename)}")
        except Exception as e:
            print(f"[Erro] Falha ao exportar JSON: {e}")

    def export_csv(self, data: Union[Dict, List[Dict]], filename: str) -> None:
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)

                if isinstance(data, dict):
                    writer.writerow(data.keys())
                    writer.writerow(data.values())
                elif isinstance(data, list) and all(isinstance(row, dict) for row in data):
                    headers = data[0].keys()
                    writer.writerow(headers)
                    for row in data:
                        writer.writerow([row.get(h, "") for h in headers])
                else:
                    raise ValueError("Formato de dados inválido para CSV.")

            print(f"[Relatório] CSV exportado: {os.path.abspath(filename)}")
        except Exception as e:
            print(f"[Erro] Falha ao exportar CSV: {e}")

    def export_pdf(self, data: Union[Dict, List[Dict]], filename: str) -> None:
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Relatório", ln=True, align="C")
            pdf.ln(10)

            if isinstance(data, dict):
                for key, value in data.items():
                    pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
            elif isinstance(data, list):
                for idx, row in enumerate(data, start=1):
                    pdf.cell(200, 10, txt=f"Item {idx}", ln=True)
                    for key, value in row.items():
                        pdf.cell(200, 10, txt=f"  {key}: {value}", ln=True)
                    pdf.ln(5)

            pdf.output(filename)
            print(f"[Relatório] PDF exportado: {os.path.abspath(filename)}")
        except Exception as e:
            print(f"[Erro] Falha ao exportar PDF: {e}")

    def send_to_external(self, data: Union[Dict, List[Dict]]) -> None:
        """
        Envia dados para sistema externo via Adapter.
        """
        try:
            adapter = ExternalRankingAdapter()
            adapter.send(data)
            print("[Relatório] Dados enviados ao sistema externo com sucesso.")
        except Exception as e:
            print(f"[Erro] Falha ao enviar dados para sistema externo: {e}")