from flask_wtf import FlaskForm
from wtforms import DecimalField,SubmitField
from wtforms.validators import DataRequired 

class Paypal(FlaskForm):
    comisiones = DecimalField("Monto:", validators=[DataRequired(message='Introduza un número')])
    submit = SubmitField("Calcular")