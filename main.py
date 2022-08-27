from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)#Referência ao objeto FLASK, criando uma variável APP que guarda os elementos Flask


@app.route("/")#Página Index = Primeira página de qualquer site
def homepage():
    return render_template("index.html")


@app.route("/soma", methods=['POST','GET'])#Página de soma = calculadora do site
def soma():
    if request.method =='POST':
        num1 = request.form['num1']
        num2 = request.form['num2']




if __name__ == '__main__':
 app.run(debug=True)

