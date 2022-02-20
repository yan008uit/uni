
#MySQL connector må være installert
#Kommando i terminalvindu: pip install mysql-connector-python

from flask import Flask, render_template
from MyDb import MyDb

app = Flask(__name__)

@app.route('/')

def hello() -> 'html':

    with MyDb() as db:
        _SQL = """SELECT id, givenName, lastName, email, studyProgram FROM student_v21""";
        result = db.query(_SQL)
    return render_template('students.html',
                           students= result)

if __name__ == "__main__":
    app.run(debug=True)
