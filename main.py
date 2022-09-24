import sqlite3
from random import *
import datetime


class IncidentDatabase:
    def __init__(self):
        pass

    # сделано
    def bases(self):
        conn = sqlite3.connect(r"IncidentDB.db")
        cursor = conn.cursor()
        # creattab1 = "create table IF NOT EXISTS employees(id INTEGER PRIMARY KEY autoincrement, " \
        #             "'registration num of the certificate' int, 'full name' text, 'title' text, 'address' text, " \
        #             "'family composition' text);"
        # cursor.execute(creattab1)
        # conn.commit()
        # tabl = "insert into employees('registration num of the certificate', 'full name', 'title', " \
        #        "'address', 'family composition') values (?, ?, ?, ?, ?);"
        # while True:
        #     exit1 = input("Для завершения введите 'д' ")
        #     if exit1 == "д":
        #         break
        #     else:
        #         try:
        #             cursor.execute(tabl, (randint(1000000, 9999999), input("ФИО сотрудника: "),
        #                                        input("Звание: "), input("Адрес: "), input("Состав семьи: ")))
        #         except TypeError:
        #             print("Неверный ввод")
        # conn.commit()
        #
        # creattab3 = "create table IF NOT EXISTS IncidentDB(id INTEGER PRIMARY KEY autoincrement, 'registration number'" \
        #             " int, 'date of registration' int, 'type event' text, 'source messages' text, " \
        #             "'registration criminal case' text, 'number criminal case' int, 'number of the operation' int, " \
        #             "'registration number of the employee' int, 'the scene of the incident' text, " \
        #             "'a brief description of the incident' text);"
        # cursor.execute(creattab3)
        # conn.commit()
        # tabl1 = "insert into IncidentDB('registration number', 'date of registration', 'type event', " \
        #         "'source messages', 'registration criminal case', 'number criminal case', 'number of the operation', " \
        #         "'registration number of the employee', 'the scene of the incident', " \
        #         "'a brief description of the incident') values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        # while True:
        #     exit1 = input("Для завершения введите 'д' ")
        #     if exit1 == "д":
        #         break
        #     else:
        #         try:
        #             cursor.execute(tabl1, (randint(1000000, 9999999),
        #                                    datetime.date(randint(2001, 2022), randint(1, 12), randint(1, 31)),
        #                                    input("Тип происшествия 1: "), input("Источник сообщения 2: "),
        #                                    input("Уголовное дело(да, нет) 3: "), 0,
        #                                    int(input("Регистрационный номер сообщения 4: ")), 0,
        #                                    input("Место происшествия 5: "),
        #                                    input("Краткое описание происшествия 6: ")))
        #         except TypeError:
        #             print("Неверный ввод")
        # conn.commit()
        #
        # creattab2 = "create table IF NOT EXISTS faces(id INTEGER PRIMARY KEY autoincrement, 'number criminal case' int, " \
        #             "'person (first and last name)' text,'registration number of person' int, 'address' text, " \
        #             "'num convictions' int, 'fingerprint cipher' text, 'status of a person' text);"
        # cursor.execute(creattab2)
        # conn.commit()
        # tabl = "insert into faces('number criminal case', 'person (first and last name)', " \
        #        "'registration number of person', 'address', 'num convictions', 'fingerprint cipher', " \
        #        "'status of a person') values (?, ?, ?, ?, ?, ?, ?);"
        # while True:
        #     exit1 = input("Для завершения введите 'д' ")
        #     if exit1 == "д":
        #         break
        #     else:
        #         try:
        #             cursor.execute(tabl, (0, input("ФИО гражданина: "), int(input("Регистрационный номер лица: ")),
        #                                   input("Адрес: "), int(input("Количество судимостей: ")),
        #                                   input("Шифр отпечатков пальцев: "),
        #                                   input("Статус гражданина в происшествии: ")))
        #         except TypeError:
        #             print("Неверный ввод")
        # conn.commit()

        zap3 = "select * from IncidentDB;"
        cursor.execute(zap3)
        k = cursor.fetchall()
        ind = 0
        for i in k:
            for j in i:
                if j == "да" and i[6] == 0:
                    sql_up = f"UPDATE IncidentDB set 'number criminal case'=? where id=?;"
                    data = (randint(1000000, 9999999), i[0])
                    cursor.execute(sql_up, data)
                if j == i[8] and i[8] == 0:
                    zap4 = "select * from employees;"
                    cursor.execute(zap4)
                    k1 = cursor.fetchall()
                    sql_up = f"UPDATE IncidentDB set 'registration number of the employee'=? where id=?;"
                    data = (k1[ind][1], i[0])
                    cursor.execute(sql_up, data)
                    conn.commit()
                    ind += 1
                    if ind > len(k1):
                        ind = 0
        conn.commit()
        zap5 = "select * from IncidentDB;"
        cursor.execute(zap5)
        k2 = cursor.fetchall()
        ind = 0
        for t in k2:
            for g in t:
                zap6 = "select * from faces;"
                cursor.execute(zap6)
                k3 = cursor.fetchall()
                if g == t[6] and t[6] != 0:
                    for r in k3:
                        for h in r:
                            if h == 0:
                                sql_up = f"UPDATE faces set 'number criminal case'=? where id=?;"
                                data = (g, r[1])
                                cursor.execute(sql_up, data)
                                conn.commit()
                                ind += 1
                                if ind > len(k3):
                                    ind = 0

        conn.commit()
        cursor.close()
        conn.close()


base = IncidentDatabase()
base.bases()
