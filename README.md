# Plataforma Gamificada de Aprendizagem

**Autores:** José Victor, João Gabriel e João Herik. 
**Curso:** Análise e Desenvolvimento de Sistemas  

---

## Descrição do Projeto

Plataforma de aprendizagem gamificada, desenvolvida para simular um ambiente educacional interativo.  
Alunos participam de desafios, acumulam pontos, desbloqueiam conquistas e interagem em um mural coletivo.  
O sistema aplica **padrões de projeto (GOF)** e **princípios SOLID**, garantindo modularidade, extensibilidade e divisão equilibrada de responsabilidades.

---

## Funcionalidades

### Gerenciamento de Usuários
- Cadastro de diferentes tipos de usuários: **Aluno**, **Professor**, **Visitante**.  
- Controle global de sessão com **Singleton**.  
- Criação de perfis via **Factory Method**.

### Sistema de Desafios
- Criação de desafios programáveis (**QuizChallenge**).  
- Estratégias de pontuação configuráveis (**Strategy**: tempo, dificuldade, acertos).  
- Registro de histórico de ações com **Command** (possibilidade de “undo”).

### Gamificação e Recompensas
- Sistema de conquistas: **pontos, níveis, medalhas**.  
- Bônus aplicáveis com **Decorator** (streak, double XP).  
- Organização hierárquica de conquistas com **Composite**.

### Relatórios e Exportação
- Geração de relatórios em **JSON, CSV e PDF**.  
- Centralização com **Facade**.  
- Integração externa simulada via **Adapter** (ranking global).

### Histórico de Interações
- Registro completo de ações do usuário (**Command**).  
- Permite desfazer ações recentes.  

---

## Estrutura de Pastas

```
/projeto-gamificado/
│
├── app.py # Ponto de entrada da aplicação
├── session.py # Singleton de sessão global
├── README.md
│
├── usuarios/
│ ├── user.py # Classes de usuário
│ └── user_factory.py # Factory Method para criar usuários
│
├── desafios/
│ ├── challenge.py # Definição de desafios
│ └── scoring_strategy.py # Estratégias de pontuação (Strategy)
│
├── gamificacao/
│ ├── achievements.py # Composite + Observer
│ └── decorators.py # Decorator para bônus
│
├── relatorios/
│ ├── facade.py # Facade para exportação de relatórios
│ └── adapter.py # Adapter para ranking externo
│
├── integracoes/
│ └── ranking_adapter.py # Adapter adicional para ranking
│
├── historico/
│ └── command.py # Command Pattern para histórico
│
└── utils/
├── logger.py # Logger simples

```
---

## Tecnologias e Padrões Utilizados

- **Linguagem:** Python 3.x  
- **Padrões de Projeto GOF:**
  - **Criação:** Singleton, Factory Method  
  - **Estruturais:** Decorator, Composite, Adapter, Facade  
  - **Comportamentais:** Observer, Strategy, Command  
- **Bibliotecas:** `fpdf` para exportação de PDF (instalar com `pip install fpdf`)

---

## Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/zevictoros/plataforma-gamificada/
cd plataforma-gamificada
```

2. Instale dependências:

```bash
pip install fpdf
```

3. Execute o sistema:

```bash
python app.py
```

---

## O console exibirá:

- Criação de usuários

- Registro de conquistas

- Execução de quizzes

- Histórico de ações e possibilidade de undo

- Geração de relatórios em JSON, CSV e PDF

- Notificações de conquistas via Observer

---

## Observações

- Todas as lógicas de gamificação foram construídas manualmente, sem frameworks prontos.

- Código modular e documentado, seguindo princípios SOLID.

- Sistema pode ser facilmente expandido (novos tipos de desafios, conquistas, estratégias de pontuação).
