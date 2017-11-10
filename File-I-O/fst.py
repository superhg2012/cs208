"""
FST class defined with:
Defined formally as { Q, Sigma, Gamma, s, F, Delta }
states        - a list of strings which define the states of the fsa e.g ("s0", "s1", "s2")
alphabet in   - a list of the accepted characters for intput string e.g. {'a','b'}
alphabet out  - a list of the accepted characters for output string e.g. {'a','b'}
start_state   - a string contained in states list which the FSA will start at
final_states  - a list of states designated as final states
transitions   - a dictionary which determines how the current state changes based on the input and the output string
"""

class FST:

    def __init__(self, states, in_alphabet, out_alphabet, start_state, final_states, transitions):
        self.states   = states
        self.in_alph  = in_alphabet
        self.out_alph = out_alphabet
        self.start    = start_state
        self.final    = final_states
        self.trans    = transitions

    def transduce_string(self, input):
        current = self.start
        x = 0;
        while x < len(input):
            if not (input[x] in self.in_alph):
                return "EXCEPTION: " + input[x] + " not in input alphabet [" + ", ".join(self.in_alph) + "]"

            new_state = self.trans[current][input[x]][0]
            new_x     = self.trans[current][input[x]][1]
            for i in new_x:
                if not (i in self.out_alph):
                    return "EXCEPTION: " + i + " not in output alphabet [" + ", ".join(self.out_alph) + "]"

            input = input[:x] + new_x + input[x+1:]

            current = new_state
            if not (current in self.states):
                return "EXCEPTION: " + current + " not a state in this FST [" + ", ".join(self.states) + "]"

            x = x + len(new_x)

        if not (current in self.final):
            return "EXCEPTION: " + current + " not a final state in this FST [" + ", ".join(self.final) + "]"

        return input
