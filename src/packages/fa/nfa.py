# Nondeterministic finite automaton

import errors.exceptions as exceptions
from collections import deque


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
        self.initial_states = states.copy()

    def set_final_states(self, states):
        self.final_states = states.copy()

    def set_transitions(self, transitions):
        self.transitions = transitions

    def set_sigma(self, sigma):
        self.sigma = sigma.copy()

    def add_initial_state(self, states):
        for state in states:
            self.initial_states.add(state)

    def add_transition(self, from_state, to, value):
        value_aux = None

        if value == "\\":
            value_aux = "\\"
        else:
            value_aux = value
        
        if from_state in self.transitions:
            if to in self.transitions[from_state]:
                self.transitions[from_state][value_aux] = self.transitions[from_state][value_aux].union(
                    to)
            else:
                if value_aux not in self.transitions[from_state]:
                    self.transitions[from_state][value_aux] = {to}
                else:
                    self.transitions[from_state][value_aux].add(to)
        else:
            self.transitions[from_state] = {value_aux: {to}}

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

    def _transitions_pairs(self):
        all_transitions = self.transitions.deepcopy()
        transition_possibilities: list = []
        for state, state_transitions in all_transitions.items():
            for symbol, transitions in state_transitions.items():
                if len(transitions) < 2:
                    if transitions != "" and transitions != {}:
                        transitions = transitions.pop()
                    transition_possibilities.append(
                        (state, transitions, symbol)
                    )
                else:
                    for transition in transitions:
                        transition_possibilities.append(
                            (state, transition, symbol)
                        )
        return transition_possibilities

    def check(self, string):
        q = deque()  # queue -> states from i to last character in S | (index, state)
        q.append([0, self.initial_states[0]])  # Starts from 0
        ans = False  # Flag

        while q and not ans:
            front = q.popleft()
            index = front[0]
            state = front[1]

            if index == len(string):
                if state in self.final_states.values():
                    ans = True
            elif string[index] not in self.sigma.values():
                raise exceptions.InvalidSymbolError(
                    string[index], 'Is not declared in sigma')
            elif state in self.transitions:
                # Search through states
                for transition in self.transitions[state].items():
                    d = transition[0]
                    states = transition[1]

                    if d == "\\":
                        # Is epsilon
                        for state in states:
                            # Do not consume character
                            q.append([index, state])
                    elif string[index] == d:
                        for state in states:
                            # Consume character
                            q.append([index + 1, state])

        if len(string.strip()) == 0 and "\\" in self.sigma.values():
            ans = True

        return ans

    def check_input(self, input_str):
        '''
            Confere que se o estado em que encerrou a computação é final
        '''

        if self.check(input_str) == True:
            print("OK")
        else:
            print("X")

    def display(self):
        print('\n--------NFA--------\n')
        print('Q: {}'.format(self.states))
        print('Σ: {}'.format(self.sigma))
        print('q: {}'.format(self.initial_states))
        print('F: {}'.format(self.final_states))
        print('δ: {}'.format(self.transitions))
        print('\n--------NFA--------\n')
