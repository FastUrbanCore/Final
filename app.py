from flask import Flask,render_template,request,redirect
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.id} - {self.email}"

@app.route("/")
def index():
    users = User.query.all()
    return render_template('index.html', users=users)
    # return render_template("index.html")
    # return "Saad Mehmood!"

@app.route("/home")
def home():
    return "22i-1655!"

@app.route('/add', methods=['POST'])
def add():
    email = request.form['email']
    password = request.form['password']
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)