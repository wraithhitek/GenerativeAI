# BPE 
from transformers import GPT2Tokenizer, BertTokenizer

text="NLP preprocessing transformers unstructured textual data effectively"

# gpt2_tok=GPT2Tokenizer.from_pretrained("gpt2")
# gpt2_tokens=gpt2_tok.tokenize(text)
# print('\n GPT-2 Tokens:',gpt2_tokens)
# print('GPT Ids:', gpt2_tok.encode(text))
# print('vocab sizes of gpt2:',gpt2_tok.vocab_size)

# Word piece
bert_tok=BertTokenizer.from_pretrained("bert-base-uncased")
bert_tokens=bert_tok.tokenize(text)
print('Bert Tokens:', bert_tokens)
print('BERT ids:', bert_tok.encode(text))
print('Bert Vocab size:', bert_tok.vocab_size)