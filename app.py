from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "CONSEGUI CUSTOMIZAR A MENSAGEM - BRUNA NYULAS"

if __name__ == '__main__':
    app.run(debug=True)