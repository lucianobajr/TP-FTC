# Deterministic finite automaton

class DFA:
    def __init__(self, sigma = set(['0', '1'])):
        self.states = set()             # Q : conjunto de todos os estados. 
        self.sigma = sigma              # Σ : conjunto de símbolos de entrada ou alfabeto
        self.initial_state = None       # q : Estado inicial.
        self.final_state = []           # F : conjunto de estado final.
        self.transitions = dict()       # δ : Função de Transição
    
    # estado de erro
    @staticmethod
    def epsilon():
        return ":e:"
    
    def set_states(self,states):
        states_splited = states.split(" ")
        for state in states_splited:
            self.states.add(state)

    def set_initial_state(self, state):
        self.initial_state = state
    
    def add_final_state(self, states):
        for state in states:
            self.final_state.add(state)
    
    def add_transition(self, from_state, to, value):
        if from_state in self.transitions:
            if to in self.transitions[from_state]:
                self.transitions[from_state][to] = self.transitions[from_state][to].union(value)
            else:
                self.transitions[from_state][to] = value
        else:
            self.transitions[from_state] = { to: value}
        
    def add_transtion_in_dictionary(self, transitions):
        for from_state, to in transitions.items():
            for state in to:
                self.add_transition(from_state,state,to[state])

    def display(self):
        print(self.states)
        '''
        print('Σ:'%self.sigma)
        print('q:'%self.initial_state)
        print('F:'%self.final_state)
        print('δ:'%self.transitions)
        '''