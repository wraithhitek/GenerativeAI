import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')

words = ['i', 'absolutely', 'love', 'this', 'mobile', 'phone', 'because', 'it', 'is', 'very', 'fast.']
# print(words)
filtered=[word for word in words if word not in stopwords.words('english')]
print(filtered)

st_words=stopwords.words('german')
print(st_words)
print(len(st_words))