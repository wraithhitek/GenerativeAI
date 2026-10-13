from nltk.stem import SnowballStemmer
snow= SnowballStemmer("english")

words=['running','runner','studies','happiness','organization','intention','easily','fairly']

print("\n Snowball Stemmer Results: ")
for w in words:
    print(w,"->", snow.stem(w))