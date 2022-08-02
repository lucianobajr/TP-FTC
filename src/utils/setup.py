from packages.dfa import DFA
import errors.exceptions as exceptions
import re

def setup_dfa(dfa: DFA):
    if isinstance(dfa,DFA) == False:
        raise exceptions.InvalidDFAClass('Você deve passar uma classe DFA')
    
    print('Q:',end=' ')
    states_tmp = input()

    states = dict()

    for state in states_tmp:
        if state != " ":
            states[len(states)] = state
    
    dfa.set_states(states)

    pattern = r'^[A-Za-z0-9]{1}$'


    print('I:',end=' ')
    initial_state = input()
    if bool(re.match(pattern,initial_state[0])) == False:
        raise exceptions.InvalidStateError('Você deve passar um estado inicial válido')
    
    dfa.set_initial_state(initial_state[0])

    print('F:',end=' ')
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
            to_state = line [5]
            values = line.split("| ")[1]

            for value in values:
                if value != " ":
                    add_transition(transitions=transitions,from_state=from_state,to=to_state,value=value)
            line = ""
        else:
            break

    dfa.set_transitions(transitions)
    

def add_transition(transitions, from_state, to, value):
        if from_state in transitions:
            if to in transitions[from_state]:
                transitions[from_state][value] = transitions[from_state][value].union(to)
            else:
                transitions[from_state][value] = to
        else:
            transitions[from_state] = {value: to}

def inputs_dfa(dfa: DFA):
    if isinstance(dfa,DFA) == False:
        raise exceptions.InvalidDFAClass('Você deve passar uma classe DFA')

    input_value = input()
    dfa.read_input_stepwise(input_value)
    input_value = ''