from models.dfa import DFA

if __name__ == "__main__":
    dfa = DFA()
    print("Q:", end = ' ')
    states = input()
    dfa.set_states(states)
    dfa.display()