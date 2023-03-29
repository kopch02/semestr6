from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, SubmitField, EmailField, SelectField, TextAreaField
from wtforms.validators import DataRequired

    

class JobsForm(FlaskForm):
    team_leader = SelectField('Ответсвенный', validators=[DataRequired()])
    job = TextAreaField('Описание работы', validators=[DataRequired()])
    work_size = StringField('Время работы в часах', validators=[DataRequired()])
    collaborators = SelectMultipleField('Участники', validators=[DataRequired()], validate_choice=False)

    submit = SubmitField('Войти')
    print(123)
