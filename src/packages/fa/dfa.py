# Deterministic finite automaton

import errors.exceptions as exceptions
import json

'''initial_states_used.pop(i)
            for symbol in string:
                self.check_symbol_in_sigma(symbol=symbol)
                if symbol in self.transitions[current_state_value]:
                    print(self.transitions[current_state_value][symbol])

            if current_state_value in self.final_states.values():
                return True
            
        return False
for state in self.transitions[current_state_value][symbol]:
                        current_state_value = self.transitions[current_state_value][symbol][state]
'''

class DFA:
    def __init__(self, sigma={0: '0', 1: '1'}):
        self.states = dict()              # Q : conjunto de todos os estados.
        self.sigma = sigma                # Σ : conjunto de símbolos de entrada ou alfabeto
        self.initial_state = None         # q : estado inicial.
        self.final_state = dict()         # F : conjunto de estado final.
        self.transitions = dict()         # δ : função de Transição

    # estado de erro
    @staticmethod
    def epsilon():
        return ":e:"

    def set_states(self, states):
        self.states = states.copy()

    def set_initial_state(self, state):
        self.initial_state = str(state)

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
        if(symbol in self.sigma.values()):
            pass
        else:
            raise exceptions.InvalidSymbolError('Invalid Symbol!')

    def get_next_current_state(self, current_state, input_symbol):
        """
        Siga a transição para o símbolo de entrada fornecido no estado atual.
        Gere um erro se a transição não existir.
        """
        if input_symbol in self.transitions[current_state]:
            return self.transitions[current_state][input_symbol]

    def check_for_input_rejection(self, current_state):
        if current_state not in self.final_state:
            print(False)

    def current_state(self, string):
        current_state_value = self.initial_state

        if len(string.strip()) == 0:
            return current_state_value
        else:
            for symbol in string:
                self.check_symbol_in_sigma(symbol=symbol)
                current_state_value = self.get_next_current_state(
                    current_state_value, symbol)

            return current_state_value

    def check_input(self, input_str):
        '''
            Confere que se o estado em que encerrou a computação é final
        '''
        if self.input_check(input_str):
            print("OK")
        else:
            print("X")

    def display(self):
        print('\n--------DFA--------\n')
        print('Q: {}'.format(self.states))
        print('Σ: {}'.format(self.sigma))
        print('q: {}'.format(self.initial_state))
        print('F: {}'.format(self.final_state))
        print('δ: {}'.format(json.dumps(self.transitions, indent=4, sort_keys=True)))
        print('\n--------DFA--------\n')