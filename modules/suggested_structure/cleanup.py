#!/usr/bin/env python3

import string
import sys

def main(words):
    '''Normalizes word list into actual words'''

    # translation table we will use to remove punctuation and numbers
    translation_table = str.maketrans(
        '', '', '''!"#$%&()*+,./:;<=>?@[\]^_`{|}~`1234567890''')

    # split dashed words into seperate words and remove all whitespace
    words[:] = [i.replace(' ', '') for e in words for i in e.split('--')]

    # remove Roman Numerals, Initials, Abbreviations, and single
    # letters that aren't words - wow this is gonna be ugly
    alphabet = [i + '.' for i in string.ascii_uppercase]
    single_letter_words = ['a', 'i']
    abbreviations3 = ['st.', 'dr.', 'mr.']
    abbreviations4 = ['mrs.', 'sq.,', 'esq.']
    words[:] = [i for i in words if i[-2:] not in alphabet and
                i[-3:].lower() not in abbreviations3 and
                i[-4:].lower() not in abbreviations4 and
                not (len(i) == 1 and i.lower() not in
                         single_letter_words)]

    # remove numbers and punctuation and make all lowercase
    words[:] = [i.translate(translation_table).lower().lstrip(
        "'").rstrip("'") for i in words]

    # return normalized word list
    return words

if __name__ == '__main__':
    main(sys.argv[1])