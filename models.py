from db import db # o primeiro db está acessando o arquivo e o segundo db acessa a variavel db

# classe criadora de tabelas 
class Contato(db.Model):
    __tablename__ = 'contatos' # nome da tabela 

# colunas
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<{self.nome}>" # trata-se de um método especial, por exemplo "if __name__ == "__main__":", tem como objetivo retornar uma string que represente o objeto de forma clara e precisa

