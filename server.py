from flask import Flask, render_template, jsonify
from modules.app import random_markov_sentence


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
  return  render_template('index.html', sentence = random_markov_sentence('the_republic'))

@app.route('/new_sentence', methods=['GET'])
def new_sentence():
  return jsonify(random_markov_sentence('the_republic'))
