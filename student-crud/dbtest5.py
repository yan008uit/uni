
#MySQL connector må være installert
#Kommando i terminalvindu: pip install mysql-connector-python

from flask import Flask, render_template, request, redirect
from StudentRegister import StudReg
from student import Student

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])

def hello() -> 'html':
    if request.method == "POST":
        req = request.form

        id = request.form['id']
        givenName = request.form['givenName']
        lastName = request.form['lastName']
        email = request.form.get('email')
        studyProgram = request.form.get('studyProgram')
        student = Student(id, givenName, lastName, email, studyProgram)
        with StudReg() as db:
            result = db.updateStudent(student)

    else:
        id = request.args.get('id')
        if not id:
            with StudReg() as db:
                result = db.getAll()
            students = [Student(*x) for x in result]
            return render_template('students3.html',
                                   students= students)
        else:
            with StudReg() as db:
                student=Student(*db.getStudent(id))
            return render_template('students4.html',
                                   student= student)

@app.route('/update', methods=["GET", "POST"])

def hello2() -> 'html':
    if request.method == "POST":
        req = request.form

        id = request.form['id']
        givenName = request.form['givenName']
        lastName = request.form['lastName']
        email = request.form.get('email')
        studyProgram = request.form.get('studyProgram')
        student = (givenName, lastName, email, studyProgram,id)
        with StudReg() as db:
            result = db.updateStudent(student)
        return redirect('/')

@app.route('/delete', methods=["GET", "POST"])

def delete() -> 'html':
    if request.method == "POST":
        req = request.form

        id = request.form['id']
        with StudReg() as db:
            result = db.deleteStudent(id)
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
