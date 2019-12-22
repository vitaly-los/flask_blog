from app import app
from flask import render_template


@app.route('/')
def index():
    user = 'Username'
    return render_template('index.html', u=user)
