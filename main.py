
from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    try:
        ano_nascimento = int(request.form['ano_nascimento'])
        ano_atual = datetime.now().year
        idade = (ano_atual-ano_nascimento)

        if idade < 18:
            diagnostico = 'Menor de idade'
        elif idade > 18:
            diagnostico = 'Maior de idade'
        elif idade > 50:
            diagnostico = 'Idoso'

        return render_template('index.html', idade=idade, diagnostico=diagnostico)
    except Exception as e:
        idade = f'Ocorreu um erro inesperado {e}'
        diagnostico = ''
        return render_template('index.html', idade=idade, diagnostico=diagnostico)

if __name__ == '__main__':
    app.run(debug=True)



