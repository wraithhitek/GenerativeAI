# Removing the punctuations using string module and regex both techniques
# using string module
import string
text="Hello!!! I have 2 cats"
cleaned=''.join([char.lower() for char in text if char not in string.punctuation])
print(cleaned)

# using regex
import re
text="Hello!!! I have 2 cats"
cleaned=re.sub(r'[^a-zA-Z0-9\s]','',text)
print(cleaned)


