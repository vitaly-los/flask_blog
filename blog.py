from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import User, Post


app = Flask(__name__)

app.config['SECRET_KEY'] = '435klf44l60sqqer'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead
# and will be disabled by default in the future
# Set it to True to suppress this warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

posts = [
    {
        'author': 'Los vitaly',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 10, 2019'
    },
    {
        'author': 'User',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 10, 2019'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About us')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' \
                and form.password.data == 'pass':
            flash('You logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unseccess', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
