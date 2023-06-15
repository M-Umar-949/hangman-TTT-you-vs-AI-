# Download Wordbank from nltk. you can create your own words list

# import nltk
# nltk.download('wordnet')

from nltk.corpus import wordnet

word_bank = wordnet.words()

words = list(word_bank)

print (words)