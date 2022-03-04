import mysql.connector
from mysql.connector import errorcode

class StudReg:

    def __init__(self) -> None:

        dbconfig = {'host': '127.0.0.1',
                    'user': 'user',
                    'password': 'test',
                    'database': 'myDb', }

        self.configuration = dbconfig

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor(prepared=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def getAll(self):
        try:
            self.cursor.execute("SELECT * FROM student ORDER BY lastName ASC")
            result = self.cursor.fetchall()
        except mysql.connector.Error as err:
                print(err)
        return result

    def getStudent(self, id):
        try:
            self.cursor.execute("SELECT * FROM student WHERE  id=(%s)", (id,))
            result = self.cursor.fetchone()
        except mysql.connector.Error as err:
                print(err)
        return result

    def deleteStudent(self, id):
        try:
            self.cursor.execute("DELETE FROM student WHERE  id=(%s)", (id,))
        except mysql.connector.Error as err:
                print(err)

    def updateStudent(self, student):
        try:
            sql1 = '''UPDATE 
                student 
            SET 
                givenName = %s, lastName = %s, email = %s, studyProgram = %s
            WHERE
                id = %s'''
            self.cursor.execute(sql1, student)
        except mysql.connector.Error as err:
                print(err)
