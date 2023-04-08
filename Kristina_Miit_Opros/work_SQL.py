import sqlite3

conn = sqlite3.connect(r'data/answers_and_usersV3.1.db')
cur = conn.cursor()

request = '''CREATE TABLE IF NOT EXISTS answers(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    userid INT ,
    question INT,
    answer TEXT);
'''
cur.execute(request)
conn.commit()

def add_answer(userid:int, question:int, answer:str, conn, cur) -> None:
    request_add = f'''INSERT INTO answers(userid, question, answer)
        VALUES('{userid}', '{question}', '{answer}');'''
    cur.execute(request_add)
    conn.commit()
