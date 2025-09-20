"""
Módulo de conquistas (achievements) — implementação completa.

Implementa os padrões:
- Composite (MedalCollection)
- Observer (AchievementCenter notifica observers quando uma conquista é desbloqueada)
"""

from typing import List
from dataclasses import dataclass, field


@dataclass
class Achievement:
    name: str
    points_required: int = 0
    description: str = ""

    def is_unlocked(self, user) -> bool:
        """Verifica se o usuário atende à condição desta conquista."""
        return getattr(user, 'points', 0) >= self.points_required

    def to_dict(self) -> dict:
        return {"name": self.name, "points_required": self.points_required, "description": self.description}

    def __str__(self) -> str:
        return f"Achievement({self.name})"


class Medal(Achievement):
    """Alias semântico para Medalha."""
    pass


class MedalCollection(Achievement):
    """Composite: coleção de achievements/medalhas."""

    def __init__(self, name: str, description: str = ""):
        super().__init__(name=name, points_required=0, description=description)
        self.children: List[Achievement] = []

    def add(self, achievement: Achievement):
        self.children.append(achievement)

    def remove(self, achievement: Achievement):
        self.children.remove(achievement)

    def is_unlocked(self, user) -> bool:
        user_medal_names = [m.name for m in getattr(user, 'achievements', [])]
        for c in self.children:
            if c.name not in user_medal_names:
                return False
        return True

    def to_dict(self) -> dict:
        return {"name": self.name, "children": [c.to_dict() for c in self.children], "description": self.description}

    def __str__(self) -> str:
        return f"MedalCollection({self.name}) -> [{', '.join(c.name for c in self.children)}]"


class AchievementCenter:
    """Centro de conquistas com Observer pattern."""

    def __init__(self):
        self.subscribers: List = []
        self.registry_medals: List[Achievement] = []
        self.registry_collections: List[MedalCollection] = []

    def subscribe(self, observer):
        if observer not in self.subscribers:
            self.subscribers.append(observer)

    def unsubscribe(self, observer):
        if observer in self.subscribers:
            self.subscribers.remove(observer)

    def notify(self, user, achievement: Achievement):
        for s in self.subscribers:
            s.update(user, achievement)

    def register_medal(self, medal: Achievement):
        if not any(m.name == medal.name for m in self.registry_medals):
            self.registry_medals.append(medal)

    def register_collection(self, collection: MedalCollection):
        if not any(c.name == collection.name for c in self.registry_collections):
            self.registry_collections.append(collection)

    def check_achievements(self, user) -> List[Achievement]:
        unlocked: List[Achievement] = []
        user_achievements = [a.name for a in getattr(user, 'achievements', [])]

        # Medals
        for m in self.registry_medals:
            if m.is_unlocked(user) and m.name not in user_achievements:
                user.add_achievement(m)
                unlocked.append(m)
                self.notify(user, m)
                user_achievements.append(m.name)

        # Collections
        for c in self.registry_collections:
            if c.is_unlocked(user) and c.name not in user_achievements:
                user.add_achievement(c)
                unlocked.append(c)
                self.notify(user, c)
                user_achievements.append(c.name)

        return unlocked


class AchievementObserver:
    """Observer simples que exibe notificações no console."""

    def update(self, user, achievement: Achievement):
        print(f"[NOTIF] {getattr(user, 'name', 'Usuário')} desbloqueou: {achievement.name}")
