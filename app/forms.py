from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class Persona(FlaskForm):
    nombre = StringField('nombre',validators=[
        DataRequired(),
        Length(max=15, min=3)
    ])
    correo = StringField('correo',validators=[
        DataRequired(),
        Email()
    ])
    telefono = StringField('telefono',validators=[
        DataRequired(),
        Length(max=15, min=5)
    ])
    asunto = StringField('asunto',validators=[
        DataRequired(),
        Length(max=10, min=5)
    ])
    mensaje = StringField('mensaje',validators=[
        DataRequired(),
        Length(max=100, min=10)
    ])
    enviar= SubmitField('enviar')

