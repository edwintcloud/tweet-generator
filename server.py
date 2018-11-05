from flask import Flask, render_template, jsonify
import weighted_generator


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
  random_sentence = weighted_generator.generate_sentence('the_republic.txt', 12)
  return  render_template('index.html', sentence = random_sentence)

@app.route('/new_sentence', methods=['GET'])
def new_sentence():
  random_sentence = weighted_generator.generate_sentence('the_republic.txt', 12)
  return jsonify(random_sentence)
