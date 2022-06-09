from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    object = IntegerField('Введите номер предмета:', validators=[DataRequired()])
    submit = SubmitField('Далее')


