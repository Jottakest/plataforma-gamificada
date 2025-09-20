"""
Módulo de logging simples.
Permite registrar mensagens com diferentes níveis.
"""

import datetime


class Logger:
    LEVELS = ("INFO", "WARNING", "ERROR", "DEBUG")

    def __init__(self):
        self.logs = []

    def log(self, message: str, level: str = "INFO"):
        """
        Registra uma mensagem no log.
        :param message: Mensagem de log
        :param level: Nível (INFO, WARNING, ERROR, DEBUG)
        """
        if level not in self.LEVELS:
            level = "INFO"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level}] {message}"
        self.logs.append(entry)
        print(entry)

    def get_logs(self):
        """Retorna todas as mensagens registradas"""
        return self.logs

    def clear_logs(self):
        """Limpa o histórico de logs"""
        self.logs.clear()
        print("[Logger] Logs limpos.")


# Alias conveniente
logger = Logger()
# Exemplo de uso:
# logger.log("Sistema iniciado", "INFO")