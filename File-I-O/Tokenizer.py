# tokenizer takes a string and returns a list of the sentences contained in that string.
def tokenizer(text):
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

# print_sentences takes a list of strings and prints them one at a time   
def print_sentences(sentence_list):
   i = 1
   for s in sentence_list:
      print 'Sentence',i,':',s
      i+=1

# Demonstration: rewrite demo() so that it 1) opens the file tokenizertest.txt and reads it into a string, 2) sends that string to tokenizer, 3) sends the result of tokenizer to print_sentences, and 4) closes the file tokenizertest.txt

def demo():
   print 'This demo currently does nothing.'








if __name__=='__main__':
   demo()


