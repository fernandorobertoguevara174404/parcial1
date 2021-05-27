from app.forms import Paypal
from app import app
from flask import render_template

@app.route("/" , methods=["GET","POST"])
def index():
    form = Paypal()
    if form.validate_on_submit():
        comisiones = float(form.comisiones.data)
        resul = calculo_com(comisiones)
        return render_template("resultado.html", comisiones = comisiones, resul = resul)
    return render_template("index.html",form=form)

def calculo_com(comisiones):
        fija = 5
        if comisiones >= 50000 and comisiones <= 249999.99:
            resul = comisiones - (comisiones * 0.0365) - (fija)
            return resul

        elif comisiones >= 250000 and comisiones <= 499999.99:
            resul = comisiones - (comisiones * 0.0345) - (fija)
            return resul

        elif comisiones >= 500000 and comisiones <= 999999.99:
            resul = comisiones - (comisiones * 0.0315) - (fija)
            return resul

        elif comisiones >= 1000000:
            resul = comisiones - (comisiones * 0.0295) - (fija)
            return resul
        else:
            resul = comisiones - (fija)
            return resul