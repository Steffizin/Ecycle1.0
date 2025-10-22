from flask import Flask, render_template, request, flash, redirect, session, jsonify, g
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ecycle123'
app.config['DATABASE'] = 'usuarios.db'


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def create_table():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL,
        numero TEXT NOT NULL,
        complemento TEXT NOT NULL
    );
''')
    db.commit()

with app.app_context():
    create_table()


@app.route("/")
def principal():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('telaLogin.html')


@app.route("/acesso", methods=['POST'] )
def acesso():
    email = request.form.get('email')
    senha = request.form.get('password')

    db = get_db()
    usuario = db.execute('SELECT * FROM usuario WHERE email = ? AND senha = ?', (email, senha)).fetchone()

    if usuario:
        return redirect('/home')
    else:
        flash('Email e/ou senha invalidos, tente novamente!')
        return redirect('/login')
    
    
@app.route("/cadastro")
def cadastro():
    return render_template('telaCadastro.html')


@app.route("/cadastrando", methods=['POST'])
def cadastrando():
    nome = request.form.get('name')
    email = request.form.get('email')
    senha = request.form.get('password')
    cpf = request.form.get('cpf')
    endereco = request.form.get('address')
    numero = request.form.get('number')
    complemento = request.form.get('complement')

    db = get_db()
    db.execute('''
        INSERT INTO usuario (nome, email, senha, cpf, endereco, numero, complemento) VALUES(?, ?, ?, ?, ?, ?, ?)
''', (nome, email, senha, cpf, endereco, numero, complemento))
    
    db.commit()

    flash('Senha bem vindo, {nome}!!')

    return redirect('/home')


@app.route('/home')
def home():
    return render_template('telaPrincipal.html')


if __name__ in '__main__':
    app.run(debug=True)