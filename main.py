from flask import Flask, request, make_response, redirect, render_template
from app.config import Config
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.forms import Persona

app = create_app()

app.secret_key = "F3YEFgqBw:0%p\~mSF"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    form = Persona()
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        asunto = request.form['asunto']
        print(nombre)
        print(correo)
        print(telefono)
        print(asunto)
    return render_template('form.html', form= form)

def main():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    app.config.from_object(Config)
    bootstrap = Bootstrap(app)
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    return app
