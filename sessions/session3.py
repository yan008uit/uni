
#MySQL connector må være installert
#Kommando i terminalvindu: pip install mysql-connector-python

from flask import Flask, render_template, request, redirect, session
from UserRegister import UserReg
from user import User
import secrets

app = Flask(__name__)

@app.route('/')

def hello() -> 'html':
    return render_template('login.html')

@app.route('/hemmelig')

def hemmelig() -> 'html':
    if 'logged_in' in session:
        return render_template('velkommen1.html', the_title='Beskyttet side')
    session1 = session
    return render_template('login.html')

@app.route('/login', methods=["GET", "POST"])

def login() -> 'html':
    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']
        if User.login(username, password):
            session['logged_in'] = True
            session['username'] = username
        return redirect('/')

@app.route('/logout', methods=["GET", "POST"])

def logout() -> 'html':
        session.pop('logged_in')
        return redirect('/')

app.secret_key = secrets.token_urlsafe(16)

if __name__ == "__main__":
    app.run(debug=True)
