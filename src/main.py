from packages.dfa import DFA
from utils.setup import setup_dfa

if __name__ == "__main__":
    dfa = DFA()
    setup_dfa(dfa)
    dfa.check_input('001')
    dfa.check_input('1000')
    dfa.check_input('                          ')
    dfa.check_input('10000011')
    dfa.check_input('111')
    dfa.check_input('1')