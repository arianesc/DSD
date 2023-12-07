const url = 'http://localhost:3000';

const getPersonagens = () => {
    const inputId = 'meuInput';
    const inputValue = document.getElementById(inputId).value;

    url_personagem = url + `/personagem/${encodeURIComponent(inputValue)}`
    fetch(url_personagem)
    .then(response => {
        if (!response.ok) {
          throw new Error(`Erro na solicitação: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        // Faça algo com os dados recebidos
        console.log(data);
        exibirDadosNoHTML(data);
      })
      .catch(error => {
        // Trate erros durante a solicitação
        console.error('Erro durante a solicitação:', error);
      });
}

function exibirDadosNoHTML(data) {
    const resultadoElemento = document.getElementById('resultado');

    resultadoElemento.innerHTML = '';

    const nameElemento = document.createElement('h2');
    nameElemento.textContent = `Nome: ${data.name}`;

    const episodeElemento = document.createElement('p');
    episodeElemento.textContent = `Quantidade de episodios em que aparece: ${(data.episode).length}`;

    const speciesElemento = document.createElement('p');
    speciesElemento.textContent = `Raça: ${data.species}`;

    resultadoElemento.appendChild(nameElemento);
    resultadoElemento.appendChild(episodeElemento);
    resultadoElemento.appendChild(speciesElemento);
    
}
