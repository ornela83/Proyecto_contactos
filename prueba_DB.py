import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='usuarios'
        )

        self.cursor = self.connection.cursor()

        print("Conexión establecida exitosamente")

    def select_user(self, id):
        sql = 'SELECT id, username, email FROM users WHERE id = {}'.format(id)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id:", user[0])
            print("Username:", user[1]) #en la segunda columna
            print("Email:", user[2])

        except Exception as e:
            raise


database = DataBase()
database.select_user(1)