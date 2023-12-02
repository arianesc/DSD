from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/informacoes')
def obter_informacoes():
    informacoes = {'mensagem': 'Informações do Microserviço 2'}
    return jsonify(informacoes)

if __name__ == '__main__':
    app.run(port=5002)
