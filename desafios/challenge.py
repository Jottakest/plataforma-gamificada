"""
Módulo de definição de desafios (ex.: quizzes, exercícios de código).
Usa Strategy para calcular pontuação de acordo com regras diferentes.
"""
from desafios.scoring_strategy import ScoringStrategy


class Challenge:
    def __init__(self, title: str, description: str, strategy: ScoringStrategy):
        self.title = title
        self.description = description
        self.strategy = strategy

    def evaluate(self, submission, context) -> int:
        """
        Avalia a submissão usando a estratégia de pontuação configurada.
        :param submission: Resposta do usuário
        :param context: Dados auxiliares (ex.: tempo, dificuldade, acerto)
        :return: Pontos ganhos
        """
        return self.strategy.calculate_score(submission, context)


class QuizChallenge(Challenge):
    def __init__(self, title: str, description: str, strategy: ScoringStrategy):
        super().__init__(title, description, strategy)
        self.questions = []

    def add_question(self, question, answer):
        """Adiciona uma questão ao quiz"""
        self.questions.append({"question": question, "answer": answer})

    def check_answer(self, submission, correct_answer) -> bool:
        """Verifica se a resposta está correta"""
        return submission == correct_answer
