import sqlite3
from random import *
import datetime


class IncidentDatabase:
    def __init__(self):
        pass

    @staticmethod
    def bases():
        conn = sqlite3.connect(r"IncidentDB.db")
        cursor = conn.cursor()
        creattab1 = "create table IF NOT EXISTS employees(id INTEGER PRIMARY KEY autoincrement, " \
                    "registration_num_of_the_certificate int, full_name text, title text, address text, " \
                    "family_composition text);"
        cursor.execute(creattab1)
        conn.commit()
        tabl = "insert into employees(registration_num_of_the_certificate, full_name, title, " \
               "address, family_composition) values (?, ?, ?, ?, ?);"
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

        creattab3 = "create table IF NOT EXISTS IncidentDB(id INTEGER PRIMARY KEY autoincrement, registration_number" \
                    " int, date_of_registration int, type_event text, source_messages text, " \
                    "registration_criminal_case text, number_criminal_case int, number_of_the_operation int, " \
                    "registration_number_of_the_employee int, the_scene_of_the_incident text, " \
                    "a_brief_description_of_the_incident text);"
        cursor.execute(creattab3)
        conn.commit()
        tabl1 = "insert into IncidentDB(registration_number, date_of_registration, type_event, " \
                "source_messages, registration_criminal_case, number_criminal_case, number_of_the_operation, " \
                "registration_number_of_the_employee, the_scene_of_the_incident, " \
                "a_brief_description_of_the_incident) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
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
                                           int(input("Регистрационный номер сообщения: ")), 0,
                                           input("Место происшествия: "),
                                           input("Краткое описание происшествия: ")))
                except TypeError:
                    print("Неверный ввод")
        conn.commit()

        creattab2 = "create table IF NOT EXISTS faces(id INTEGER PRIMARY KEY autoincrement, number_criminal_case int, " \
                    "person text,registration_number_of_person int, address text, " \
                    "num_convictions int, fingerprint_cipher text, status_of_a_person text);"
        cursor.execute(creattab2)
        conn.commit()
        tabl = "insert into faces(number_criminal_case, person, " \
               "registration_number_of_person, address, num_convictions, fingerprint_cipher, " \
               "status_of_a_person) values (?, ?, ?, ?, ?, ?, ?);"
        while True:
            exit1 = input("Для завершения введите 'д' ")
            if exit1 == "д":
                break
            else:
                try:
                    cursor.execute(tabl, (0, input("ФИО гражданина: "), int(input("Регистрационный номер лица: ")),
                                          input("Адрес: "), int(input("Количество судимостей: ")),
                                          input("Шифр отпечатков пальцев: "),
                                          input("Статус гражданина в происшествии: ")))
                except TypeError:
                    print("Неверный ввод")
        conn.commit()

        zap3 = "select * from IncidentDB;"
        cursor.execute(zap3)
        k = cursor.fetchall()
        ind = 0
        for i in k:
            if i[5] == "да" and i[6] == 0:
                sql_up = f"UPDATE IncidentDB set number_criminal_case=? where id=?;"
                data = (randint(1000000, 9999999), i[0])
                cursor.execute(sql_up, data)
            if i[8] == 0:
                zap4 = "select * from employees;"
                cursor.execute(zap4)
                k1 = cursor.fetchall()
                if ind >= len(k1):
                    ind = 0
                sql_up = f"UPDATE IncidentDB set registration_number_of_the_employee=? where id=?;"
                data = (k1[ind][1], i[0])
                cursor.execute(sql_up, data)
                conn.commit()
                ind += 1

        conn.commit()
        zap5 = "select * from faces;"
        cursor.execute(zap5)
        k2 = cursor.fetchall()
        ind = 0
        for t in k2:
            for d in t:
                zap6 = "select * from IncidentDB;"
                cursor.execute(zap6)
                k3 = cursor.fetchall()
                if ind >= len(k3):
                    ind = 0
                if k3[ind][5] == "да" and d == 0:
                    sql_up = "UPDATE faces set number_criminal_case=? where id=?;"
                    cursor.execute(sql_up, (k3[ind][6], 1))
                    conn.commit()
                    ind += 1
        conn.commit()
        zap7 = "select * from faces;"
        cursor.execute(zap7)
        k4 = cursor.fetchall()
        print(k4)
        conn.commit()
        cursor.close()
        conn.close()


base = IncidentDatabase()
base.bases()
