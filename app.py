from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/teste")
def ola_mundo():
    return "<p>Olá, Mundo!</p>"

@app.route("/")
def pag_imc():
    return render_template("pag_imc.html")

@app.route("/resultado", methods=['GET', 'POST'])
def resultado():
    if request.method == "POST":
        nome = request.form['nome']
        idade = request.form['idade']
        peso = request.form['peso'].replace(",", ".")
        altura = request.form['altura'].replace(",", ".")

        peso = float(peso)
        altura = float(altura)

        res = round(peso / (altura * altura), 2)
        if res < 18.5:
            baixo_peso =  "{} Baixo Peso".format(res)
            return render_template("resultado.html", nome=nome, idade=idade, peso=peso, altura=altura, res=baixo_peso)
        elif res < 25:
            peso_normal =  "{} Peso Normal".format(res)
            return render_template("resultado.html", nome=nome, idade=idade, peso=peso, altura=altura, res=peso_normal)
        elif res < 30:
            sobrepeso =  "{} Sobrepeso".format(res)
            return render_template("resultado.html", nome=nome, idade=idade, peso=peso, altura=altura, res=sobrepeso)
        elif res < 35:
            obesidade1 =  "{} Obesidade grau |".format(res)
            return render_template("resultado.html", nome=nome, idade=idade, peso=peso, altura=altura, res=obesidade1)
        elif res < 40:
            obesidade2 =  "{} Obesidade grau ||".format(res)
            return render_template("resultado.html", nome=nome, idade=idade, peso=peso, altura=altura, res=obesidade2)
        else:
            obesidade3 =  "{} Obesidade grau |||".format(res)
            return render_template("resultado.html", nome=nome, idade=idade, peso=peso, altura=altura, res=obesidade3)            
        
    return render_template("pag_imc.html")
    
if __name__ == "__main__":
    app.run(debug=True)
