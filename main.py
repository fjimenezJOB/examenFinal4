from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import CSRFProtect
from metodos import Logica
import time

app = Flask(__name__)
app.secret_key = 'examen_final'
csrf = CSRFProtect(app)
game = Logica(500, 0, False, 0)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ruleta', methods=['POST', 'GET'])
def ruleta():
    elegidas = request.form.getlist('opciones')
    game.añadir_opciones(elegidas)
    suerte = game.random()
    saldo, score, ronda, saltar, pierde = game.normas(suerte)
    premios = game.leer_historico()
    for line in premios:
        print(premios)
    context = {
        'saldo': saldo,
        'suerte': suerte,
        'score': score,
        'ronda': ronda,
        'saltar': saltar,
        'opciones': elegidas,
        'premios': premios
    }

    if pierde == True:
        return redirect('/final')

    return render_template('game.html', **context)


@app.route('/final', methods=['POST', 'GET'])
def final():
    nombre = request.form.get('nombre')
    score = game.getScore()
    game.escribir(nombre, score)
    return render_template('final.html', score = score)

@app.errorhandler(404)
def error(error):
    return '<h1> Pagina no encontrada...(404)<h1>'


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)