"""
Módulo de definição dos usuários do sistema.
Inclui classes base e especializações (Aluno, Professor, Visitante).
"""


class User:
    def __init__(self, name: str):
        self.name = name
        self.points = 0
        self.achievements = []

    def add_points(self, points: int):
        """Adiciona pontos ao usuário"""
        self.points += points

    def add_achievement(self, achievement):
        """Adiciona uma conquista ao usuário"""
        self.achievements.append(achievement)

    def __str__(self):
        return f"{self.__class__.__name__}(nome={self.name}, pontos={self.points})"


class Aluno(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.role = "Aluno"


class Professor(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.role = "Professor"


class Visitante(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.role = "Visitante"
