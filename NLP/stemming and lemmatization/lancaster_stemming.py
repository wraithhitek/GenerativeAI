from nltk.stem import LancasterStemmer
lancaster= LancasterStemmer()

words=['running','runner','studies','happiness','organization','intention','easily','fairly']

print("\n Lancaster Stemmer Results: ")
for w in words:
    print(w, "->", lancaster.stem(w))
    