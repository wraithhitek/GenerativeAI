# Before running this prgram we have to download the en_core_web_sm model
# To download    python -m spacy download en_core_web_sm

import spacy
nlp=spacy.load("en_core_web_sm")

doc = nlp("""Wow!! 🤩 I bought this smartphone for ₹29,999, and it's amazing! 📱 The battery lasts only 6 hours. 😕Thanks @MobileHub! Visit https://www.mobilehub.com. I'd definitely buy again! #HappyCustomer""")
# print(doc)
tokens=[token.text for token in doc.sents]
print(tokens)

