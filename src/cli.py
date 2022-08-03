from packages.fa.dfa import DFA
from packages.fa.nfa import NFA

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
        inputs_dfa(dfa)
    elif type == "@AFN":
        nfa = NFA()
        setup_nfa(nfa)
        nfa.display()
        inputs_nfa(nfa)