from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post


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
