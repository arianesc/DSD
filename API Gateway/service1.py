from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dados')
def obter_dados():
    dados = {'mensagem': 'Dados do Microserviço 1'}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(port=5001)
