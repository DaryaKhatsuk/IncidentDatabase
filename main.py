import sqlite3
from random import *
import datetime
datetime.date(2001, 10, 28)


class IncidentDatabase:
    def __init__(self):
        self.employees()

    # сделано
    def employees(self):
        conn = sqlite3.connect(r"IncidentDB.db")
        cursor = conn.cursor()
        creattab = "create table IF NOT EXISTS employees(id INTEGER PRIMARY KEY autoincrement, " \
                    "'registration number of the certificate' int, 'full name' text, 'title' text, 'address' text, " \
                    "'family composition' text);"
        cursor.execute(creattab)
        conn.commit()
        tabl = "insert into employees('registration number of the certificate', 'full name', 'title', " \
                "'address', 'family composition') values (?, ?, ?, ?, ?);"
        while True:
            exit1 = input("Для завершения введите 'д' ")
            if exit1 == "д":
                break
            else:
                try:
                    cursor.execute(tabl, (randint(1000000, 9999999), input("ФИО сотрудника: "),
                                               input("Звание: "), input("Адрес: "), input("Состав семьи: ")))
                except TypeError:
                    print("Неверный ввод")
        conn.commit()
        zap = "select * from employees;"
        cursor.execute(zap)
        k = cursor.fetchall()
        print(k)
        cursor.close()
        conn.close()

        creattab = "create table IF NOT EXISTS faces(id INTEGER PRIMARY KEY autoincrement, 'number criminal case' int, " \
                   "'person (first and last name)' text,'registration number of person' int, 'address' text, " \
                   "'num convictions' int, 'fingerprint cipher' text, 'status of a person' text);"
        cursor.execute(creattab)
        conn.commit()
        tabl = "insert into faces('number criminal case', 'person (first and last name)', " \
               "'registration number of person', 'address', 'num convictions', 'fingerprint cipher', " \
               "'status of a person') values (?, ?, ?, ?, ?, ?, ?);"
        while True:
            exit1 = input("Для завершения введите 'д' ")
            if exit1 == "д":
                break
            else:
                try:
                    cursor.execute(tabl, (0, input("ФИО гражданина: "),
                                               int(input("Регистрационный номер лица: ")), input("Адрес: "),
                                               int(input("Количество судимостей: ")), input("Шифр отпечатков пальцев: "),
                                               input("Статус гражданина в происшествии: ")))
                except TypeError:
                    print("Неверный ввод")
        conn.commit()
        zap = "select * from faces;"
        cursor.execute(zap)
        k = cursor.fetchall()
        print(k)
        cursor.close()
        conn.close()

        creattab = "create table IF NOT EXISTS IncidentDB(id INTEGER PRIMARY KEY autoincrement, 'registration number' " \
                   "int, 'date of registration' int, 'type event' text, 'source messages' text, " \
                   "'registration criminal case' text, 'number criminal case' int, 'number of the operation' int, " \
                   "'registration number of the employee' int, 'the scene of the incident' text, " \
                   "'a brief description of the incident' text);"
        cursor.execute(creattab)
        conn.commit()
        tabl1 = "insert into IncidentDB('registration number', 'date of registration', 'type event', " \
                "'source messages', 'registration criminal case', 'number criminal case', 'number of the operation', " \
                "'registration number of the employee', 'the scene of the incident', " \
                "'a brief description of the incident') values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        while True:
            exit1 = input("Для завершения введите 'д' ")
            if exit1 == "д":
                break
            else:
                try:
                    cursor.execute(tabl1, (randint(1000000, 9999999),
                                                datetime.date(randint(2001, 2022), randint(1, 12), randint(1, 31)),
                                                input("Тип происшествия: "), input("Источник сообщения: "),
                                                input("Уголовное дело(да, нет): "), 0,
                                                int(input("Регистрационный номер сообщения: ")),
                                                input("Регистрационный номер сотрудника: "),
                                                input("Место происшествия: "),
                                                input("Краткое описание происшествия: ")))
                except TypeError:
                    print("Неверный ввод")
        zap = "select * from IncidentDB;"
        cursor.execute(zap)
        k1 = cursor.fetchall()
        print(k1)
        cursor.close()
        conn.close()

    # # добав. персон и связать номера дел
    # def faces(self):
    #
    #
    # # добав. номера уголовных дел, при их наличии
    # def incident(self):


base = IncidentDatabase()
base.employees()
# base.incident()
# base.faces()
