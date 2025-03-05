document.getElementById('form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const height = document.getElementById('height').value
    const weight = document.getElementById('weight').value
    const resultDiv = document.getElementById('result')
    const errorDiv = document.getElementById('error')

    resultDiv.innerHTML = ''
    errorDiv.innerHTML = ''

    try {
        const response = await axios.post('http://localhost:5000/calculate-imc', {
            height,
            weight
        });

        if (!response.ok) {
            throw new Error('Erro na comunicação com o servidor');
        }

        const data = await response.json();

        resultDiv.innerHTML = `
                    Seu IMC: ${data.imc}<br>
                    Classificação: ${data.classification}
                `;
    } catch{
        errorDiv.innerHTML = `Erro: ${error.message}`;
    }


})

