from flask_wtf import FlaskForm
from db_models.model import db, User
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError, InputRequired


class RegForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()])
    second_name = StringField('Фамилия', validators=[DataRequired()])
    email = EmailField('Адрес почты', validators=[DataRequired(), Email(), InputRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Submit')

    def validate_email(self, email):
        # count the number of user ids for that email
        # if it's not 0, there's a user with that email already
        print(1234)
        a = db.session.query(db.func.count(User.id)).filter_by(email=email.data).scalar()
        print(a)
        print(email.data)
        if a:
            raise ValidationError('The email is already registered in the system')
