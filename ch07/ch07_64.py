from tqdm import tqdm
import pandas as pd
from gensim.models import KeyedVectors


def culcSim(row):
    global model
    return pd.Series(list(model.most_similar(positive=[row['v2'], row['v3']], negative=[row['v1']])[0]))

tqdm.pandas()
df = pd.read_csv('../data/questions-words.txt', sep=' ')
df = df.reset_index()
df.columns = ['v1', 'v2', 'v3', 'v4']
df.dropna(inplace=True)

model = KeyedVectors.load_word2vec_format('../data/GoogleNews-vectors-negative300.bin', binary=True)
df[['simWord', 'simScore']] = df.progress_apply(culcSim, axis=1)
df.to_csv('../data/ch07_64.txt', sep=' ', index=False, header=False)
