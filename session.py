from threading import Lock
from typing import Any


class Session:
    """
    Singleton de sessão que centraliza usuários ativos e logs de ações.
    Thread-safe para garantir consistência em ambientes concorrentes.
    """

    _instance = None
    _lock = Lock()

    def __init__(self):
        if Session._instance is not None:
            raise RuntimeError("Use Session.get_instance() para acessar a instância única.")
        self._users: list[str] = []
        self._actions: list[Any] = []
        self._data_lock = Lock()

    @classmethod
    def get_instance(cls) -> "Session":
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance

    def add_user(self, user: str) -> None:
        """Adiciona um usuário ativo na sessão (thread-safe)."""
        with self._data_lock:
            if user not in self._users:
                self._users.append(user)

    def remove_user(self, user: str) -> None:
        """Remove um usuário da sessão (thread-safe)."""
        with self._data_lock:
            if user in self._users:
                self._users.remove(user)

    def log_action(self, action: Any) -> None:
        """Registra uma ação realizada na sessão (thread-safe)."""
        with self._data_lock:
            self._actions.append(action)

    def get_users(self) -> tuple[str, ...]:
        """Retorna os usuários ativos (imutável)."""
        with self._data_lock:
            return tuple(self._users)

    def get_actions(self) -> tuple[Any, ...]:
        """Retorna o histórico de ações (imutável)."""
        with self._data_lock:
            return tuple(self._actions)


class SessionManager:
    """Atalho para acessar a instância da sessão global."""
    def __new__(cls) -> Session:
        return Session.get_instance()
