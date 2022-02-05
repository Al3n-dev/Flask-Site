from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///alcompany.db'
db = SQLAlchemy(app)


# class Item(db.Model):
#    id = db.Column(db.Integer,primary_key=True)
#    email = db.Column(db.String(100), nullable-False)
#    fulname =
#    number = 0
#    comment = 0


@app.route('/')
def index():
    return render_template('index.html')  # подключаем html из templates


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/blog-single')
def blog_single():
    return render_template('blog-single.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
