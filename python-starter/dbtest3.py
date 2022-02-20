
#MySQL connector må være installert
#Kommando i terminalvindu: pip install mysql-connector-python

from flask import Flask, render_template
from StudentRegister import StudReg
from student import Student

app = Flask(__name__)

@app.route('/')

def hello() -> 'html':

    with StudReg() as db:
        result = db.visAlle()
    students = [Student(*x) for x in result]
    return render_template('students2.html',
                           students= students)

if __name__ == "__main__":
    app.run(debug=True)
