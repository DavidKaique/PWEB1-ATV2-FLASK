from flask import Flask, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return 'Conheça o meu curriculo clicando abaixo:' \
        '<br>' \
        '<br>' \
        '<a href="/sobre">Sobre</a>' \
        '<br>' \
        '<a href="/experiencia">Experiencia</a>' \
        '<br>' \
        '<a href="/formacao">Formacão</a>' \
        '<br>' \
        '<a href="/contato">Contato</a>' \

@app.route("/sobre", methods=["GET"])
def sobre():
    return 'Meu nome é David Kaique, tenho 21 anos e estou pronto para obter novos conhecimentos no mercado de TI.'

@app.route("/experiencia", methods=["GET"])
def experiencia():
    return 'Tenho o curso técnico de administração feito na EEEP Dr. José Iran Costa e estágio supervisonado no Cartório Eleitoral de Várzea Alegre.'

@app.route("/formacao", methods=["GET"])
def formacao():
    return 'Atualmente estou cursando Sistemas de Informação no IFCE Campus Cedro.'

@app.route("/contato", methods=["GET"])
def contato():
    return 'Email: david.kaique.sousa08@aluno.ifce.edu.br'

if __name__ == '__main__':
    app.run(debug=True)
