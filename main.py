import sqlite3
connection = sqlite3.connect('test_db.sqlite') # отрыть соеденение с БД, создаст файл если его нет
cursor=connection.cursor() #обьект БД с помощью которого можем удалять.добавлять вся работа с ним
#-юсерз это название таблицы, потом перечисляются название столбцов
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (  
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')
# cursor.execute("INSERT INTO users (name, email) VALUES ('Иванов Иван', 'ivanov@gmail.com')") #вставляем в таблицу вариант 1
# cursor.execute("INSERT INTO users (name, email) VALUES ('Петров Пётр', 'petrov@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Сидоров Сидор', 'sidorov@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Пупкин Вася', 'pupkin@gmail.com')")
#
# cursor.executescript('''
# INSERT INTO users (name, email) VALUES ('John Doe', 'doe@gmail.com');
# INSERT INTO users (name, email) VALUES ('Nick Sand', 'sand@gmail.com');
#  ''')  #вариант 2
#
# users = [
#     ('User 1', 'user1@gmail.com'),
#     ('User 2', 'user2@gmail.com'),
#     ('User 3', 'user3@gmail.com'),
# ]
# cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)    # от юскерс до этой строки вариант 3
# connection.commit() # сохраняем изменения
cursor.execute("SELECT * FROM users") # выбирате все из юсерс, всемто * модно поставить name или emale
#res = cursor.fetchall() #забрать результат собирает адреса где лежит инфо, при повторном запске адресов уже нет, предыдущий res надо комментировать
# res1= cursor.fetchone() #забрать 1 стороку
# print(res1)

email = 'petrov@gmail.com'
#cursor.execute(f"SELECT * FROM users WHERE email = '{email}'") # нельзя использовать тк емайл не проверить и мб иньекция
cursor.execute("SELECT * FROM users WHERE email = ?", (email,)) # емайл передается в кортеже главная тут запятая
cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email, 'name': 'John Doe'}) # передаем в словаре
res=cursor.fetchone()
print(res)
connection.close()

