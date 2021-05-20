import mysql.connector

class DBconnect:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='root', database='supermarket')
        self.cur = self.connection.cursor()

    def insert(self, query, values):
        self.cur.execute(query, values)
        self.connection.commit()


    def select(self, query):
        self.cur.execute(query)
        rows=self.cur.fetchall()
        return rows


    def update(self, query, values):
        self.cur.execute(query, values)
        self.connection.commit()
    def delete(self, query, value):
        self.cur.execute(query, value)
        self.connection.commit()

    def select2(self, query, value=''):
        self.cur.execute(query, value)
        rows=self.cur.fetchall()
        return rows
    def __del__(self):
        self.connection.close()
