from packages.fa.nfa import NFA
import errors.exceptions as exceptions


def setup_nfa(nfa: NFA):
    if isinstance(nfa, NFA) == False:
        raise exceptions.InvalidNFAClass('Você deve passar uma classe NFA')

    nfa.set_states(set_Q())

    sigma = set_S()

    if sigma != None:
        nfa.set_sigma(sigma)

    nfa.set_initial_states(set_I())
    nfa.set_final_states(set_F())
    nfa.set_transitions(set_transactions())


def add_transition_nfa(transitions, from_state, to, value):
    value_aux = None

    if value == "\\":
        value_aux = "\\"
    else:
        value_aux = value

    if from_state in transitions:
        if to in transitions[from_state]:
            transitions[from_state][value_aux] = transitions[from_state][value_aux].union(
                to)
        else:
            if value_aux not in transitions[from_state]:
                transitions[from_state][value_aux] = {to}
            else:
                transitions[from_state][value_aux].add(to)

    else:
        transitions[from_state] = {value_aux: {to}}


def convert_sigma_to_dict(sigma):
    sigma_dict = dict()

    for symbol in sigma:
        if symbol != " ":
            if symbol == "\\":
                sigma_dict[len(sigma_dict)] = "\\"
            else:
                sigma_dict[len(sigma_dict)] = symbol

    return sigma_dict


def inputs_nfa(nfa: NFA):
    if isinstance(nfa, NFA) == False:
        raise exceptions.InvalidNFAClass('Você deve passar uma classe NFA')

    while True:
        print('Entrada:', end=' ')
        input_value = input()

        if(input_value == "---"):
            break

        nfa.check_input(input_value)
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


def set_I():
    print('I:', end=' ')
    initial_states_tmp = input()
    initial_states = dict()

    initial_states_splited = initial_states_tmp.split(" ")

    for state in initial_states_splited:
        initial_states[len(initial_states)] = state

    return initial_states


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
                add_transition_nfa(transitions, from_state, to_state, value)
            line = ""
        else:
            break

    return transitions
