#!/usr/bin/env python3

import random

def generate_sentence(words):
    '''Takes a list of random weighted words and generates a sentence'''
     # Capitalize first word
    words[0] = words[0].capitalize()

    # save sentence as a variable to return later
    sentence = ' '.join(words)+'.'

    # return random words
    return sentence

if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    from word_count import get_dictogram
    from sample import get_random_words
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    listogram = get_dictogram(cleaned_words)
    random_weighted_words = get_random_words(listogram, sys.argv[2])
    sentence = generate_sentence(random_weighted_words)

    # print sentence
    print(sentence)