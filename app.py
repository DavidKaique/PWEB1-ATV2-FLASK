from flask import Flask, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return '<a href="/sobre">sobre</a>' \
           '<br>' \
           '<a href="/experiencia">experiencia</a>' \
           '<br>' \
           '<a href="/formacao">formacao</a>' \
           '<br>' \
           '<a href="/contato">contato</a>' \

@app.route("/sobre", methods=["GET"])
def sobre():
    return 'Meu nome é David Kaique e atualmente estou cursando Sistemas de Informação no IFCE Campus Cedro.'

@app.route("/experiencia", methods=["GET"])
def experiencia():
    return 'Tenho o curso técnico de administração feito na EEEP José Iran Costa e estágio supervisonado no Cartório Eleitoral de Várzea Alegre.'

@app.route("/formacao", methods=["GET"])
def formacao():
    return 'Estou cursando o ensino superior.'

@app.route("/contato", methods=["GET"])
def contato():
    return 'Email: david.kaique.sousa08@aluno.ifce.edu.br'

if __name__ == '__main__':
    app.run(debug=True)