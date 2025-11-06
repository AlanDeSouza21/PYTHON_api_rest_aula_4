from flask import Flask, render_template, request, redirect, url_for
from db import db
from models import Contato

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db" # configuração padrão 
db.init_app(app) # conexão entre o banco de dados e a classe db.py

# rotas
@app.route('/')
def home():
    contatos = db.session.query(Contato).all() # variavel que armazena o conteúdo da tabela 
    return render_template('home.html', contatos=contatos) # linha de codigo para enviar o conteúdo para o arquivo home.html

# REGISTRAR
@app.route('/registrar_contato', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template('registrar_contato.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        telefone = request.form['telefoneForm']
        
        instancia = Contato(nome=nome, telefone=telefone) # instancia que irá inserir dados na tabela usando a classe "Contato" localizada no arquivo "models.py"
        db.session.add(instancia) # insere os dados 
        db.session.commit() # finaliza a execução

        return redirect(url_for('home')) # essa linha de codigo direciona o usuário para a página principal, nesse caso é a página home, para isso é necessário importar as funções redirect e url_for da biblioteca flask, a palavra 'home' dentro da url_for representa a função home localizada na primeira rota dessa api

# EDITAR
@app.route('/editar/<int:id>', methods=["GET", "POST"]) # "<int:id>" representa o parametro que virá no formato de inteiro
def editar(id):
    contato = db.session.query(Contato).filter_by(id=id).first() # o filtro "filter_by(id=id)" serve para a variavel contato armazenar o dado correspondente ao id que será digitado
    if request.method == "GET":
        return render_template('editar.html', contato=contato)
    elif request.method == "POST":
        nome = request.form['nomeForm']
        telefone = request.form['telefoneForm']

        contato.nome = nome
        contato.telefone = telefone
        db.session.commit()
        return redirect(url_for('home'))
    

# DELETAR
# rota direcionada para o arquivo home
@app.route('/deletar/<int:id>') # "<int:id>" representa o parametro que virá no formato de inteiro
def deletar(id):
    contato = db.session.query(Contato).filter_by(id=id).first() # o filtro "filter_by(id=id)" serve para a variavel contato armazenar o dado correspondente ao id que será digitado 
    db.session.delete(contato) # linha de comando que acessa o banco de dados para deletar o dado referente ao id usado no parametro, contato nesse caso é a variável que precede essa linha 
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)