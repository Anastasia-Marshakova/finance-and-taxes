from flask import Flask, render_template, request
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PythonProject1.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

@app.route('/')
@app.route('/index')# Декоратор для гравной страницы
def index():
    return render_template('index.html')  # файл index.html должен быть в папке templates


@app.route('/about')# Декоратор для аторичных страниц
def about():
    return render_template('about.html')  # создайте about.html в templates


@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        print(request.form['project_name'])
        print(request.form['at_work'])
        print(request.form['deadline'])
        print(request.form['composition_genre'])
        print(request.form['composition'])
        print(request.form['project_status'])
        print(request.form['clip'])
    else:
        return render_template('create.html')# файл index.html должен быть в папке templates


if __name__ == "__main__":
    app.run(debug=True)