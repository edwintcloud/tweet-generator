import sys, string, time


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


def get_histogram(words):
    '''Generates histogram from word list'''

    # create dictionary of unique words
    unique_words = {word: 0 for word in words}

    # count number of each word and update dictionary value
    for word in words:
        unique_words[word] += 1

    # sort dictionary in a list of tuples in decending order
    histogram = sorted(unique_words.items(), key=lambda i: i[1], reverse=True)

    # return histogram
    return histogram


def get_words(file_name):
    '''Opens file and returns list of words in file'''

    # open the file safely
    with open(file_name) as file:
        words = file.read().split()

    # return the file as a list of words
    return words


def normalize_words(words):
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


def unique_words(histogram):
    '''Returns number of unique words in histogram'''
    return len(histogram)


def total_words(histogram):
    '''Returns total number of words in histogram'''
    return sum(i[1] for i in histogram)


def frequency(word, histogram):
    '''Returns histogram value for specified word or 0 if word not found'''

    return dict(histogram).get(word, 0)


def write_to_file(histogram):
    '''Writes histogram to file in an easy to read format'''

    # open the file for writing or create a new one
    with open('histogram.txt', 'w+') as file:
        for i in histogram:
            file.write("%s%s\n" % ('{:<40}'.format(i[0]), i[1]))


def main(file_name):
    '''Main Entry point for program'''

    # get list of words in soure file
    words = get_words(file_name)

    # normalize list of words into actual words
    words[:] = normalize_words(words)

    # get histogram from list of words
    histogram = get_histogram(words)

    # return histogram
    return histogram


if __name__ == '__main__':

    # start the timer
    start_time = time.time()

    # run our program which requires a file name and word argument
    histogram = main(sys.argv[1])

    # print total number of words in source
    print("\nThere are %s%s%s words in this source." %
          (color.PURPLE, total_words(histogram), color.END))

    # get 10 most common words
    most_common_words = histogram[:10]

    # print 10 most common words
    print("\nThe ten most common words are:\n")
    for word in most_common_words:
        print("   %s%s%s appearing %s%s%s times." % (color.GREEN, '{:<10}'.format(word[0]),
                                                     color.END, color.RED, word[1], color.END))

    # print number of unique words
    print("\nThere are %s%s%s unique words in this source." % (color.CYAN,
                                                               unique_words(histogram), color.END))
    # print number of times given word appears in source
    print("\nThe word %s%s%s appears exactly %s%s%s time(s)." % (color.GREEN,
                                                                 sys.argv[2], color.END, color.RED, frequency(sys.argv[2], histogram), color.END))

    # print the time elapsed
    print("\n%sFinished in %s seconds%s\n" % (color.BLUE, "{0:.2f}"
                                              .format((time.time() - start_time)), color.END))

    # # Ask user to save result to a file
    to_file = input(
        "Would you like to save the sorted histogram to a file? (y/n): ")

    # If user entered 'y' then save the file
    if to_file == 'y':
        write_to_file(histogram)
