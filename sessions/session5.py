# MySQL connector må være installert
# Kommando i terminalvindu: pip install -r requirements.txt

from flask import Flask, render_template, request, redirect, session, url_for
import secrets
from flask_login import LoginManager, current_user, login_user, logout_user
from user import User
from UserRegister import UserReg
from flask_login import login_required

app = Flask(__name__)
# ...
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user_dict = session['user']
    user = User(user_dict['id'], user_dict['passwordHash'], user_dict['firstname'], user_dict['lastname'], user_dict['username'])
    user.is_authenticated = user_dict['is_authenticated']
    return user


@app.route('/hemmelig')
@login_required
def hemmelig() -> 'html':
    return render_template('velkommen.html', the_title='Beskyttet side')


@app.route('/')
@app.route('/index')
# @login_required
def hello() -> 'html':
    return render_template('login.html')


@app.route('/login', methods=["GET", "POST"])
def hello2() -> 'html':
    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']
        with UserReg() as db:
            usr = db.getUser(username)
            if usr:
                user = User(*usr)
                if user.check_password(password):       
                    user.is_authenticated = True
                    login_user(user)
                    session['user'] = user.__dict__
                    session['logged_in'] = True
                    session['username'] = username
                    return redirect(url_for('hemmelig'))
            else:
                return redirect('/')


@app.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    session.pop('logged_in')
    return redirect('/')


app.secret_key = secrets.token_urlsafe(16)

if __name__ == "__main__":
    app.run(debug=True)
