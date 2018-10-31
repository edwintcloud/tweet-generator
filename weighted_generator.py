import sys, random
import word_frequency as wf


def main(file_name, num_of_words):
    '''Main entry point for program'''

    # get histogram from file using our word_frequency import
    histogram = wf.main(file_name)

    # create list of words from histogram
    words = [i[0] for i in histogram]

    # create list of weights from histogram
    weights = [i[1]/wf.total_words(histogram) for i in histogram]

    # generate random words based on weights
    random_words = random.choices(words, weights, k=int(num_of_words))

    # return random words
    return random_words


if __name__ == '__main__':

    # get random words
    random_words = main(sys.argv[1], sys.argv[2])

    # Capitalize first word
    random_words[0] = random_words[0].capitalize()

    # print out a sentence of the random words
    print(' '.join(random_words)+'.')
