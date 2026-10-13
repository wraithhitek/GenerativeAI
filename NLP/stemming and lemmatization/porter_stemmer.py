from nltk.stem import PorterStemmer # -> nltk is library, stem is module, porterstemer is a class
porter = PorterStemmer()
words = ['running', 'runner', 'studies', 'happiness', 'organization', 'intention', 'easily']
print("\n Porter stemmer results:")
for w in words:
 print(w, "->", porter.stem(w)) #-> stem() is method
