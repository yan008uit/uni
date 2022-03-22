# MySQL connector må være installert
# Kommando i terminalvindu: pip install -r requirements.txt

from site import venv
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
    with UserReg() as db:
        user = User(*db.getUserById(user_id))
    return user


@app.route('/hemmelig')
@login_required
def hemmelig() -> 'html':
    return render_template('velkommen2.html', the_title='Beskyttet side')


@app.route('/')
@app.route('/index')
# @login_required
def index() -> 'html':
    return render_template('login1.html')


@app.route('/login', methods=["GET", "POST"])
def login() -> 'html':
    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']
        with UserReg() as db:
            usr = db.getUser(username)
            if usr:
                user = User(*usr)
                if user.check_password(password):
                    login_user(user, remember=True)
            return redirect(url_for('index'))


@app.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


app.secret_key = secrets.token_urlsafe(16)

if __name__ == "__main__":
    app.run(debug=True)
