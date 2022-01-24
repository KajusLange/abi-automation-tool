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
    sql = "INSERT INTO tbl_kurs VALUES (NULL, ?, ?, ?, ?)"
    cur.execute(sql, attributes)


def fetch_kurse():
    sql = "SELECT kurs_id, bezeichnung FROM tbl_kurs"
    cur.execute(sql)
    return cur.fetchall()


def add_student(attributes):
    sql = "INSERT INTO tbl_schueler VALUES (NULL, ?, ?, ?, ?, ?, ?)"
    cur.execute(sql, attributes)


def add_kursbelegung(course_id, student_id):
    sql = "INSERT INTO tbl_kursbelegung VALUES (?, ?, NULL, NULL, NULL, NULL, NULL, NULL, NULL)"
    cur.execute(sql, (course_id, student_id))


def update_kursbelegung(abiturfach, points, student_id, course_id):
    sql = """UPDATE tbl_kursbelegung 
        SET abiturfach=?, punkte_12_1=?, punkte_12_2=?, punkte_13_1=?, punkte_13_2=?,
            punkte_pruefung=?, punkte_nachpruefung=?
        WHERE kurs_id=? AND student_id=?"""
    cur.execute(sql, (abiturfach,) + points + (student_id, course_id))


def add_kursbelegung_template(name, kurs_id):
    sql = "INSERT INTO tbl_kursbelegung_template VALUES(?, ?)"
    cur.execute(sql, (name, kurs_id))


def fetch_kursbelegung_template(name):
    sql = "SELECT kurs_id FROM tbl_kursbelegung_template WHERE template_name=?"
    cur.execute(sql, (name,))
    return cur.fetchall()


def fetch_student_kursbelegung_group_size(student_id):
    sql = """SELECT COUNT(tkb.kurs_id) FROM tbl_kursbelegung AS tkb
        INNER JOIN tbl_kurs AS tk ON tk.kurs_id = tkb.kurs_id
        WHERE tkb.student_id=? GROUP BY tk.aufgabenfeld"""
    cur.execute(sql, (student_id,))
    return cur.fetchall()
