from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import CSRFProtect
import form
import csv

app = Flask(__name__)
app.secret_key = 'examen_final'
csrf = CSRFProtect(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/enviar', methods=['POST', 'GET'])
def enviar():


    return render_template('index.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
