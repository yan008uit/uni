from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# ...
#from app import login
from student import Student
from StudentRegister import StudReg


# ...

@login.user_loader
def load_user(id):
    with StudReg() as db:
        student = Student(*db.getStudent(id))
    return student


class User(UserMixin):
    # ...
    def __init__(self, db) -> None:
        self.__db = db

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
