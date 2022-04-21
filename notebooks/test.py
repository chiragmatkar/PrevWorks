import numpy as np
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
from scipy.spatial.distance import cosine
import re

fname = 'word2vec.kv'
model = KeyedVectors.load(fname, mmap='r')
stop_words = set(stopwords.words('english'))
#wordVectors = model.wv

def transform(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    text = text.split()
    vecs = []
    for word in text:
        if word in model and word not in stop_words:
            vecs.append(model[word])
    print(vecs)
    mean_vec = np.mean(np.array(vecs), axis=0)
    return mean_vec

"""
class_vec: vector representation of the text for the class
industries: array of the vectors for all the industries

returns: index in array of the value
        
"""
def find_similar(class_vec, industries):
    distances = distance.cdist([class_vec], industries, "cosine")[0]
    min_index = np.argmin(distances)
    return min_index

    
