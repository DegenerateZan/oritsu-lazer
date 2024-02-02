import mysql.connector
from helpers.ENV import ENV

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = ENV.get(ENV.DB_HOST),
                user = ENV.get(ENV.DB_USER),
                password = ENV.get(ENV.DB_PASSWORD),
                database = ENV.get(ENV.DB_DATABASE)
            )
            print("Connected to the database")
        except mysql.connector.Error as error:
            print("Failed to connect to the database:", error)

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connection closed")
    
    def execute(self, query, values=None):
        cursor = self.connection.cursor(buffered=True)
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        self.connection.commit()
        return cursor
    
    def fetch(self, query, values=None):
        cursor = self.execute(query, values)
        return cursor.fetchall()
    
    def fetch_one(self, query, values=None):
        cursor = self.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        return result

db = Database()
db.connect()