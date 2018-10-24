import random
import sys

def main():
    args = sys.argv[1:]
    randomIndex = random.randint(0, len(args) - 1)
    print(args[randomIndex])

if __name__ == '__main__':
    main()
