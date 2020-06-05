from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True)
us = model['United_States']
print(us)
