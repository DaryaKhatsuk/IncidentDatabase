import sqlite3
from random import *
import datetime
datetime.date(2001, 10, 28)


class IncidentDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("IncidentDB.db")
        self.cursor = self.conn.cursor()

    def employees(self):
        creattab = "create table IF NOT EXISTS employees(id INTEGER PRIMARY KEY autoincrement, " \
                    "'registration number of the certificate' int, 'full name' text, 'title' text, 'address' text, " \
                    "'family composition' text);"
        self.cursor.execute(creattab)
        self.conn.commit()
        tabl = "insert into employees('registration number of the certificate', 'full name', 'title', " \
                "'address', 'family composition') values (?, ?, ?, ?, ?);"
        while True:
            exit1 = input("Для завершения введите 'д' ")
            if exit1 == "д":
                break
            else:
                try:
                    self.cursor.execute(tabl, (randint(1000000, 9999999), input("ФИО сотрудника: "),
                                               input("Звание: "), input("Адрес: "), input("Состав семьи: ")))
                except TypeError:
                    print("Неверный ввод")
        self.conn.commit()
        zap = "select * from employees;"
        self.cursor.execute(zap)
        k = self.cursor.fetchall()
        print(k)
        self.cursor.close()
        self.conn.close()

    def faces(self):
        creattab = "create table IF NOT EXISTS faces(id INTEGER PRIMARY KEY autoincrement, 'number criminal case' int, " \
                   "'person (first and last name)' text,'registration number of person' int, 'address' text, " \
                   "'num convictions', 'fingerprint cipher' int, 'status of a person' text);"
        self.cursor.execute(creattab)
        self.conn.commit()
        tabl = "insert into employees('number criminal case', 'person (first and last name)', " \
               "'registration number of person', 'address', 'num convictions', 'fingerprint cipher', " \
               "'status of a person') values (?, ?, ?, ?, ?, ?, ?);"
        while True:
            exit1 = input("Для завершения введите 'д' ")
            if exit1 == "д":
                break
            else:
                try:
                    self.cursor.execute(tabl, (randint(1000000, 9999999), input("ФИО сотрудника: "),
                                               input("Звание: "), input("Адрес: "), input("Состав семьи: ")))
                except TypeError:
                    print("Неверный ввод")

        self.conn.commit()
        zap = "select * from employees;"
        self.cursor.execute(zap)
        k = self.cursor.fetchall()
        print(k)
        self.cursor.close()
        self.conn.close()

    def incident(self):
        creattab = "create table IF NOT EXISTS IncidentDB(id INTEGER PRIMARY KEY autoincrement, 'registration number' "\
                   "int, 'date of registration' int, 'type event' text, 'source messages' text, " \
                   "'registration criminal case' text, 'number criminal case' int, 'number of the operation' int, " \
                   "'registration number of the employee' int, 'the scene of the incident' text, " \
                   "'a brief description of the incident' text);"
        self.cursor.execute(creattab)
        self.conn.commit()
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
                    self.cursor.execute(tabl1, (randint(1000000, 9999999),
                                                datetime.date(randint(2001, 2022), randint(1, 12), randint(1, 31)),
                                                input("Тип происшествия: "), input("Источник сообщения: "),
                                                input("Уголовное дело(да, нет): "), "-",
                                                int(input("Регистрационный номер сообщения: ")),
                                                input("Регистрационный номер сотрудника: "),
                                                input("Место происшествия: "), input("Краткое описание происшествия:")))
                    self.conn.commit()
                    zap2 = "select * from IncidentDB;"
                    self.cursor.execute(zap2)
                    k = self.cursor.fetchall()
                    print(k)
                    if k[5] == "да":
                        zap2 = "insert into IncidentDB('registration criminal case') values(?);"
                        self.cursor.execute(zap2, ())
                        self.conn.commit()
                except TypeError:
                    print("Неверный ввод")
        zap = "select * from employees;"
        self.cursor.execute(zap)
        k1 = self.cursor.fetchall()
        print(k1)
        self.cursor.close()
        self.conn.close()


base = IncidentDatabase()
base.incident()
