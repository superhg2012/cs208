"""
FSA class defined with:
Defined formally as { Q, Sigma, F, s, Delta }
states        - a list of strings which define the states of the fsa e.g ("s0", "s1", "s2")
alphabet      - a list of the accepted characters for transitions e.g. {'a','b'}
start_state   - a string contained in states list which the FSA will start at
accept_states - a list of states which will be used to check if FSA accepts or rejects a strings
transitions   - a dictionary which determines how the current state changes based on the input
"""

class FSA:

    def __init__(self, states, alphabet, accept_states, start_state, transitions):
        self.states  = states
        self.alph    = alphabet
        self.accept  = accept_states
        self.start   = start_state
        self.trans   = transitions

    # Check string takes a string input to iterate through and returns boolean
    def accept_string(self, input):
        current = self.start
        for x in input:
            if not (x in self.alph):
                print "Exception: " + x + " not in alphabet [" + ", ".join(self.alph) + "]"
                return False
            current = self.trans[current][x]
            if not (current in self.states):
                print "Exception: " + current + " not a state in this FSA [" + ", ".join(self.states) + "]"
                return False

        return current in self.accept
