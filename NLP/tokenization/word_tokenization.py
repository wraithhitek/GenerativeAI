import nltk
from nltk.tokenize import word_tokenize
# nltk.download('punkt') #punkt is a ml model which already learnt to tokenize sentences
# nltk.download('punkt_tab') #punkt_tab is just a lookup table which is conationg the rules to do the tokenization

text = "Hello, my dog is cute"
tokens = word_tokenize(text)
print(tokens)