"""
Módulo de estratégias de pontuação.
Implementa Strategy para calcular pontos de formas diferentes.
"""
from abc import ABC, abstractmethod


class ScoringStrategy(ABC):
    @abstractmethod
    def calculate_score(self, submission, context) -> int:
        """
        Calcula a pontuação baseada na submissão e no contexto.
        :param submission: Resposta do usuário
        :param context: Dados auxiliares (ex.: tempo, dificuldade, acerto)
        :return: Pontos ganhos
        """
        pass


class TimeBasedScoring(ScoringStrategy):
    """
    Estratégia baseada em tempo.
    Quanto menor o tempo, maior a pontuação.
    """
    def calculate_score(self, submission, context) -> int:
        if not context.get("correct", False):
            return 0
        time = context.get("time", 999)
        return max(0, 100 - time)


class DifficultyBasedScoring(ScoringStrategy):
    """
    Estratégia baseada na dificuldade.
    Multiplica pontos conforme a dificuldade do desafio.
    """
    def calculate_score(self, submission, context) -> int:
        if not context.get("correct", False):
            return 0
        difficulty = context.get("difficulty", 1)
        return 10 * difficulty


class AccuracyBasedScoring(ScoringStrategy):
    """
    Estratégia baseada em acertos percentuais (ex.: quizzes com várias questões).
    """
    def calculate_score(self, submission, context) -> int:
        accuracy = context.get("accuracy", 0.0)
        return int(accuracy * 100)
