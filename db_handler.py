# db_handler.py
import sqlite3

con = sqlite3.connect("data/abitur-automation.sql")
cur = con.cursor()


def fetch_abiturfach_kombination(kurse_kombi):
    sql = """SELECT kombination_id FROM tbl_abiturfach_kombination 
    WHERE abiturfach_1=? AND abiturfach_2=? AND abiturfach_3=? AND abiturfach_4=?"""
    cur.execute(sql, kurse_kombi)

    return cur.fetchone()[0]


def add_kurs(attributes):
    sql = "INSERT INTO tbl_kurs (None, ?, ?, ?, ?)"
    cur.execute(sql, attributes)


def add_student(attributes):
    sql = "INSERT INTO tbl_schueler (None, ?, ?, ?, ?, ?)"
    cur.execute(sql, attributes)


def add_kursbelegung(student_id, course_id):
    sql = "INSERT INTO tbl_kurs_belegung (None, ?, ?, None, None, None, None, None)"
    cur.execute(sql, (student_id, course_id))


def update_kursbelegung(points, student_id, course_id):
    sql = """UPDATE tbl_kurs_belegung 
    SET punkte_12_1=?, punkte_12_2=?, punkte_13_1=?, punkte_13_2=? WHERE schueler_id=? AND course_id=?"""
    cur.execute(sql, points + (student_id, course_id))
