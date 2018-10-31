import sys, random
import word_frequency as wf


def main(file_name, num_of_words):

    # get histogram from file using our word_frequency import
    hg = wf.histogram(file_name)

    # get our total number of words in source
    total_words = sum(hg.values())

    # create empty list to hold our random words
    random_words = []

    # do random weighted generation until we have num_of_words words
    while len(random_words) < int(num_of_words):

        # pick a random word
        random_word = random.choice(list(hg))

        # generate probability percentage based on word frequency
        word_probability = hg[random_word] / total_words

        # generate random probability percentage based on total words in source
        random_probability = random.random() * total_words

        # if the word probability is greater than the random probability,
        # add the word to random words list
        if word_probability > random_probability:
            random_words.append(random_word)

    print(random_words)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
