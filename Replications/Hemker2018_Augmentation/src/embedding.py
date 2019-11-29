import pandas as pd
import numpy as np
from gensim.models.keyedvectors import KeyedVectors


def get_corpus(corpus_, path=''):
    """Loads pre-trained word2vec model from src/ directory and
    returns a gensim word2vec object"""
    if corpus_ == 'google':
        return KeyedVectors.load_word2vec_format(path + 'GoogleNews-vectors-negative300.bin',
                                                 binary=True)
    if corpus_=='glove':
        return KeyedVectors.load_word2vec_format(path + 'glove.42B.300d.txt',
                                                 binary=False)
    if corpus_=='glove25':
        return KeyedVectors.load_word2vec_format(path + 'glove.twitter.27B.25d.txt',
                                                 binary=False)
    if corpus_=='fasttext':
        return KeyedVectors.load_word2vec_format(path + 'crawl-300d-2M.vec',
                                                 binary=False,
                                                 encoding='UTF-8')




if __name__ == '__main__':
    model = get_corpus('google')