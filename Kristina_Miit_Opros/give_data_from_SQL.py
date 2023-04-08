import sqlite3


user_id = set()
dict_answer = {}

def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('data/answers_and_usersV3.1.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from answers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))

        for row in records:
            user_id.add(row[1])
            dict_answer[row[2]] = dict_answer.get(row[2], [])
            dict_answer[row[2]].append(row[3])
            # print("ID: ", row[0])
            # print("User_ID: ", row[1])
            # print("Вопрос №: ", row[2])
            # print("Ответ: ", row[3], end="\n\n")
        cursor.close()
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)




read_sqlite_table()
for i in user_id:
    print(f'User_id: {i}')
print(f'Всего {len(user_id)} прошли опрос')
for key in dict_answer:
    if key == 0:
        continue
    print(f'Вопрос: {key} ---> Ответы: {dict_answer[key]}')