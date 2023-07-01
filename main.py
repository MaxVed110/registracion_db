# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен
# быть зашифрован.
from flask import Flask, render_template, request, redirect
from db_models.model import db, User
from flask_wtf.csrf import CSRFProtect
from reg_forms.forms import RegForm
import hashlib


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///infodatabase.db'
app.config['SECRET_KEY'] = 'b8887dbf59a60aaf13215bb74faed84fc1cc0a7d3446fbd5ca4f52ebf63b827f'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        second_name = form.second_name.data
        email = form.email.data
        password = hashlib.md5(form.password.data.encode()).hexdigest()
        us = User(first_name=first_name, second_name=second_name, email=email, password=password)
        db.session.add(us)
        db.session.commit()
        return redirect('/')
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
