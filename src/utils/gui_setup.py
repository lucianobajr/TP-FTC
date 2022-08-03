def convert_sigma_to_dict(sigma):
        sigma_dict = dict()

        for symbol in sigma:
            if symbol != " ":
                sigma_dict[len(sigma_dict)] = symbol

        return sigma_dict

def convert_sigma_to_dict_NFA(sigma):
    sigma_dict = dict()

    for symbol in sigma:
        if symbol != " ":
            sigma_dict[len(sigma_dict)] = symbol

    return sigma_dict

def set_Q(states_tmp):
    states = dict()

    states_splited = states_tmp.split(" ")

    for state in states_splited:
        states[len(states)] = state

    return states

def set_S_dfa(sigma):
    if len(sigma.strip()) != 0:
        return convert_sigma_to_dict(sigma)

def set_S_nfa(sigma):
    if len(sigma.strip()) != 0:
        return convert_sigma_to_dict_NFA(sigma)

def set_i(initial_state):
    initial_state_splited = initial_state.split(" ")

    return initial_state_splited[0]

def set_I(initial_states_tmp):
    initial_states = dict()

    initial_states_splited = initial_states_tmp.split(" ")

    for state in initial_states_splited:
        initial_states[len(initial_states)] = state

    return initial_states

def set_F(final_states_tmp):
    final_states = dict()

    final_states_splited = final_states_tmp.split(" ")

    for state in final_states_splited:
        final_states[len(final_states)] = state

    return final_states

def add_transition_dfa(transitions, from_state, to, value):
    if from_state in transitions:
        if to in transitions[from_state]:
            transitions[from_state][value] = transitions[from_state][value].union(
                to)
        else:
            transitions[from_state][value] = to
    else:
        transitions[from_state] = {value: to}

def set_transactions_dfa(transitions,line):

    line_splited = line.split(" ")
    line_splited.remove("->")
    line_splited.remove("|")

    from_state = line_splited[0]
    to_state = line_splited[1]
    values = line_splited[2:]

    for value in values:
        add_transition_dfa(transitions, from_state, to_state, value)

    return transitions

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

def set_transactions_nfa(transitions,line):
    line_splited = line.split(" ")
    line_splited.remove("->")
    line_splited.remove("|")

    from_state = line_splited[0]
    to_state = line_splited[1]
    values = line_splited[2:]

    for value in values:
        add_transition_nfa(transitions, from_state, to_state, value)

    return transitions