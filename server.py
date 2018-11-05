from flask import Flask
import weighted_generator


app = Flask(__name__)


@app.route('/')
def hello_world():
  random_sentence = weighted_generator.main('the_republic.txt', 12)
  return random_sentence