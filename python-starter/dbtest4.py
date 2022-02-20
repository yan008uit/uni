
#MySQL connector må være installert
#Kommando i terminalvindu: pip install mysql-connector-python

from flask import Flask, render_template, request
from StudentRegister import StudReg
from student import Student

app = Flask(__name__)

@app.route('/')

def hello() -> 'html':

    # if key doesn't exist, returns a 400, bad request error
    #framework = request.args['framework']

    # if key doesn't exist, returns None
    id = request.args.get('id')
    if not id:
        with StudReg() as db:
            result = db.visAlle()
        students = [Student(*x) for x in result]
        return render_template('students3.html',
                               students= students)
    else:
        with StudReg() as db:
            student=Student(*db.visStudent(id))
        return render_template('students3.html',
                               student= student)
if __name__ == "__main__":
    app.run(debug=True)
