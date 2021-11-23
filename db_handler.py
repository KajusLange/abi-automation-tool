# db_handler.py
import sqlite3

con = sqlite3.connect("data/abitur-automation.sql")
cur = con.cursor()


def fetch_abiturfach_kombination(kurse_kombi):
    sql = """SELECT kombination_id FROM tbl_abiturfach_kombination 
    WHERE abiturfach_1=? AND abiturfach_2=? AND abiturfach_3=? AND abiturfach_4=?"""

    cur.execute(sql, kurse_kombi)

    return cur.fetchone()[0]


