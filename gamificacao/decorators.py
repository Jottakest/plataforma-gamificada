"""
Módulo de Decorators para aplicar bônus em pontos ou conquistas.
Ex.: streak, double XP, bônus temporário.
"""

from abc import ABC, abstractmethod


class AchievementComponent(ABC):
    @abstractmethod
    def get_points(self) -> int:
        """Retorna os pontos do componente"""
        pass


class BaseAchievement(AchievementComponent):
    """Componente base representando pontos simples"""

    def __init__(self, points: int):
        self.points = points

    def get_points(self) -> int:
        return self.points


class AchievementDecorator(AchievementComponent):
    """Decorator abstrato"""

    def __init__(self, component: AchievementComponent):
        self.component = component

    @abstractmethod
    def get_points(self) -> int:
        pass


class StreakBonus(AchievementDecorator):
    """Bônus por sequência de conquistas (streak)"""

    def __init__(self, component: AchievementComponent, streak_count: int):
        super().__init__(component)
        self.streak_count = streak_count

    def get_points(self) -> int:
        base = self.component.get_points()
        bonus = self.streak_count * 10  # exemplo: 10 pontos por streak
        return base + bonus


class DoubleXP(AchievementDecorator):
    """Bônus de pontos dobrados"""

    def get_points(self) -> int:
        base = self.component.get_points()
        return base * 2


# Exemplo de uso quando executado diretamente
if __name__ == "__main__":
    base = BaseAchievement(50)
    streak = StreakBonus(base, streak_count=3)
    double = DoubleXP(streak)
    print("Pontos base:", base.get_points())
    print("Com streak:", streak.get_points())
    print("Com double XP:", double.get_points())
