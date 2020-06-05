import numpy as np
from gensim.models import KeyedVectors

def conSim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

model = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True)
us1 = model['United_States']
us2 = model['U.S.']
print(conSim(us1, us2))
