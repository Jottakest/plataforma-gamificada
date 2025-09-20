"""
Módulo de histórico de ações usando Command Pattern.
Permite registrar ações e desfazer (undo) quando necessário.
"""


class ActionCommand:
    """
    Interface Command abstrata.
    """
    def execute(self):
        raise NotImplementedError("Execute deve ser implementado.")

    def undo(self):
        raise NotImplementedError("Undo deve ser implementado.")


class LogAction(ActionCommand):
    """
    Command concreto que registra uma ação textual.
    """
    def __init__(self, description: str):
        self.description = description

    def execute(self):
        # Apenas registra a ação
        return self.description

    def undo(self):
        # Retorna a ação como 'desfeita'
        return f"{self.description} (desfeito)"


class ActionHistory:
    """
    Invoker/History: mantém a lista de comandos e permite undo.
    """
    def __init__(self):
        self.history = []

    def execute(self, command: ActionCommand):
        result = command.execute()
        self.history.append(command)
        print(f"[Histórico] {result}")

    def undo_last(self):
        if not self.history:
            print("[Histórico] Nenhuma ação para desfazer.")
            return
        command = self.history.pop()
        undone = command.undo()
        print(f"[Histórico] {undone}")

    def clear(self):
        self.history.clear()
        print("[Histórico] Histórico limpo.")
