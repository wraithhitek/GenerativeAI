from sklearn.feature_extraction.text import CountVectorizer # feature_extrcation  is module and text is also a module and Count Vectorizer is a class

sentences=["love phone camera amazing camera quality amazing battery"] #cleaned text

vectorizer=CountVectorizer()
x=vectorizer.fit_transform(sentences) #fit means understand tramsfrom means it will convert it into number
print(x)
print(vectorizer.get_feature_names_out())
print(x.toarray())

