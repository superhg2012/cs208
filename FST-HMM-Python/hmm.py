"""

"""

class HMM:

    def __init__(self, states, observations, start_probability, transition_probability, observation_probability):
        self.states     = states
        self.obs        = observations
        self.start_prob = start_probability
        self.trans_prob = transition_probability
        self.obs_prob   = observation_probability

    def get_state_sequence_prob(self, state_sequence):
        current_state = state_sequence[0]
        probability   = self.start_prob[current_state]

        for state in state_sequence[1:]:
            probability *= self.trans_prob[current_state][state]
            current_state = state

        return probability

    def viterbi(self, obs_sequence):
        # this dictionary holds highest probability to each state after som num of observations
        t1 = {}
        # this dictionary holds the temporary probs from one state to another before the max is taken and stored in t1
        t2 = {}
        # keeps track of path of highest probability to states based on observations
        path = {}
        for state in self.states:
            t1[state] = self.start_prob[state] * self.obs_prob[state][obs_sequence[0]]
            t2[state] = []
            path[state] = [] # key is the ending state

        for obs in obs_sequence[1:]:
            t3 = {} # another temporary dict for storing maxing until all are calculated
            for trans_s in self.states:
                for cur_s in self.states:
                    # storing probability to transition so trans_s from each cur_s
                    t2[trans_s].append(t1[cur_s] * self.obs_prob[trans_s][obs] * self.trans_prob[cur_s][trans_s])
                # storing the max in t3 becuase we don't want to change t1 yet
                t3[trans_s] = max(t2[trans_s])
                # backtracking to see which state have us that max
                path[trans_s].append(self.states[t2[trans_s].index(max(t2[trans_s]))])
                t2[trans_s] = []
            # updating t1 so it hold highest probability to each state so far
            t1 = t3

        # added for debugging to show maximal path/probability ending on a cold state is still correct
        # print t1
        # print path

        max_prob = 0
        path_max = ""
        # looping through final probs to each state to find max probability and path to that state
        for prob in t1:
            if t1[prob] > max_prob:
                path_max = prob
                max_prob = t1[prob]

        # if loop just to make output look nice if path is only one observation deep
        if path[path_max] != []:
            print "path of most likely probability: " + ", ".join (path[path_max]) + ", " + path_max
        else:
            print "path of most likely probability: " + path_max
        return max_prob
