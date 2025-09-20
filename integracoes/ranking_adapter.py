"""
Adapter para integração com sistema externo de ranking.
Permite enviar dados de usuários e pontos sem alterar o core do sistema.
"""

class ExternalRankingService:
    """
    Simulação de serviço externo de ranking.
    Normalmente seria uma API REST ou banco externo.
    """
    def send_data(self, user_data: dict):
        # Simula envio para serviço externo
        print(f"[RankingService] Dados enviados: {user_data}")


class RankingAdapter:
    """
    Adapter que adapta a interface do sistema para o serviço externo.
    """
    def __init__(self):
        self.service = ExternalRankingService()

    def send_user_ranking(self, user):
        """
        Adapta os dados do usuário para o formato esperado pelo serviço externo.
        """
        data = {
            "nome": getattr(user, "name", ""),
            "pontos": getattr(user, "points", 0),
            "conquistas": [a.name for a in getattr(user, "achievements", [])]
        }
        self.service.send_data(data)
