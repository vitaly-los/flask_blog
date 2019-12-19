from flask import Flask, render_template, url_for
from forms import RegistrationFrom, LoginFrom
app = Flask(__name__)

app.config['SECRET_KEY'] = '435klf44l60sqqer'

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
def index():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About us')


if __name__ == "__main__":
    app.run(debug=True)
