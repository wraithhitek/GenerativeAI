# Task
# Create a python program that:
# 1. Takes a list of 5 product reviews from the user, generates a bow matrix, prints both the vocabulary and the matrix
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import streamlit as st

st.title("Bag Of Words")
st.text_area("Enter sentences(one per line)").split("\n)
if st.button("Generate BOW"):
  vectorizer=CountVectorizer()
  x=vectorizer.fit_transform(sentences)
  df=pd.DataFrame(x.toarray(),columns=vectorizer.get_feature_names_out())
  st.write(df)
