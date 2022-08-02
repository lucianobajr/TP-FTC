from packages.fa.nfa import NFA
import errors.exceptions as exceptions
import re

def setup_nfa(nfa: NFA):
    if isinstance(nfa, NFA) == False:
        raise exceptions.InvalidNFAClass('Você deve passar uma classe NFA')

    print('Q:', end=' ')
    states_tmp = input()

    states = dict()

    for state in states_tmp:
        if state != " ":
            states[len(states)] = state

    nfa.set_states(states)

    print('S:', end=' ')
    sigma = input()
    if len(sigma.strip()) != 0:
        nfa.set_sigma(convert_sigma_to_dict(sigma))

    pattern = r'^[A-Za-z0-9]{1}$'

    print('I:', end=' ')
    initial_states_tmp = input()
    initial_states = dict()

    for state in initial_states_tmp:
        if state != " ":
            if bool(re.match(pattern, state)) == False:
                raise exceptions.InvalidStateError(
                    'Você deve passar um estado inicial válido')
            initial_states[len(initial_states)] = state

    nfa.set_initial_states(initial_states)

    print('F:', end=' ')
    final_states_tmp = input()
    final_states = dict()

    for state in final_states_tmp:
        if state != " ":
            final_states[len(final_states)] = state

    nfa.set_final_states(final_states)

    transitions = dict()

    line = ""

    while True:
        line = input()

        if line != "---":

            from_state = line[0]
            to_state = line[5]
            values = line.split("| ")[1]

            for value in values:
                if value != " ":
                    add_transition_dfa(
                        transitions=transitions, from_state=from_state, to=to_state, value=value)
            line = ""
        else:
            break

    nfa.set_transitions(transitions)


def add_transition_dfa(transitions, from_state, to, value):
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
            transitions[from_state][value_aux] = to
    else:
        transitions[from_state] = {value_aux: to}


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
        raise exceptions.InvalidDFAClass('Você deve passar uma classe NFA')

    while True:
        print('Entrada:', end=' ')
        input_value = input()

        if(input_value == "---"):
            break

        nfa.check_input(input_value)
        input_value = None