# -*- coding: utf-8 -*-

from itertools import combinations


while True:
    print("Выберите задание, которое хотите проверить : \n 1\n 2\n 3\n 4\n 5 - Выход")
    taskChoice = input()
    taskChoice = int(taskChoice)
    
    if taskChoice == 1:
        passw = input("Создайте пароль : ")
        print("Чтобы продолжить вам нужно ввести пароль заново")
        passwConfirm = input("Введите пароль : ")
        if passwConfirm == passw :
            print("Пароль принят")
        else :
            print("Пароль отклонен")
        print("Программа завершена")
        
    if taskChoice == 2:
        newAvalPlaces = 50
        while True:
            availablePlaces = newAvalPlaces
            
            place = input(f"В плацкарте доступно {availablePlaces} мест, выберите одно из них ")
            place = int(place)
            if place < 1 and place > availablePlaces :
                print("Такого места нет")

            choosenPlace = place % 6
            if choosenPlace == 1 :
                print("Верхняя левая полка")
            if choosenPlace == 2 :
                print("Нижняя левая полка")
            if choosenPlace == 3 :
                print("Верхняя правая полка")
            if choosenPlace == 4 :
                print("Нижняя левая полка")
            if choosenPlace == 5 :
                print("Боковая верхняя полка")
            if choosenPlace == 6 :
                print("Боковая левая полка")
            
            
            whatNext = input("Вы хотите продолжить ? Введите число \n 1 - да \n 2 - нет ")
            whatNext = int(whatNext)
            if whatNext == 2:
                break
            else:
                newAvalPlaces -= 1
                
    if taskChoice == 3:
        while True:
            jod = input("Введите год : ")
            jod = int(jod)
            if jod > 0 :
                if jod % 4 == 0 and jod % 100 != 0 or jod % 400 == 0:
                    print(f"{jod} <- високосный год")
                else:
                    print(f"{jod} <- не вишнекостный год")
            else :
                print("Время неизбежно и безустанно марширует только вперед")

            whatNext = input("Вы хотите продолжить ? Введите число \n 1 - да \n 2 - нет \n ")
            whatNext = int(whatNext)
            if whatNext == 2:
                break
    
    if taskChoice == 4:
        while True:
            colorLib = {1: "Красный", 2: "Желтый", 3: "Синий", 4: "Оранжевый", 5: "Фиолетовый", 6: "Зеленый"}
            print("3 основных цвета : 1) Красный 2) Желтый 3) Синий")

            firstColor = input("Выберите номер первого основного цвета, который хотите смешать - ")
            firstColor = int(firstColor)
            if firstColor not in colorLib:
                print("Выберите число основного цвета, давайте начнем заново")
                break
            
            secondColor = input("Выберите номер второго основного цвета, который хотите смешать - ")
            secondColor = int(secondColor)
            if secondColor not in colorLib:
                print("Выберите число основного цвета, давайте начнем заново")
                break
            
            if firstColor == secondColor:
                print("Цвета должны отличаться, иначе выйдет тот же цвет, давайте начнем заново")
                break

            if firstColor == 1 and secondColor == 2:
                combination = colorLib[4]
                print("Получился " + combination + " цвет")
            elif firstColor == 1 and secondColor == 3:
                combination = colorLib[5]
                print("Получился " + combination + " цвет")
            elif firstColor == 2 and secondColor == 3:
                combination = colorLib[6]
                print("Получился " + combination + " цвет")
            
            whatNext = input("Вы хотите попробовать заново ? Введите число \n 1 - да \n 2 - нет \n ")
            whatNext = int(whatNext)
            if whatNext == 2:
                break

    if taskChoice == 5:
        break
        