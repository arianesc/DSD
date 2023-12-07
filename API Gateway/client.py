import requests


def api_info():
    try:
        response = requests.get('http://localhost:3000/api_info')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Erro ao consumir o Serviço 1: {e}')
        return None


class Personagem():

    def get_all():
        try:
            response = requests.get('http://localhost:3000/personagem')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro ao consumir: {e}')
            return None

    def get(id):
        try:
            response = requests.get(f'http://localhost:3000/personagem/{id}')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro ao consumir: {e}')
            return None


class Localizacao():

    def get_all():
        try:
            response = requests.get('http://localhost:3000/localizacao')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro ao consumir: {e}')
            return None

    def get(id):
        try:
            response = requests.get(f'http://localhost:3000/localizacao/{id}')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro ao consumir: {e}')
            return None

class Relatorio():
    def get(id):
        try:
            response = requests.get(f'http://localhost:3000/relatorio/{id}')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro ao consumir: {e}')
            return None

# class Episodio():
#
#     def get_all():
#         try:
#             response = requests.get('http://localhost:3000/episodio')
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             print(f'Erro ao consumir: {e}')
#             return None
#
#     def get(id):
#         try:
#             response = requests.get(f'http://localhost:3000/episodio/{id}')
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             print(f'Erro ao consumir: {e}')
#             return None


def exibir_menu():
    print("=== Menu ===")
    print("1. Informações da API")
    print("2. Todos os personagens")
    print("3. Personagem específico")
    print("4. Todos as Localizações")
    print("5. Localização específica")
    print("6. Relatório")
    print("7. Sair")


def realizar_acao(opcao):
    if opcao == 1:
        print("Executando Informações da API")
        if opcao == 1:
            print(api_info())

    elif opcao == 2:
        print("Executando Todos os personagens")

        if opcao == 2:
            print(Personagem.get_all())

    elif opcao == 3:
        print("Executando Personagem específico")
        if opcao == 3:
            id = int(input("Digite o id do personagem"))

            print(Personagem.get(id))

    elif opcao == 4:
        print("Executando todas as localizações")
        if opcao == 4:
            print(Localizacao.get_all())

    elif opcao == 5:
        print("Executando Localização específica")
        if opcao == 5:
            id = int(input("Digite o id da localização"))

            print(Localizacao.get(id))

    elif opcao == 6:
        print("Executando relatório")
        if opcao == 6:
            id = int(input("Digite o id do personagem"))
            print(Relatorio.get(id))

    elif opcao == 7:
        print("Saindo do programa")
    else:
        print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    opcao = 0

    while opcao != 7:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção (1-7): "))
            realizar_acao(opcao)
        except ValueError:
            print("Por favor, digite um número válido.")
