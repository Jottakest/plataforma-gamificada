from abc import ABC, abstractmethod
from typing import Final


class AchievementComponent(ABC):
    """Interface para componentes de conquista."""

    @abstractmethod
    def get_points(self) -> int:
        """Retorna os pontos totais do componente."""
        pass


class BaseAchievement(AchievementComponent):
    """Componente base representando pontos simples."""

    def __init__(self, points: int) -> None:
        self._points: Final[int] = points

    def get_points(self) -> int:
        return self._points


class AchievementDecorator(AchievementComponent):
    """Decorator abstrato para aplicar bônus."""

    def __init__(self, component: AchievementComponent) -> None:
        self._component = component

    @abstractmethod
    def get_points(self) -> int:
        pass


class StreakBonus(AchievementDecorator):
    """Bônus por sequência de conquistas (streak)."""

    def __init__(self, component: AchievementComponent, streak_count: int) -> None:
        super().__init__(component)
        self._streak_count = streak_count

    def get_points(self) -> int:
        return self._component.get_points() + self._calculate_bonus()

    def _calculate_bonus(self) -> int:
        return self._streak_count * 10  # 10 pontos por streak


class DoubleXP(AchievementDecorator):
    """Bônus de pontos dobrados."""

    def get_points(self) -> int:
        return self._component.get_points() * 2


# Exemplo de uso
if __name__ == "__main__":
    base = BaseAchievement(50)
    streak = StreakBonus(base, streak_count=3)
    double = DoubleXP(streak)

    print(f"Pontos base: {base.get_points()}")
    print(f"Com streak: {streak.get_points()}")
    print(f"Com double XP: {double.get_points()}")