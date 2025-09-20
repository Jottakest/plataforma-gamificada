"""
Factory Method para criação de diferentes tipos de usuários.
"""
from usuarios.user import Aluno, Professor, Visitante


class UserFactory:
    def create_user(self, user_type: str, name: str):
        """
        Cria usuários de acordo com o tipo informado.
        :param user_type: Tipo de usuário ('aluno', 'professor', 'visitante')
        :param name: Nome do usuário
        :return: Instância de User
        """
        user_type = user_type.lower()

        if user_type == "aluno":
            return Aluno(name)
        elif user_type == "professor":
            return Professor(name)
        elif user_type == "visitante":
            return Visitante(name)
        else:
            raise ValueError(f"Tipo de usuário inválido: {user_type}")
