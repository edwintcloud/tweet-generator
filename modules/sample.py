#!/usr/bin/env python3

import random

def get_random_word(gram):
    '''Takes a histogram and generates a single random word based on weights'''

    # get type of gram (dictogram or listogram)
    histogram_type = str(type(gram).__name__ )

    if(histogram_type == "Listogram"):
        histogram = gram
    elif(histogram_type == "Dictogram"):
        histogram = [(key, value) for key, value in gram.items()]
    else:
        return

    # get total number of words in source
    total_words = gram.tokens

    # create list of words and counts
    words, counts = zip(*histogram)

    # create list of weights from counts
    weights = [count/total_words for count in counts]

    # generate a random word based on weights
    random_word = ''
    while random_word == '':
        random_index = random.randrange(len(words))
        if random.random() < weights[random_index]:
            random_word = words[random_index]

    # return random word
    return random_word

if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    from dictogram import Dictogram
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    listogram = Dictogram(cleaned_words)
    random_weighted_word = get_random_word(listogram)

    # print random weighted word
    print(random_weighted_word)