from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st
import pandas as pd

st.title("BOW Representation")

sentences=st.text_area("Enter 5 Sentences(one per line): ").split("\n")

if st.button("Generate BOW:"):
    vectorizer=CountVectorizer()
    x=vectorizer.fit_transform(sentences)
    df=pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names_out())
    st.write(df)
    