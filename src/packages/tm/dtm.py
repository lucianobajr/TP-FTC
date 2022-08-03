#!/usr/bin/env python3
"""Classes and methods for working with deterministic Turing machines."""

import errors.exceptions as exceptions
import collections

class TMConfiguration(collections.namedtuple(
    'TMConfiguration',
    ['state', 'tape']
)):
    """A Turing machine configuration."""

    def __repr__(self):
        """Return a string representation of the configuration."""
        return '{}(\'{}\', {})'.format(
            self.__class__.__name__, self.state, self.tape
        )

    def print(self):
        """Print the machine's current configuration in a readable form."""
        print('{current_state}: {tape}\n{current_position}'.format(
            current_state=self.state,
            tape=''.join(self.tape).rjust(
                len(self.tape),
                self.tape.blank_symbol),
            current_position='^'.rjust(
                self.tape.current_position + len(self.state) + 3
            ),
        ))

class TMTape(collections.namedtuple(
    'TMTape',
    ['tape', 'blank_symbol', 'current_position']
)):
    """A Turing machine tape."""

    def __new__(cls, tape, *, blank_symbol, current_position=0):
        """Initialize a new Turing machine tape."""
        tape = list(tape)
        # Make sure that there's something under the cursor.
        while len(tape) <= current_position:
            tape.append(blank_symbol)
        tape = tuple(tape)
        return super(TMTape, cls).__new__(
            cls, tape, blank_symbol, current_position
        )

    def load_symbols(self, input_str, head):
        """Loads a given string in tape and sets the head to the given
        value."""
        return TMTape(
            list(input_str),
            blank_symbol=self.blank_symbol,
            current_position=head
        )

    def read_symbol(self):
        """Read the symbol at the current position in the tape."""
        return self.tape[self.current_position]

    def write_symbol(self, new_tape_symbol):
        """Write the given symbol at the current position in the tape."""
        tape_elements = list(self.tape)
        tape_elements[self.current_position] = new_tape_symbol
        return TMTape(
            tape_elements,
            blank_symbol=self.blank_symbol,
            current_position=self.current_position
        )

    def move(self, direction):
        """Move the tape to the next symbol in the given direction."""
        # Copy stuff.
        new_tape = list(self.tape)
        new_position = self.current_position
        if direction == 'R':
            new_position += 1
        elif direction == 'N':
            pass
        elif direction == 'L':  # pragma: no branch
            new_position -= 1
        # Make sure that the cursor doesn't run off the end of the tape.
        if new_position == -1:
            new_tape.insert(0, self.blank_symbol)
            new_position += 1
        if new_position == len(new_tape):
            new_tape.append(self.blank_symbol)
        return TMTape(
            new_tape,
            blank_symbol=self.blank_symbol,
            current_position=new_position
        )

    def copy(self):
        return TMTape(list(self.tape).copy(),
                      blank_symbol=self.blank_symbol,
                      current_position=self.current_position)

    def get_symbols_as_str(self):
        return "".join(self.tape)

    def __len__(self):
        """Return the number of symbols on the tape."""
        return len(self.tape)  # TODO: do we count the blank symbols?

    def __iter__(self):
        """Return an interator for the tape."""
        return iter(self.tape)

    def __repr__(self):
        """Return a string representation of the tape."""
        return '{}(\'{}\', {})'.format(
            self.__class__.__name__, ''.join(self.tape), self.current_position
        )


class DTM():
    """A deterministic Turing machine."""

    def __init__(self, *, states, input_symbols, tape_symbols,transitions, initial_state, blank_symbol,final_states):
        """Initialize a complete Turing machine."""
        self.states = states.copy()
        self.input_symbols = input_symbols.copy()
        self.tape_symbols = tape_symbols.copy()
        self.transitions = transitions.copy()
        self.initial_state = initial_state
        self.blank_symbol = blank_symbol
        self.final_states = final_states.copy()
        self.validate()

    def _validate_transition_state(self, transition_state):
        if transition_state not in self.states:
            raise exceptions.InvalidStateError('transition state is not valid ({})'.format(transition_state))

    def _validate_transition_symbols(self, state, paths):
        for tape_symbol in paths.keys():
            if tape_symbol not in self.tape_symbols:
                raise exceptions.InvalidSymbolError(
                    'transition symbol {} for state {} is not valid'.format(
                        tape_symbol, state))

    def _validate_transition_result_direction(self, result_direction):
        if result_direction not in ('L', 'N', 'R'):
            raise exceptions.InvalidDirectionError('result direction is not valid ({})'.format(result_direction))

    def _validate_transition_result(self, result):
        result_state, result_symbol, result_direction = result
        if result_state not in self.states:
            raise exceptions.InvalidStateError(
                'result state is not valid ({})'.format(result_state))
        if result_symbol not in self.tape_symbols:
            raise exceptions.InvalidSymbolError(
                'result symbol is not valid ({})'.format(result_symbol))
        self._validate_transition_result_direction(result_direction)

    def _validate_transition_results(self, paths):
        for result in paths.values():
            self._validate_transition_result(result)

    def _validate_transitions(self):
        for state, paths in self.transitions.items():
            self._validate_transition_state(state)
            self._validate_transition_symbols(state, paths)
            self._validate_transition_results(paths)

    def _validate_final_state_transitions(self):
        for final_state in self.final_states:
            if final_state in self.transitions:
                raise exceptions.FinalStateError(
                    'final state {} has transitions defined'.format(
                        final_state))

    def validate(self):
        """Return True if this DTM is internally consistent."""
        self._read_input_symbol_subset()
        self._validate_blank_symbol()
        self._validate_transitions()
        self._validate_initial_state()
        self._validate_initial_state_transitions()
        self._validate_nonfinal_initial_state()
        self._validate_final_states()
        self._validate_final_state_transitions()
        return True

    def _get_transition(self, state, tape_symbol):
        """Get the transiton tuple for the given state and tape symbol."""
        if (state in self.transitions and
                tape_symbol in self.transitions[state]):
            return self.transitions[state][tape_symbol]
        else:
            return None

    def _has_accepted(self, configuration):
        """Check whether the given config indicates accepted input."""
        return configuration.state in self.final_states

    def _get_next_configuration(self, old_config):
        """Advance to the next configuration."""
        transitions = {self._get_transition(
            old_config.state,
            old_config.tape.read_symbol()
        )}
        if None in transitions:
            transitions.remove(None)
        if len(transitions) == 0:
            raise exceptions.RejectionException(
                'The machine entered a non-final configuration for which no '
                'transition is defined ({}, {})'.format(
                    old_config.state, old_config.tape.read_symbol()))
        tape = old_config.tape
        (new_state, new_tape_symbol,
            direction) = transitions.pop()
        tape = tape.write_symbol(new_tape_symbol)
        tape = tape.move(direction)
        return TMConfiguration(new_state, tape)

    def read_input_stepwise(self, input_str):
        """
        Check if the given string is accepted by this Turing machine.
        Yield the current configuration of the machine at each step.
        """
        current_configuration = TMConfiguration(
            self.initial_state,
            TMTape(input_str, blank_symbol=self.blank_symbol)
        )
        yield current_configuration

        # The initial state cannot be a final state for a DTM, so the first
        # iteration is always guaranteed to run (as it should)
        while not self._has_accepted(current_configuration):
            current_configuration = self._get_next_configuration(
                current_configuration
            )
            yield current_configuration