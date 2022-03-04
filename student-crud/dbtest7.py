
#Install all requirements: pip install -r requirements.txt

from flask import Flask, render_template, request, redirect
from StudentRegister import StudReg
from student import Student
from StudentForm import StudentForm

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])

def hello() -> 'html':
    id = request.args.get('id')
    if not id:
        with StudReg() as db:
            result = db.getAll()
        students = [Student(*x) for x in result]
        return render_template('students3.html',
                               students=students)
    else:
        with StudReg() as db:
            stud = db.getStudent(id)
            if stud is None:
                return render_template('error.html',
                                       msg='Invalid parameter')
            else:
                student = Student(*stud)
                form = StudentForm()
                form.id=id
                form.lastName.data = student.lastName
                form.givenName.data = student.givenName
                form.email.data = student.email
                form.studyProgram.data = student.studyProgram
                return render_template('students7.html',
                                       form=form)

@app.route('/update', methods=["GET", "POST"])

def hello2() -> 'html':
    form = StudentForm(request.form)
    if request.method == "POST" and form.validate():

        id = request.form['id']
        givenName = form.givenName.data
        lastName = form.lastName.data
        email = form.email.data
        studyProgram = form.studyProgram.data
        student = (givenName, lastName, email, studyProgram,id)
        with StudReg() as db:
            result = db.updateStudent(student)
        return redirect('/')
    else:
        return render_template('students7.html',
                               form=form)

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
                              student=stud, deleteConfirmation=True)

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
