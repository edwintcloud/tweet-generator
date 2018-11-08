import random
import sys

def main():
    args = sys.argv[1:]
    randargs = random.sample(args, len(args))
    print(" ".join(randargs))

if __name__ == '__main__':
    main()
