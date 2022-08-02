# Nondeterministic finite automaton

class NFA:
    def __init__(self, sigma = set(['0', '1'])):
        self.states = set()             # Q : conjunto de todos os estados. 
        self.sigma = sigma              # Σ : conjunto de símbolos de entrada ou alfabeto
        self.initial_states = []        # I : conjunto não vazio de estados iniciais.
        self.final_state = []           # F : conjunto de estados finais
        self.transitions = dict()       # δ : função de Transição