import bisect, sys, itertools, random


def main(file_name):

    # open histogram file
    with open(file_name) as words:
        sample = words.read().split()
        sample = [(sample[i], sample[i+1]) for i in range(0, len(sample)-1, 2)]

    

if __name__ == '__main__':
    main(sys.argv[1])
