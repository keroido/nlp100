import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans


country = pd.read_table('../data/countries.tsv')
country = country['Short name'].values

model = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True)

countryVec = []
countryName = []

for c in country:
    if c in model.vocab:
        countryVec.append(model[c])
        countryName.append(c)


X = np.array(countryVec)
km = KMeans(n_clusters=5, random_state=0)
y_km = km.fit_predict(X)
print(y_km)

