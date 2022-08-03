# Nondeterministic finite automaton

import errors.exceptions as exceptions
import json


class NFA:
    def __init__(self, sigma={0: '0', 1: '1', 2: '\\'}):
        self.states = dict()             # Q : conjunto de todos os estados.
        self.sigma = sigma               # Σ : conjunto de símbolos de entrada ou alfabeto
        # Q : conjunto não vazio de estados iniciais.
        self.initial_states = dict()
        self.final_states = dict()       # F : conjunto de estados finais
        self.transitions = dict()        # δ : função de Transição

        # estado de erro
    @staticmethod
    def epsilon():
        return ":e:"

    def set_states(self, states):
        self.states = states.copy()

    def set_initial_states(self, states):
        self.initial_state = states.copy()

    def set_final_states(self, states):
        self.final_states = states.copy()

    def set_transitions(self, transitions):
        self.transitions = transitions

    def set_sigma(self, sigma):
        self.sigma = sigma.copy()

    def add_initial_state(self, states):
        for state in states:
            self.initial_state.add(state)

    def add_final_state(self, states):
        for state in states:
            self.final_states.add(state)

    def check_symbol_in_sigma(self, symbol):
        if(symbol in self.sigma.values()):
            pass
        else:
            raise exceptions.InvalidSymbolError('Invalid Symbol!')

    def get_next_current_state(self, current_state, input_symbol):
        """
        Follow the transition for the given input symbol on the current state.
        Raise an error if the transition does not exist.
        """
        if input_symbol in self.transitions[current_state]:
            return self.transitions[current_state][input_symbol]

    def check_for_input_rejection(self, current_state):
        if current_state not in self.final_states:
            print(False)

    def check(self, string):
        initial_states_used = self.initial_states.copy()
        print(initial_states_used)

        return False

    def check_input(self, input_str):
        '''
            Confere que se o estado em que encerrou a computação é final
        '''

        state = self.check(input_str)

        if state == True:
            print("OK")
        else:
            print("X")

    def display(self):
        print('\n--------NFA--------\n')
        print('Q: {}'.format(self.states))
        print('Σ: {}'.format(self.sigma))
        print('q: {}'.format(self.initial_state))
        print('F: {}'.format(self.final_states))
        print('δ: {}'.format(json.dumps(self.transitions, indent=4, sort_keys=True)))
        print('\n--------NFA--------\n')
