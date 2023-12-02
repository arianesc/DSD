from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Rota para o primeiro microserviço
@app.route('/servico1')
def servico1():
    try:
        response = requests.get('http://localhost:5001/dados')
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar o Microserviço 1: {e}')
        return jsonify({'error': 'Erro ao acessar o Microserviço 1'}), 500

# Rota para o segundo microserviço
@app.route('/servico2')
def servico2():
    try:
        response = requests.get('http://localhost:5002/informacoes')
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar o Microserviço 2: {e}')
        return jsonify({'error': 'Erro ao acessar o Microserviço 2'}), 500

if __name__ == '__main__':
    app.run(port=3000)
