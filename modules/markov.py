#!/usr/bin/env python3

from dictogram import Dictogram


def generate_dictograms(words):
    '''Takes a list of words and generates a dictionary of dictograms of each word directly following each word'''

    # create a dictionary to hold our dictograms
    dictograms = {}

    # First we must iterate through the words list, exluding the last item
    for index in range(len(words) - 1):
        # check if the word is not in dictionary of word histograms already
        if words[index] not in dictograms:
            # create new dictogram for the word in dictionary of dictograms
            dictograms[words[index]] = Dictogram()
        # add count of word following word to dictogram
        dictograms[words[index]].add_count(words[index+1])
    
    # return dictograms dictionary
    return dictograms

# def random_walk():

if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    dictograms = generate_dictograms(cleaned_words)

    # print results
    print(dictograms)
