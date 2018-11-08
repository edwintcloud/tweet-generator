#!/usr/bin/env python3

from modules.tokenize import get_words
from modules.cleanup import clean
from modules.word_count import get_dictogram
from modules.sample import get_random_words
from modules.sentence import generate_sentence
from random import randint

def random_sentence(corpus, min_num_of_words=12, max_num_of_words=18):
    '''Generates random sentence of random length between min and max num of words'''
    num_of_words = randint(min_num_of_words, max_num_of_words)
    words = get_words(corpus)
    cleaned_words = clean(words)
    listogram = get_dictogram(cleaned_words)
    random_weighted_words = get_random_words(listogram, num_of_words)
    sentence = generate_sentence(random_weighted_words)
    return sentence

if __name__ == '__main__':
    import sys
    sentence = random_sentence(sys.argv[1], sys.argv[2], sys.argv[3])

    # print sentence
    print(sentence)