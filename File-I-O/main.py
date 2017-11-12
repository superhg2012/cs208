from fst import FST

##### Creating an FST for minidictionary.txt #####

mini_dict = open('minidictionary.txt', 'r')
fst_states = []
# source for generating list of chars http://snipplr.com/view/5058/
fst_in_alph  = map(chr, range(97, 123))
fst_out_alph = map(chr, range(65, 91))
fst_out_alph.append(" ")
fst_start  = "start"
fst_final  = []
fst_trans  = {"start" : {}}

char_list = []
arp_list  = []
# splitting input into list of words and list of arphabet characters
for line in mini_dict:
    char_list.append(line.split()[0])
    arp_list.append(line.split()[1:])

# closing input file
mini_dict.close()

for i in range(0, len(char_list)):
    if not char_list[i][0] in fst_trans:
        # adding new states to fst_states
        fst_states.append(char_list[i][0])
        # adding initial transitions from start state
        fst_trans[char_list[i][0]] = {}
        fst_trans["start"][char_list[i][0]] = [char_list[i][:1], arp_list[i][0]+" "]

for i in range(0, len(char_list)):
    for j in range(1, len(char_list[i])):
        # adding new states to fst_states
        fst_states.append(char_list[i][:j+1])
        # adding state transitions, where state names are string of chars in the color
        # so far so the 3rd state on the way to blue is named 'blu'
        # example in dictionary: 'ru': {'b': ['rub', 'B ']}
        fst_trans[char_list[i][:j+1]] = {}
        fst_trans[char_list[i][:j]][char_list[i][j]] = [char_list[i][:j+1]]
        # if/else accounting for silent letters at end of word
        if j < len(arp_list[i]):
            fst_trans[char_list[i][:j]][char_list[i][j]].append(arp_list[i][j]+" ")
        else:
            fst_trans[char_list[i][:j]][char_list[i][j]].append("")

# Our final states are all of our input words
fst_final = char_list
# Declaring our fst
test_fst = FST(fst_states, fst_in_alph, fst_out_alph, fst_start, fst_final, fst_trans)

# Calling transduce on each color in our input
for word in char_list:
    print test_fst.transduce_string(word)
