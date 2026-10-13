import nltk
from nltk.stem import PorterStemmer,LancasterStemmer,SnowballStemmer

porter=PorterStemmer()
lancaster=LancasterStemmer()
snow=SnowballStemmer("english")

words=['running','runner','studies','happiness','organization','intention','easily','fairly']

print("Original words:",words)
print("\n Porter Stem Results: ")
for w in words:
    print(w,"->",porter.stem(w))

print("\n Lancaster Stem result:")
for w in words:
    print(w,"->", lancaster.stem(w))

print("\n Snowball Stem result: ")
for w in words:
    print(w,"->",snow.stem(w))
