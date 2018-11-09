#!/usr/bin/env python3

import sys

def get_words(file_name):
    '''Opens file and returns list of words in file'''

    # set path depending on where script is run from
    if 'modules' in sys.path[0]:
        path = 'corpuses/'
    else:
        path = 'modules/corpuses/'

    # open the file safely
    with open(path + file_name + '.txt') as file:
        words = file.read().split()

    # return the file as a list of words
    return words

if __name__ == '__main__':
    import sys
    words = get_words(sys.argv[1])

    # print words in text
    for word in words: 
        print(word)