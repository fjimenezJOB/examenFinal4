from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import CSRFProtect
from metodos import Logica

app = Flask(__name__)
app.secret_key = 'examen_final'
csrf = CSRFProtect(app)
game = Logica()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/enviar', methods=['POST', 'GET'])
def enviar():
    elegidas = request.form.getlist('opciones')
    suerte = game.random_opciones(elegidas)

    return render_template('game.html', suerte = suerte)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)