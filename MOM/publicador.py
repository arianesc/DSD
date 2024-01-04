import pika
"""
Resumindo, este script é um exemplo de um produtor RabbitMQ em 
Python que usa o exchange do tipo 'topic' para rotear mensagens 
com base em chaves de roteamento específicas. 
Ele envia uma mensagem para o RabbitMQ com uma chave de roteamento 
específica e imprime uma mensagem informativa indicando o sucesso 
do envio.
"""
# A função send_message é definida para enviar uma mensagem para o RabbitMQ.
# Ela cria uma conexão (connection) e um canal (channel) para comunicação com o RabbitMQ.


def send_message(message, routing_key):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='topic')
    # Esta linha declara um exchange chamado 'logs' com o tipo 'topic'.
    # O exchange é uma entidade no RabbitMQ que roteia mensagens para filas com base em certos critérios.

    channel.basic_publish(
        exchange='logs',
        routing_key=routing_key,
        body=message
    )
    # Aqui, a mensagem é publicada no RabbitMQ.
    # Ela é enviada para o exchange 'logs' com uma chave de roteamento específica (routing_key).
    # A mensagem em si é o corpo (body) da mensagem

    print(f" [x] Enviado '{message}' com chave de roteamento '{routing_key}'")

    # Uma mensagem informativa é impressa indicando que a mensagem foi enviada com sucesso

    connection.close()

    # A conexão é fechada para liberar os recursos.


if __name__ == '__main__':
    message = "Mensagem de exemplo"
    routing_key_to_use = "ariane"
    print("Digite 'sair' para encerrar")
    while message != "sair":
        message = input("Digite uma mensagem: ")
        send_message(message, routing_key_to_use)


