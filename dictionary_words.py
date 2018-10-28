from random import randrange
import sys
import time


def main():
    with open('words_alpha.txt') as words:
        sample = words.read().split()

    for i in range(0, int(sys.argv[1])):
        print(sample[randrange(len(sample))])


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("generated in %s seconds" % (time.time()-start_time))
