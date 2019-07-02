from getpass import getpass
import sys

from schedule import create_app
from schedule.db import db
from schedule.user.models import Person

app = create_app()

with app.app_context():
    username = input('Введите имя пользователя: ')

    if Person.query.filter(Person.username == username).count():
        print('Такой пользователь уже есть')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        sys.exit(0)

    new_user = Person(username=username, role = 'admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('Добавлен пользователь с id {} '.format(new_user.id))