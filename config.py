import sqlite3

options = {}


def session():
    return sqlite3.connect('guestbook.db', detect_types=sqlite3.PARSE_DECLTYPES)