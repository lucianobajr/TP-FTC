from packages.fa.dfa import DFA
from packages.fa.nfa import NFA
from packages.pa.pda_modified import PDA

from utils.fa.dfa_setup import setup_dfa, inputs_dfa
from utils.fa.nfa_setup import setup_nfa, inputs_nfa

from utils.cli_setup import type_machine_input

if __name__ == "__main__":
    type = input()
    type_machine_input(type)

    if type == "@AFD":
        dfa = DFA()
        setup_dfa(dfa)
        dfa.display()
        # inputs_dfa(dfa)
    elif type == "@AFN":
        nfa = NFA()
        setup_nfa(nfa)
        inputs_nfa(nfa)

    elif type == "@APD":
        pda = PDA(states={'q0', 'q1', 'q2', 'q3'},
                  input_symbols={'a', 'b'},
                  stack_symbols={'0', '1'},
                  transitions={
            'q0': {
                # transition pushes '1' to stack
                'a': {'0': ('q1', ('1', '0'))}
            },
            'q1': {
                'a': {'1': ('q1', ('1', '1'))},
                'b': {'1': ('q2', '')}  # transition pops from stack
            },
            'q2': {
                'b': {'1': ('q2', '')},
                '': {'0': ('q3', ('0',))}  # transition does not change stack
            }
        },
            initial_state='q0',
            initial_stack_symbol='0',
            final_states={'q3'},
            acceptance_mode='both')
        
