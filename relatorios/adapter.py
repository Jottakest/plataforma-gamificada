"""
Adapter para integração com sistema externo de ranking.
Permite enviar dados do relatório sem alterar a Facade principal.
"""

class ExternalRankingService:
    """
    Simulação de serviço externo.
    Normalmente seria uma API REST ou banco externo.
    """
    def send_data(self, data: dict):
        # Simula envio para serviço externo
        print(f"[ExternalRankingService] Dados enviados: {data}")


class ExternalRankingAdapter:
    """
    Adapter que adapta a interface da Facade para o serviço externo.
    """
    def __init__(self):
        self.service = ExternalRankingService()

    def send(self, data: dict):
        # Aqui podemos adaptar campos ou formatos se necessário
        self.service.send_data(data)
        print("[Relatório] Dados enviados para ranking externo via Adapter.")   