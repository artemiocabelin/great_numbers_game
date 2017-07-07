from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    # session['random'] = -1
    # session['outcome'] = ''
    if session['random'] == -1:
        randomNum = random.randint(1,100)
        session['random'] = randomNum
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['guess'] = request.form['guess']
    if session['guess'] == str(session['random']):
        session['outcome'] = 'Correct!'
    elif session['guess'] < str(session['random']):
        session['outcome'] = 'Too Low!'
    elif session['guess'] > str(session['random']):
        session['outcome'] = 'Too High!'
    return redirect('/')

@app.route('/restart', methods=['POST'])
def restart():
    session['random'] = -1
    session['outcome'] = ''
    return redirect('/')

app.run(debug=True)