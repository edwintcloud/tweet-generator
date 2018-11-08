#!/usr/bin/env python3

import random

def get_random_words(gram, n):
    '''Takes a histogram and generates n random words based on weights'''

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

    # generate random words based on weights
    random_words = []
    while len(random_words) < int(n):
        random_index = random.randrange(len(words))
        if random.random() < weights[random_index]:
            random_words.append(words[random_index])

    # return random words
    return random_words

if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    from word_count import get_dictogram
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    listogram = get_dictogram(cleaned_words)
    random_weighted_words = get_random_words(listogram, sys.argv[2])

    # print random weighted words
    print(random_weighted_words)