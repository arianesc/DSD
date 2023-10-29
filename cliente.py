import rpyc

if __name__ == "__main__":
    conn = rpyc.connect("localhost", 12345) #  Estabelece uma conexão com o servidor RMI que está sendo executado localmente na porta 12345.

    while True:
        print("1. Adicionar Item")
        print("2. Listar Itens")
        print("3. Remover Item")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            item = input("Digite o item para adicionar: ")
            response = conn.root.exposed_add_item(item)
            print("Resposta do servidor:", response)
        elif choice == "2":
            items = conn.root.exposed_get_items()
            print("Itens no servidor:", items)
        elif choice == "3":
            item = input("Digite o item para remover: ")
            response = conn.root.exposed_remove_item(item)
            print("Resposta do servidor:", response)
        elif choice == "4":
            break
        else:
            print("Opção inválida.")

    conn.close()
