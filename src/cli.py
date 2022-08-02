from packages.fa.dfa import DFA
from utils.fa.dfa_setup import setup_dfa,inputs_dfa
from utils.cli_setup import type_machine_input

if __name__ == "__main__":
    type = input()
    type_machine_input(type)
    
    dfa = DFA()
    setup_dfa(dfa)
    inputs_dfa(dfa)