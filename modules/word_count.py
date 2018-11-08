#!/usr/bin/env python3

from modules.dictogram import Dictogram
from modules.listogram import Listogram

def get_listogram(words):
    '''Generates Listogram from word list'''

    listogram = Listogram(words)

    # return listogram
    return listogram

def get_dictogram(words):
    '''Generates Dictogram from word list'''

    dictogram = Dictogram(words)

    # return dictogram
    return dictogram


if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    listogram = get_listogram(cleaned_words)

    # print listogram
    print(listogram)