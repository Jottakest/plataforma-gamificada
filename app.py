from usuarios.user_factory import UserFactory
from desafios.challenge import QuizChallenge
from desafios.scoring_strategy import TimeBasedScoring, DifficultyBasedScoring
from gamificacao.achievements import Achievement, Medal, AchievementObserver, UserAchievementManager
from relatorios.facade import ReportFacade
from historico.command import ActionHistory, LogAction
from utils.singleton import SessionManager


def main():
    print("=== Plataforma Gamificada ===")

    # Singleton para sessão
    session = SessionManager()
    factory = UserFactory()

    # Criar usuários
    aluno = factory.create_user("aluno", "João")
    professor = factory.create_user("professor", "Maria")
    visitante = factory.create_user("visitante", "Pedro")

    print(f"Usuários criados: {aluno}, {professor}, {visitante}")

    # Gerenciar conquistas com Observer
    observer = AchievementObserver()
    achievement_manager = UserAchievementManager()
    achievement_manager.attach(observer)

    # Criar conquistas
    medal_math = Medal("Medalha Matemática")
    medal_logic = Medal("Medalha Lógica")
    big_achievement = Achievement("Campeão dos Desafios")
    big_achievement.add(medal_math)
    big_achievement.add(medal_logic)

    # Adicionar conquistas para aluno
    achievement_manager.add_achievement(aluno, medal_math)
    achievement_manager.add_achievement(aluno, big_achievement)

    # Criar desafios com Strategy
    quiz = QuizChallenge("Quiz de Matemática", "Matemática básica", strategy=TimeBasedScoring())
    score = quiz.evaluate({"answer": "42"}, {"time": 10, "correct": True})
    aluno.add_points(score)
    print(f"{aluno.name} fez {quiz.title} e ganhou {score} pontos! Total: {aluno.points}")

    quiz2 = QuizChallenge("Quiz de Lógica", "Questões de lógica", strategy=DifficultyBasedScoring())
    score2 = quiz2.evaluate({"answer": "Sim"}, {"difficulty": 3, "correct": True})
    aluno.add_points(score2)
    print(f"{aluno.name} fez {quiz2.title} e ganhou {score2} pontos! Total: {aluno.points}")

    # Histórico de ações com Command
    history = ActionHistory()
    history.execute(LogAction("Respondeu quiz de Matemática"))
    history.execute(LogAction("Respondeu quiz de Lógica"))
    history.undo_last()  # desfaz a última

    print("Histórico de ações:")
    for log in history.history:
        print("-", log.description)

    # Relatórios com Facade
    report_facade = ReportFacade()
    data = {"user": aluno.name, "points": aluno.points}
    print("Gerando relatórios...")
    report_facade.export_all(data, prefix="relatorio_aluno")

    print("=== Fim da execução ===")


if __name__ == "__main__":
    main()
