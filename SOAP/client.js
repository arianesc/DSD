const soap = require('soap');

const url = 'http://localhost:8080/service?wsdl';

soap.createClient(url, (err, client) => {
    if (err) {
        console.error(err);
        return;
    }

    const mensagem = { Texto: 'Olá, servidor SOAP!' };

    client.ServicoPortType.ServicoBinding.EnviarMensagem(mensagem, (err, result) => {
        if (err) {
            console.error(err);
        } else {
            console.log(result);
        }
    });
});
