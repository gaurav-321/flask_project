from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)


db.session.add(User(username="admin", password="admin"))
db.session.commit()
print(db.session.query(db.exists().where(User.username == 'admin').w, User.password == "admin")).scalar())
users = User.query.all()
print(users.Objects)
