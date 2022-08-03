# Pushdown Automaton
# Desempilha/Empilha
from typing_extensions import Self
import errors.exceptions as exceptions
import json


class Stack:
    def __init__(self):
        self.values = []

    def __repr__(self) -> str:
        return str(self.values)

    def stack(self, value):
        self.values.append(value)

    def unstack(self, value):
        if self.peek == value:
            self.values.pop(value)
    # Retorna objeto no topo da pilha
    def peek(self):
        if not self.checkEmpty():
            return self.values[-1]

    def check_empty(self) -> bool:
        if len(self.values) == 0:
            return True
        return False

class PDA:
    def __init__(self, sigma = set(['0', '1']),):
        self.states = set()             # Q :  conjunto de todos os estados. 
        self.sigma = sigma              # Σ :  conjunto de símbolos de entrada ou alfabeto
        self.stack_symbols = []
        self.initial_state = None       # q0 : estado inicial.
        self.final_state = []           # F :  conjunto de estados finais
        self.transitions = dict()       # δ :  função de Transição
        self.stack = Stack()            # Γ :  conjunto de símbolos de empilhamento
    
    def set_states(self, states):
        self.states = states.copy()
    
    def set_initial_state(self, state):
        self.initial_state = str(state)
    
    def set_stack(self, stacks):
        self.stack_symbols = stacks.copy()
    
    def set_final_state(self, states):
        self.final_state = states.copy()

    def set_transitions(self, transitions):
        self.transitions = transitions
    
    def set_sigma(self, sigma):
        self.sigma = sigma.copy()
    
    def add_final_state(self, states):
        for state in states:
            self.final_state.add(state)

    def check_symbol_in_sigma(self, symbol):
        if (symbol in self.sigma.values()):
            pass
        else:
            raise exceptions.InvalidSymbolError('Invalid Symbol!')     


    def transition(self, current_state, input_symbol, unstack, stack):
        
        if input_symbol in self.transition[current_state]:
            self.stack.stack(stack)
            self.stack.unstack(unstack)

            return self.transitions[current_state][input_symbol]
    
    def input_rejection(self, current_state):
        if current_state not in self.final_state and not self.stack.check_empty():
            print(False) 

    def current_state(self, string):
        current_state_value = self.initial_state

        if len(string.strip()) == 0:
            return current_state_value
        else:
            for symbol in string:
                self.check_symbol_in_sigma(symbol=symbol)
                current_state_value = self.transition(current_state_value)

