from http.server import BaseHTTPRequestHandler
import random
import string


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        num_of_walks = random.randint(6, 8)
        words = get_words('dracula')
        cleaned_words = clean(words)
        dictograms = generate_dictograms(cleaned_words)
        random_words = []
        for i in range(num_of_walks):
            walk = random_walk(dictograms)
            random_words.append(walk[0])
            random_words.append(walk[1])
        random_words.pop()
        sentence = generate_sentence(random_words)
        self.wfile.write(sentence.encode())
        return


def generate_sentence(words):
    '''Takes a list of random weighted words and generates a sentence'''
    # Capitalize first word
    words[0] = words[0].capitalize()

    # save sentence as a variable to return later
    sentence = ' '.join(words)+'.'

    # return random words
    return sentence


def generate_dictograms(words):
    '''Takes a list of words and generates a dictionary of dictograms of each word directly following each word'''

    # create a dictionary to hold our dictograms
    dictograms = {}

    # First we must iterate through the words list, exluding the last item
    for index in range(len(words) - 1):
        # check if the word is not in dictionary of word histograms already
        if words[index] not in dictograms:
            # create new dictogram for the word in dictionary of dictograms
            dictograms[words[index]] = Dictogram()
        # add count of word following word to dictogram
        dictograms[words[index]].add_count(words[index+1])

    # return dictograms dictionary
    return dictograms


def random_walk(dict_of_dictograms):
    '''Takes a dictionary of dictograms and returns a random weighted traversal along the markov chain'''

    # first pick a random dictogram
    key = random.choice(list(dict_of_dictograms))
    dictogram = dict_of_dictograms[key]

    # now pick a random weighted word
    random_weighted_word = get_random_word(dictogram)

    # return the words
    return [key, random_weighted_word]


def clean(words):
    '''Normalizes word list into actual words'''

    # translation table we will use to remove punctuation and numbers
    translation_table = str.maketrans(
        '', '', '''!"#$%&()*+,./:;<=>?@[\]^_`{|}~`1234567890''')

    # split dashed words into seperate words and remove all whitespace
    words[:] = [i.replace(' ', '') for e in words for i in e.split('--')]

    # remove Roman Numerals, Initials, Abbreviations, and single
    # letters that aren't words - wow this is gonna be ugly
    alphabet = [i + '.' for i in string.ascii_uppercase]
    single_letter_words = ['a', 'i']
    abbreviations3 = ['st.', 'dr.', 'mr.']
    abbreviations4 = ['mrs.', 'sq.,', 'esq.']
    words[:] = [i for i in words if i[-2:] not in alphabet and
                i[-3:].lower() not in abbreviations3 and
                i[-4:].lower() not in abbreviations4 and
                not (len(i) == 1 and i.lower() not in
                     single_letter_words)]

    # remove numbers and punctuation and make all lowercase
    words[:] = [i.translate(translation_table).lower().lstrip(
        "'").rstrip("'") for i in words]

    # return normalized word list
    return words


def get_words(file_name):
    '''Opens file and returns list of words in file'''

    # open the file safely
    with open(file_name + '.txt') as file:
        words = file.read().split()

    # return the file as a list of words
    return words

def get_random_word(gram):
    '''Takes a histogram and generates a single random word based on weights'''

    # get type of gram (dictogram or listogram)
    histogram_type = str(type(gram).__name__ )

    if(histogram_type == "Listogram"):
        histogram = gram
    elif(histogram_type == "Dictogram"):
        histogram = [(key, value) for key, value in gram.items()]
    else:
        return

    # get total number of words in source
    total_words = gram.tokens

    # create list of words and counts
    words, counts = zip(*histogram)

    # create list of weights from counts
    weights = [count/total_words for count in counts]

    # generate a random word based on weights
    random_word = ''
    while random_word == '':
        random_index = random.randrange(len(words))
        if random.random() < weights[random_index]:
            random_word = words[random_index]

    # return random word
    return random_word

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        if word in self:
            self[word] += count
        else:
            self[word] = count
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        return self.get(word, default=0)
