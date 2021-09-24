from flask import url_for, redirect, Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        return {"name": self.name,
                "email": self.email}

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)


@app.route('/')
def home_page():
    return render_template("index.html", current=0)


@app.route("/login", methods=['POST', 'GET'])
def login_page():
    if request.method == "POST":
        data = request.form.to_dict()
        user = db.session.query(db.exists().where(User.username == 'admin')).scalar()
        print(user)
        if user:
            login_user(user)
            return f"logged in {data['username']} with {data['password']}"
    else:
        return render_template("login.html")


@app.route("/send_complaint")
@login_required
def complaint_page():
    return "Secure"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True, threaded=True)
