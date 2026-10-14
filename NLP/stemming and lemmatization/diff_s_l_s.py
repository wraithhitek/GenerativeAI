import streamlit as st
import nltk
from nltk.stem import PorterStemmer,LancasterStemmer,SnowballStemmer,WordNetLemmatizer
from nltk.corpus import wordnet
import spacy

# nltk.download('wordnet')
# nltk.download('omw-1.4')

porter=PorterStemmer()
lancaster=LancasterStemmer()
snowball=SnowballStemmer("english")
lemmatizer=WordNetLemmatizer()
nlp=spacy.load("en_core_web_sm")

st.title("Stemming vs Lemmatization")

text=st.text_input("Enter a sentence or list of words: ")
if st.button("Process"):
    words=nltk.word_tokenize(text)

    st.markdown('### Result: ')
    st.markdown("|word| Porter Stem| Lancaster Stem| Snowball Stem| Lemma (NLTK)| Lemma (spacy)")
    st.markdown("|-------|----------|------------|------------|-----------|----------|-----|")
    for word in words:
        doc=nlp(word)
        spacy_lemma=doc[0].lemma_
        row=f"|{word}|{porter.stem(word)}|{lancaster.stem(word)}|{snowball.stem(word)}|{lemmatizer.lemmatize(word)}|{spacy_lemma}|"
        st.markdown(row)