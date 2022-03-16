
#MySQL connector må være installert
#Kommando i terminalvindu: pip install mysql-connector-python

from flask import Flask, render_template, request, redirect
from StudentRegister import StudReg
from student import Student

app = Flask(__name__)

@app.route('/')

def index() -> 'html':
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
        return render_template('students5.html',
                    student= student)

@app.route('/update', methods=["GET", "POST"])

def update() -> 'html':
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

@app.route('/delete_confirm')

def deleteConfirm() -> 'html':
    id = request.args.get('id')
    if not id:
        return render_template('error.html',
                               msg='Invalid parameter')
    else:
        with StudReg() as db:
            stud = db.getStudent(id)
            if stud is None:
                return render_template('error.html',
                                       msg='Invalid parameter')
            else:
                student = Student(*stud)
                return render_template('students6.html',
                              student=student, deleteConfirmation=True)

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
