
##### creating file objects for input(test.txt) and output(morgan.txt) #####
input_file = open('test.txt', 'r')
output = open('morgan.txt', 'w')

##### Find number of characters in file #####
num_chars = len(input_file.read())
input_file.seek(0)
##### Find # of lines in file and # of words per line #####
line_words = []
num_lines = 0
for line in input_file:
    line_words.append(len(line.split()))
    num_lines += 1

##### Writing results to morgan.txt #####
output.write("This file has " + str(num_chars) + " characters.\n")
output.write("This file has " + str(num_lines) + " lines.\n")
output.write("Line 0 has " + str(line_words[0]) + " words.\n")
output.write("Line 1 has " + str(line_words[1]) + " words.\n")
output.write("Line 2 has " + str(line_words[2]) + " words.\n")
output.write("Line 3 has " + str(line_words[3]) + " words.\n")
output.write("Line 4 has " + str(line_words[4]) + " words.\n")
