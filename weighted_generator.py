import sys
import random
import word_frequency as wf
from multiprocessing import Pool


def get_random_words(histogram, n):
    '''Takes a histogram and generates n random words based on weights'''

    # get total number of words in source
    total_words = wf.total_words(histogram)

    # create list of words
    words = [entry[0] for entry in histogram]

    # create list of weights
    weights = [entry[1]/total_words for entry in histogram]

    # generate random words based on weights
    random_words = []
    while len(random_words) < int(n):
        random_index = random.randrange(len(words))
        if random.random() < weights[random_index]:
            random_words.append(words[random_index])

    # alternative implementation -- this is slower
    # random_words = []
    # for _ in range(int(n)):
    #     accumulator = 0
    #     random_sum = random.randrange(total_words)
    #     for i in range(len(words)):
    #         accumulator += weights[i]
    #         if accumulator > random_sum:
    #             random_words.append(words[i])

    # return random words
    return random_words


def generate_sentence(file_name, num_of_words):
    '''Generates sentence'''
    # get histogram from file using our word_frequency import
    histogram = wf.main(file_name)

    # get random words
    random_words = get_random_words(histogram, num_of_words)

    # Capitalize first word
    random_words[0] = random_words[0].capitalize()

    # save sentence as a variable to return later
    sentence = ' '.join(random_words)+'.'

    return sentence

def main(file_name, num_of_words):
    '''Prints results of get_random_words'''
   # generate sentence
    sentence = generate_sentence(file_name, num_of_words)

    # print out a sentence of the random words
    print(sentence)

    # # create histogram of random words results
    # random_words_histogram = wf.get_histogram(random_words)
    
    # # print out random words histogram results
    # for i in random_words_histogram:
    #     print(i)

    # return sentence
    return sentence


if __name__ == '__main__':

    # get random words and print results
    main(sys.argv[1], sys.argv[2])
