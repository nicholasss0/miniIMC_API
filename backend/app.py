from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calculate_imc_classification(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"


@app.route('/calculate-imc', methods=['POST'])
def calculate_imc():
    data = request.json
    height = float(data.get('height')) 
    weight = float(data.get('weight'))  


    height_meters = height / 100


    imc = weight / (height_meters ** 2)


    classification = calculate_imc_classification(imc)

    return jsonify({
        'imc': round(imc, 2),
        'classification': classification
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3005)