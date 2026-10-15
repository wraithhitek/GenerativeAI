from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

sentences=["The cake was delicious and fresh and good cake .",
    "The bread was fresh and soft",
    "Fresh cake and bread every day"]

#BOW techique
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(sentences)
df=pd.DataFrame(x.toarray())
print("BOW:")
print(df)
print("\n")

#term frequency representation
df_tf=df.div(df.sum(axis=1),axis=0)
print("TF normalized")
print(vectorizer.get_feature_names_out())
print(df_tf)
