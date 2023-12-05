from flask import Flask, jsonify
import requests


base_url = "https://rickandmortyapi.com/api/"
character_url = base_url + "character/"
location_url = base_url + "location/"
episode_url = base_url + "episode/"

app = Flask(__name__)


@app.route('/api_info', methods=['GET'])
def api_info(self):
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar o Microserviço 1: {e}')
        return jsonify({'error': 'Erro ao acessar o Microserviço 1'}), 500


# PERSONAGEM
@app.route('/personagem', methods=['GET'])
def get_all_characters():
    try:
        response = requests.get(character_url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar o Microserviço: {e}')
        return jsonify({'error': 'Erro ao acessar o Microserviço 1'}), 500


@app.route('/personagem/<id>', methods=['GET'])
def get_character(id):
    try:
        response = requests.get(character_url + str(id))
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar o Microserviço: {e}')
        return jsonify({'error': 'Erro ao acessar o Microserviço 1'}), 500


# LOCALIZAÇÂO
@app.route('/localizacao', methods=['GET'])
def get_all_locations():
    try:
        response = requests.get(location_url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar o Microserviço: {e}')
        return jsonify({'error': 'Erro ao acessar o Microserviço 1'}), 500


@app.route('/localizacao/<id>', methods=['GET'])
def get_location(id):
    try:
        response = requests.get(location_url + str(id))
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar o Microserviço: {e}')
        return jsonify({'error': 'Erro ao acessar o Microserviço 1'}), 500

# # EPISODIO
# @app.route('/episodio')
# def get_all_episodes():
#     try:
#         response = requests.get(episode_url)
#         response.raise_for_status()
#         return jsonify(response.json())
#     except requests.exceptions.RequestException as e:
#         print(f'Erro ao acessar o Microserviço: {e}')
#         return jsonify({'error': 'Erro ao acessar o Microserviço 1'}), 500
#
# @app.route('/episodio/<id>')
# def get_episode(id):
#     try:
#         response = requests.get(episode_url + str(id))
#         response.raise_for_status()
#         return jsonify(response.json())
#     except requests.exceptions.RequestException as e:
#         print(f'Erro ao acessar o Microserviço: {e}')
#         return jsonify({'error': 'Erro ao acessar o Microserviço 1'}), 500

if __name__ == '__main__':
    app.run(port=3000)
    app.run(debug=True)