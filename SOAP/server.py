from flask import Flask, request, Response
from zeep import Client
from zeep.wsdl.utils import etree_to_string

app = Flask(__name__)

@app.route('/service', methods=['POST', 'GET'])
def service():
    if request.method == 'GET':
        # Retorna o WSDL quando a solicitação é GET
        wsdl = open('service.wsdl').read()
        return Response(wsdl, content_type='text/xml')

    elif request.method == 'POST':
        # Manipula solicitações POST SOAP
        client = Client('service.wsdl')
        resposta = client.bind('ServicoBinding').EnviarMensagem(request.data)
        return resposta

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
