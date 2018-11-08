from random import randrange
import sys, time


def main():
    '''Main entry point for program'''

    # Open the file safely
    with open('words_alpha.txt') as words:
        sample = words.read().split()

    # Create an empty list
    result = []

    # Generate random words and append to result list
    for i in range(0, int(sys.argv[1])):
        result.append(sample[randrange(len(sample))])

    # Print result
    print(" ".join(result))

    # Returns result
    return result


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Finished in %s seconds" % "{0:.2f}".format(time.time()-start_time))
