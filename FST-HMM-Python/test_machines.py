"""

Test file for FSA, FST and HMM classes

"""
from fsa import FSA
from fst import FST
from hmm import HMM

def fsa_test(test_string):
    # Defining FSA which accepts strings with even number of a's and b's
    fsa_states = ["q0", "q1", "q2", "q3"]
    fsa_alph   = ["a", "b"]
    fsa_start  = "q0"
    fsa_final  = ["q0"]
    fsa_trans  = {
        "q0": {
            "a" : "q2",
            "b" : "q1"
        },
        "q1": {
            "a" : "q3",
            "b" : "q0"
        },
        "q2": {
            "a" : "q0",
            "b" : "q3"
        },
        "q3": {
            "a" : "q1",
            "b" : "q2"
        },
    }

    test_fsa = FSA(fsa_states, fsa_alph, fsa_final, fsa_start, fsa_trans)

    if (test_fsa.accept_string(test_string)):
        print "Yay! this FSA does accept the string  : " + test_string
    else:
        print "NO! this FSA doesnt accept the string : " + test_string

def fst_test(test_string):
    # print "\nThis FST replaces the first 'a' in a string with an 'ba'"
    fst_states = ["q0", "q1"]
    fst_in_alph   = ["a", "b"]
    fst_out_alph = ["a", "b"]
    fst_start  = "q0"
    fst_final  = ["q0", "q1"]
    fst_trans  = {
        "q0": {
            "a" : ["q1", "ba"],
            "b" : ["q0", "b"]
        },
        "q1": {
            "a" : ["q1", "a"],
            "b" : ["q1", "b"]
        },
    }

    test_fst = FST(fst_states, fst_in_alph, fst_out_alph, fst_start, fst_final, fst_trans)

    print test_string + " : " + test_fst.transduce_string(test_string)

def fst_test2(test_string):
    # print "\nThis FST removes all b's from string\n"
    fst_states = ["q0"]
    fst_in_alph   = ["a", "b"]
    fst_out_alph = ["a", "b"]
    fst_start  = "q0"
    fst_final  = ["q0"]
    fst_trans  = {
        "q0": {
            "a" : ["q0", "a"],
            "b" : ["q0", ""]
        },
    }

    test_fst = FST(fst_states, fst_in_alph, fst_out_alph, fst_start, fst_final, fst_trans)

    print test_string + " : " + test_fst.transduce_string(test_string)

def hmm_test_prob(state_list):
    # hmm from class with icecream cones and hot and cold
    hmm_states = ["hot", "cold"]
    hmm_observations = ["1", "2", "3"]
    hmm_start_prob = {"hot" : .8, "cold" : .2}
    hmm_trans_prob = {
        "hot"  : {"hot" : .7, "cold" : .3},
        "cold" : {"hot" : .4, "cold" : .6}
    }
    hmm_obs_prob = {
        "hot"  : {"1" : .2, "2" : .4, "3" : .4},
        "cold" : {"1" : .5, "2" : .4, "3" : .1}
    }

    test_hmm = HMM(hmm_states, hmm_observations, hmm_start_prob, hmm_trans_prob, hmm_obs_prob)

    print ", ".join(state_list) + ": probability = " + str(test_hmm.get_state_sequence_prob(state_list))

def hmm_test_virterbi(observations):
    # hmm from class with icecream cones and hot and cold
    hmm_states = ["hot", "cold"]
    hmm_observations = ["1", "2", "3"]
    hmm_start_prob = {"hot" : .8, "cold" : .2}
    hmm_trans_prob = {
        "hot"  : {"hot" : .7, "cold" : .3},
        "cold" : {"hot" : .4, "cold" : .6}
    }
    hmm_obs_prob = {
        "hot"  : {"1" : .2, "2" : .4, "3" : .4},
        "cold" : {"1" : .5, "2" : .4, "3" : .1}
    }

    test_hmm = HMM(hmm_states, hmm_observations, hmm_start_prob, hmm_trans_prob, hmm_obs_prob)

    print test_hmm.viterbi(observations);

########## Helper functions to call test ##########

def do_fsa_test():
    print "\n******** FSA Tests below ********\n"

    print "\nThis FSA accepts strings with an even number of a's and b's\n"
    fsa_test("")
    fsa_test("a")
    fsa_test("b")
    fsa_test("aa")
    fsa_test("bb")
    fsa_test("aaa")
    fsa_test("aaaa")
    fsa_test("abba")
    fsa_test("bbbb")
    fsa_test("bab")
    fsa_test("bbaaaabb")
    fsa_test("abca")

def do_fst_test():
    print "\n******** FST Tests below ********\n"

    print "\nThis FST replaces the first 'a' in a string with an 'ba'"
    fst_test("")
    fst_test("a")
    fst_test("b")
    fst_test("aa")
    fst_test("bb")
    fst_test("aaa")
    fst_test("aaaa")
    fst_test("abba")
    fst_test("bbbb")
    fst_test("bab")
    fst_test("bbaaaabb")
    fst_test("abca")

    print "\nThis FST removes all b's from string\n"
    fst_test2("")
    fst_test2("a")
    fst_test2("b")
    fst_test2("aa")
    fst_test2("bb")
    fst_test2("aaa")
    fst_test2("aaaa")
    fst_test2("abba")
    fst_test2("bbbb")
    fst_test2("bab")
    fst_test2("bbaaaabb")
    fst_test2("abca")

def do_hmm_test():
    print "\n******** HMM Tests below ********\n"

    print "\nTests for state squence probability\n"
    hmm_test_prob(["hot"])
    hmm_test_prob(["cold"])
    hmm_test_prob(["hot", "cold"])
    hmm_test_prob(["cold", "hot"])
    hmm_test_prob(["hot", "hot", "hot"])
    hmm_test_prob(["cold", "cold", "cold"])
    hmm_test_prob(["hot", "cold", "hot"])
    hmm_test_prob(["hot", "hot", "cold"])

    print "\nTests for Virterbi Algorithm\n"
    hmm_test_virterbi(["1", "2", "3"])
    hmm_test_virterbi(["3", "1", "3"])
    hmm_test_virterbi(["3"])
    hmm_test_virterbi(["1"])
    hmm_test_virterbi(["2", "3"])


# Code to call Tests
do_fsa_test()
do_fst_test()
do_hmm_test()
