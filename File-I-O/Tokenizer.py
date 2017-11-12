"""
Read token_discussion.txt for information about changes to tokenizer function
"""

# tokenizer takes a string and returns a list of the sentences contained in that string.
def tokenizer_old(text):
	end_punctuation = ['.','!','?',':',';']
	sentence = ''
	sentences = []
	for c in text:
		if c in end_punctuation:
			sentence+=c
			sentences.append(sentence)
			sentence = ''
		else:
			sentence+=c
	return sentences

# my modified version of the tokenizer function: see token_discussion.txt for details
def tokenizer(text):
	end_punctuation  = ['. ','! ','? ',': ','; ']
	end_newline_punc = ['.\n','!\n','?\n',':\n',';\n']
	end_quotes_punc  = ['." ','!" ','?" ',':" ',';" ']
	end_qandn_punc   = ['.\"\n','!\"\n','?\"\n',':\"\n',';\"\n']
	month_abreves    = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
	sentence = ''
	sentences = []
	i = 0
	while i < len(text):
		# removing newline chars
		if text[i] == '\n':
			i +=1
		# catch for a period is following an inital of someones name
		elif text[i] in map(chr, range(65, 91)) and text[i+1] == '.':
			sentence += text[i:i+2]
			i +=2
		# catch for month abreviations
		elif text[i:i+4] in month_abreves:
			sentence += text[i:i+4]
			i +=4
		# catch for quotation followed by newline
		elif text[i:i+3] in end_qandn_punc:
			sentence += text[i:i+2]
			sentences.append(sentence)
			sentence = ''
			i +=3
		# catch for end of sentence followed by quote followed by space
		elif text[i:i+3] in end_quotes_punc:
		  	sentence += text[i:i+2]
		  	sentences.append(sentence)
		  	sentence = ''
		  	i +=3
		# catch for end of sentence followed by space
		elif text[i:i+2] in end_punctuation:
			sentence += text[i:i+2]
			sentences.append(sentence)
			sentence = ''
			i +=2
		# catch for end of sentences followed by newline
		elif text[i:i+2] in end_newline_punc:
			sentence += text[i]
			sentences.append(sentence)
			sentence = ''
			i +=2

		# all other characters
	  	else:
		 	sentence += text[i]
			i +=1
   	return sentences

# print_sentences takes a list of strings and prints them one at a time
def print_sentences(sentence_list):
   	i = 1
   	for s in sentence_list:
	  	print 'Sentence',i,':',s
	  	i+=1

# Demonstration: rewrite demo() so that it
# 1) opens the file tokenizertest.txt and reads it into a string,
# 2) sends that string to tokenizer,
# 3) sends the result of tokenizer to print_sentences, and
# 4) closes the file tokenizertest.txt

def demo():
	input_file = open('tokenizertest.txt', 'r')
   	input_string = input_file.read()
   	string_tokens = tokenizer(input_string)
   	print_sentences(string_tokens)
   	input_file.close()







if __name__=='__main__':
   demo()
