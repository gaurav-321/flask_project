from flask import url_for, redirect, Flask, render_template, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)
app.config['TESTING'] = False
# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"


class User(UserMixin, db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/')
def home_page():
    return render_template("index.html", current=110)


@app.route("/login", methods=['POST', 'GET'])
def login_page():
    if request.method == "POST":
        data = request.form.to_dict()
        if "" not in list(data.values()):
            user = User.query.filter_by(username=data['username'], password=data['password']).first()
            if user is not None:
                print(user)
                login_user(user)
                print(user.is_active)
                return redirect("/send_complaint")
            else:
                flash("Incorrect Username or Password")
                return redirect("/login")
        else:
            flash("Fields Shouldn't Be empty")
            return redirect("/login")
    else:
        return render_template("login.html")


@app.route("/send_complaint")
@login_required
def complaint_page():
    flash("You are loggrd in", "information")
    return "Secure"


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True, threaded=True)
