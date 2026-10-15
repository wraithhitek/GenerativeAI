from sklearn.feature_extraction.text import TfidfVectorizer

sentences=["The phone is good",
    "The camera is good",
    "The battery is good",
    "The charger is good"]

vectorizer=TfidfVectorizer()

tfid_matrix=vectorizer.fit_transform(sentences)

print("TF_IDF values: ")
print(tfidf_matrix) # sparse matrix

print(vectorizer.get_feature_names_out())

print("\n TF+IDF values in Matrix form: ")
print(tfidf_matrix.toarray())

#---------------------------------------------------------------------------
print("\n idf Values: ")
for ele1, ele2 in zip(vectorizer.get_feature_names_out(), vetorizer.idf_):
    print(ele1,':',ele2) #idf value for each vocabulary

print("\n Vocablary Indexes: ")
print(vectorizer.vocabulary_) # to get the index if each vicabulary

