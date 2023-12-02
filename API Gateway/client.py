import requests

def consumir_servico1():
    try:
        response = requests.get('http://localhost:3000/servico1')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Erro ao consumir o Serviço 1: {e}')
        return None

def consumir_servico2():
    try:
        response = requests.get('http://localhost:3000/servico2')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Erro ao consumir o Serviço 2: {e}')
        return None

if __name__ == '__main__':
    # TODO input para o cliente selecionar qual serviço vai consumir.

    resultado_servico1 = consumir_servico1()
    resultado_servico2 = consumir_servico2()

    if resultado_servico1:
        print('Resultado do Serviço 1:', resultado_servico1)

    if resultado_servico2:
        print('Resultado do Serviço 2:', resultado_servico2)
