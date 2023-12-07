const baseUrl = 'http://localhost:3000';

const getRelatorio = () => {
    const inputIds = 'relatorioInput';
    const inputValueId = document.getElementById(inputIds).value;

    url_relatorio = baseUrl + `/relatorio/${encodeURIComponent(inputValueId)}`
    fetch(url_relatorio)
    .then(response => {
        if (!response.ok) {
          throw new Error(`Erro na solicitação: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log(data);
        exibirRelatorioNoHTML(data);
      })
      .catch(error => {
        console.error('Erro durante a solicitação:', error);
      });
}

function exibirRelatorioNoHTML(data) {
    const resultadoRelatorio = document.getElementById('relatorio');

    resultadoRelatorio.innerHTML = '';

    const nomeRelatorio = document.createElement('p');
    nomeRelatorio.textContent = `Nome: ${data[0].name}`;

    const localRelatorio = document.createElement('p');
    localRelatorio.textContent = `Localização: ${data[1].name}`;


    resultadoRelatorio.appendChild(nomeRelatorio);
    resultadoRelatorio.appendChild(localRelatorio);
    
}