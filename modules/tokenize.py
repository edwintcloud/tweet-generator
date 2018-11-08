#!/usr/bin/env python3

def get_words(file_name):
    '''Opens file and returns list of words in file'''

    # open the file safely
    with open(file_name) as file:
        words = file.read().split()

    # return the file as a list of words
    return words

if __name__ == '__main__':
    import sys
    words = get_words(sys.argv[1])

    # print words in text
    for word in words: 
        print(word)