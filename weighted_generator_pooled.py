import sys, random
import word_frequency as wf
from multiprocessing import Pool


def main(file_name, num_of_words):
    '''Main entry point for program'''

    # get histogram from file using our word_frequency import
    histogram = wf.main(file_name)

    # shuffle histogram
    histogram[:] = random.sample(histogram, len(histogram))

    # split the work up based on num of words
    pool = Pool(processes=int(num_of_words))
    res = pool.map_async(random_words, chunks(histogram, int(num_of_words)))
    random_weighted_pools = res.get(timeout=1)

    print(random_weighted_pools)

    # return a random index from each random weighted pool
    return [i[random.randrange(len(i))] for i in random_weighted_pools]


def chunks(l, n):
    '''Yield successive n-sized chunks from l.'''

    for i in range(0, len(l), int(len(l)/n)):
        yield l[i:i + n]


def random_words(chunk):
    '''Iterable function that returns random words for a histogram chunk'''

    # create list of words from histogram chunk
    words = [i[0] for i in chunk]

     # create list of weights from histogram chunk
    total_words = wf.total_words(chunk)
    weights = [i[1]/total_words for i in chunk]

    # generate random words based on weights
    random_words = []
    while len(random_words) < int(sys.argv[2]):
        random_index = random.randrange(len(words))
        if random.random() < weights[random_index]:
            random_words.append(words[random_index])
    
    print(random_words)
    # return random words list
    return random_words


if __name__ == '__main__':

    # get random words
    random_words = main(sys.argv[1], sys.argv[2])

    # Capitalize first word
    random_words[0] = random_words[0].capitalize()

    # print out a sentence of the random words
    print(' '.join(random_words)+'.')
