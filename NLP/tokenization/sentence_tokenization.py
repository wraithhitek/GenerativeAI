#method 1
# import nltk
# from nltk.tokenize import sent_tokenize 
# # nltk.download('punkt') #punkt is a ml model which already learnt to tokenize sentences
# # nltk.download('punkt_tab') #punkt_tab is just a lookup table which is conationg the rules to do the tokenization

# text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."""
# sentences = sent_tokenize(text)
# print(sentences)

#method 2 for large amt of data(realtime)
import spacy
nlp=spacy.load("en_core_web_sm") #en_core_web_sm is a pretrained ml model( en: english , core: features, web: webistes, sm: small) 
#nlp is a model obj
doc=nlp("""Wow!! 🤩 I bought this smartphone for ₹29,999, and it's amazing! 📱 The battery lasts only 6 hours. 😕Thanks @MobileHub! Visit https://www.mobilehub.com. I'd definitely buy again! #HappyCustomer""")
tokens=[token.text for token in doc]
print(tokens )
