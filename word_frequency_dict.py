import sys
import collections
import string
import time


class color:
    '''Color class to hold ASCI color codes as accessible properties'''

    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


def histogram(source_text):
    '''Generates histogram from file and returns result'''

    # translation table we will use to remove punctuation and numbers
    t_table = str.maketrans('', '', '''!"#$%&()*+,./:;<=>?@[\]^_`{|}~`1234567890''')

    # open the file safely
    with open(source_text) as words:
        sample = words.read().split()

        # trim any whitespaces
        sample[:] = [i.strip(' ') for i in sample]

        # split dashed words into seperate words
        sample[:] = [i for e in sample for i in e.split('--')]

        # remove Roman Numerals, Initials, Abbreviations, and single
        # letters that aren't words - wow this is gonna be ugly
        alphabet = [i+'.' for i in string.ascii_uppercase]
        single_letter_words = ['a', 'i']
        abbreviations3 = ['st.', 'dr.', 'mr.']
        abbreviations4 = ['mrs.', 'sq.,', 'esq.']
        sample[:] = [i for i in sample if i[-2:] not in alphabet and
                     i[-3:].lower() not in abbreviations3
                     and i[-4:].lower() not in abbreviations4
                     and not (len(i) == 1 and i.lower() not in
                     single_letter_words)]

        # remove numbers and punctuation except ' and - and make all lowercase
        sample[:] = [i.translate(t_table).lower() for i in sample]

        # trim trailing and leading puncuation
        sample[:] = [i.lstrip("'").rstrip("'") for i in sample]

    # create our histogram
    hg = {sample[i]: 0 for i in range(len(sample)-1)}
    for i in sample:
        hg[i] += 1
    hg = sorted(hg.items(), key=lambda kv: kv[1], reverse=True)

    # print total number of words in source
    print("\nThere are %s%s%s words in this source." % (color.PURPLE, len(sample), color.END))

    # print 10 most common words
    print("\nThe ten most common words are:\n")
    for i in range(10 if len(hg) >= 10 else len(hg)):
        print("   %s%s%s appearing %s%s%s times." % (color.GREEN, '{:<10}'.format(hg[i][1]),
              color.END, color.RED, hg[i][0], color.END))

    return dict(hg)


def unique_words(histogram):
    '''Returns number of unique words in histogram'''
    return len(histogram)


def frequency(word, histogram):
    '''Returns histogram value for specified word or 0 if word not found'''

    return 0 if word not in histogram else histogram[word]


def write_to_file(histogram):
    '''Writes histogram to file in an easy to read format'''

    # open the file for writing or create a new one
    with open('histogram.txt', 'w+') as file:
        for i in histogram:
            file.write("%s%s\n" % ('{:<40}'.format(i), histogram[i]))


def main(source_text, word):
    '''Main Entry point for program'''

    # generate histogram
    result = histogram(source_text)

    # print result
    print("\nThere are %s%s%s unique words in this source." % (color.CYAN,
          unique_words(result), color.END))
    print("\nThe word %s%s%s appears exactly %s%s%s time(s)." % (color.GREEN,
          word, color.END, color.RED, frequency(word, result), color.END))

    # return the results
    return result


if __name__ == '__main__':

    # start the timer
    start_time = time.time()

    # run our program which requires a file name and word argument
    hg = main(sys.argv[1], sys.argv[2])

    # print the time elapsed
    print("\n%sFinished in %s seconds%s\n" % (color.BLUE, "{0:.2f}"
          .format((time.time()-start_time)), color.END))

    # # Ask user to save result to a file
    to_file = input("Would you like to save the sorted histogram to a file? (y/n): ")

    # If user entered 'y' then save the file
    if to_file == 'y':
        write_to_file(hg)
