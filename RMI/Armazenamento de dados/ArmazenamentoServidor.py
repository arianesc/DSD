import rpyc

class DataStorageService(rpyc.Service):

    def on_connect(self, conn):
        print("Conexão estabelecida com o cliente.")
        self.data = []

    def on_disconnect(self, conn):
        print("Conexão encerrada.")

    def exposed_add_item(self, item):
        self.data.append(item)
        return "Item adicionado com sucesso."

    def exposed_get_items(self):
        return self.data

    def exposed_remove_item(self, item):
        if item in self.data:
            self.data.remove(item)
            return "Item removido com sucesso."
        else:
            return "Item não encontrado."

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer # permite criar um servidor RMI que pode lidar com várias conexões de clientes simultaneamente.
    server = ThreadedServer(DataStorageService, port=12345) # Cria uma instância da classe ThreadedServer usando DataStorageService como o serviço a ser oferecido e a porta 12345.
    print("Servidor RMI iniciado na porta 12345.")
    server.start() #  Inicia o servidor RMI, aguardando conexões de clientes. O servidor é iniciado em uma thread separada para que possa lidar com várias conexões simultaneamente.
