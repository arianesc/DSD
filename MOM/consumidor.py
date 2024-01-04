import pika #  biblioteca Python para interagir com o RabbitMQ


def callback(ch, method, properties, body):
    print(f" [x] Recebido '{body}' com chave de roteamento '{method.routing_key}'")
#Esta função callback será chamada sempre que uma mensagem for recebida.
# Ela imprime o corpo da mensagem (body) e a chave de roteamento (method.routing_key).


# responsável por iniciar o consumo de mensagens.
# Ela cria uma conexão (connection) e um canal (channel)
# para comunicação com o RabbitMQ.
def start_consuming(routing_key):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='topic')
    # Esta linha declara um exchange chamado 'logs' com o tipo 'topic'.
    # O exchange é uma entidade no RabbitMQ que roteia mensagens para filas com base em certos critérios.

    result = channel.queue_declare(queue='', exclusive=True)
    # Aqui, uma fila anônima é declarada. A fila é criada exclusiva para a
    # conexão atual e um nome de fila é obtido através de result.method.queue.

    queue_name = result.method.queue

    channel.queue_bind(exchange='logs', queue=queue_name, routing_key=routing_key)
    # Esta linha vincula a fila à troca ('logs') usando uma chave de roteamento específica (routing_key).


    print(f' [*] Aguardando mensagens com chave de roteamento "{routing_key}". Para sair, pressione CTRL+C')
    # Uma mensagem informativa é impressa indicando que o consumidor está aguardando mensagens com uma chave de roteamento específica.

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    # Aqui, o método basic_consume é usado para começar a consumir mensagens da fila.
    # A função de callback callback será chamada para cada mensagem recebida.
    # O parâmetro auto_ack=True indica que as mensagens serão automaticamente reconhecidas após serem entregues.

    channel.start_consuming()
    # Este método inicia o loop de consumo, o que significa que o consumidor ficará esperando por mensagens
    # indefinidamente até que seja interrompido manualmente (pressionando CTRL+C, por exemplo).


if __name__ == '__main__':
    routing_key_to_consume = "ariane"
    start_consuming(routing_key_to_consume)

# Esta parte verifica se o script está sendo executado diretamente (não importado como um módulo) e,
# se sim, inicia o consumo de mensagens com a chave de roteamento "exemplo.*".