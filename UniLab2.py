# -*- coding: cp1251 -*-
passw = input("Создайте пароль : ")
print("Чтобы продолжить вам нужно ввести пароль заново")
passwConfirm = input("Введите пароль : ")
if passwConfirm == passw :
    print("Пароль принят")
else :
    print("Пароль отклонен")
