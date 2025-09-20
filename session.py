"""
Singleton de sessão que centraliza usuários, logs e sessão global.
"""
from threading import Lock


class Session:
    _instance = None
    _lock = Lock()

    def __init__(self):
        if Session._instance is not None:
            raise Exception("Use get_instance() para acessar a instância única.")
        self.users = []
        self.actions = []

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = Session()
            return cls._instance

    def add_user(self, user):
        """Adiciona um usuário ativo na sessão"""
        self.users.append(user)

    def log_action(self, action):
        """Registra uma ação realizada na sessão"""
        self.actions.append(action)

    def get_users(self):
        """Retorna todos os usuários ativos"""
        return self.users

    def get_actions(self):
        """Retorna o histórico de ações"""
        return self.actions


# alias conveniente
Session = Session
class SessionManager:
    def __new__(cls):
        return Session.get_instance()