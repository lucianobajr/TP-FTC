# Pushdown Automaton

class Stack:
    def __init__(self):
        self.values = []

    def __repr__(self) -> str:
        return str(self.values)

    def add_value(self, value):
        self.values.append(value)

    def read_value(self):
        self.values.pop()

    def peek(self):
        if not self.checkEmpty():
            return self.values[-1]

    def check_empty(self) -> bool:
        if len(self.values) == 0:
            return True
        return False

class PDA:
    def __init__(self, sigma = set(['0', '1'])):
        self.states = set()             # Q :  conjunto de todos os estados. 
        self.sigma = sigma              # Σ :  conjunto de símbolos de entrada ou alfabeto
        self.initial_state = None       # q0 : estado inicial.
        self.final_state = []           # F :  conjunto de estados finais
        self.transitions = dict()       # δ :  função de Transição
        self.stack = Stack()            # Γ :  conjunto de símbolos de empilhamento