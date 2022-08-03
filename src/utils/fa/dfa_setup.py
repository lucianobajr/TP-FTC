from packages.fa.dfa import DFA
import errors.exceptions as exceptions

def setup_dfa(dfa: DFA):
    if isinstance(dfa, DFA) == False:
        raise exceptions.InvalidDFAClass('Você deve passar uma classe DFA')

    dfa.set_states(set_Q())

    sigma = set_S()
    if sigma != None:
        dfa.set_sigma(sigma)

    dfa.set_initial_state(set_i())
    dfa.set_final_state(set_F())
    dfa.set_transitions(set_transactions())


def add_transition_dfa(transitions, from_state, to, value):
    if from_state in transitions:
        if to in transitions[from_state]:
            transitions[from_state][value] = transitions[from_state][value].union(
                to)
        else:
            transitions[from_state][value] = to
    else:
        transitions[from_state] = {value: to}


def convert_sigma_to_dict(sigma):
    sigma_dict = dict()

    for symbol in sigma:
        if symbol != " ":
            sigma_dict[len(sigma_dict)] = symbol

    return sigma_dict


def inputs_dfa(dfa: DFA):
    if isinstance(dfa, DFA) == False:
        raise exceptions.InvalidDFAClass('Você deve passar uma classe DFA')

    while True:
        print('Entrada:', end=' ')
        input_value = input()

        if(input_value == "---"):
            break

        dfa.check_input(input_value)
        input_value = None


def set_Q():
    print('Q:', end=' ')
    states_tmp = input()

    states = dict()

    states_splited = states_tmp.split(" ")

    for state in states_splited:
        states[len(states)] = state

    return states


def set_S():
    print('S:', end=' ')
    sigma = input()
    if len(sigma.strip()) != 0:
        return convert_sigma_to_dict(sigma)


def set_i():
    print('I:', end=' ')
    initial_state = input()
    initial_state_splited = initial_state.split(" ")

    return initial_state_splited[0]


def set_F():
    print('F:', end=' ')
    final_states_tmp = input()
    final_states = dict()

    final_states_splited = final_states_tmp.split(" ")

    for state in final_states_splited:
        final_states[len(final_states)] = state

    return final_states


def set_transactions():
    transitions = dict()

    line = ""

    while True:
        line = input()

        if line != "---":
            line_splited = line.split(" ")
            line_splited.remove("->")
            line_splited.remove("|")

            from_state = line_splited[0]
            to_state = line_splited[1]
            values = line_splited[2:]

            for value in values:
                add_transition_dfa(transitions, from_state, to_state, value)
            line = ""
        else:
            break

    return transitions