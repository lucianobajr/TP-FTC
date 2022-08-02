from packages.fa.dfa import DFA
import errors.exceptions as exceptions
import re


def setup_dfa(dfa: DFA):
    if isinstance(dfa, DFA) == False:
        raise exceptions.InvalidDFAClass('Você deve passar uma classe DFA')

    print('Q:', end=' ')
    states_tmp = input()

    states = dict()

    for state in states_tmp:
        if state != " ":
            states[len(states)] = state

    dfa.set_states(states)

    print('S:', end=' ')
    sigma = input()
    if len(sigma.strip()) != 0:
        dfa.set_sigma(convert_sigma_to_dict(sigma))

    pattern = r'^[A-Za-z0-9]{1}$'

    print('I:', end=' ')
    initial_state = input()
    if bool(re.match(pattern, initial_state[0])) == False:
        raise exceptions.InvalidStateError(
            'Você deve passar um estado inicial válido')

    dfa.set_initial_state(initial_state[0])

    print('F:', end=' ')
    final_states_tmp = input()
    final_states = dict()

    for state in final_states_tmp:
        if state != " ":
            final_states[len(final_states)] = state

    dfa.set_final_state(final_states)

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
                    add_transition_dfa(transitions=transitions,
                                       from_state=from_state, to=to_state, value=value)
            line = ""
        else:
            break

    dfa.set_transitions(transitions)


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