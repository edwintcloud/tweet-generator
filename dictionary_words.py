import random
import sys

def main():
    with open('words_alpha.txt') as words:
        sample = words.read().split()
    print(" ".join(random.sample(sample, int(sys.argv[1]))))

if __name__ == '__main__':
    main()
