from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Start Blog'


@app.route('/about')
def about():
    return 'About page'


if __name__ == "__main__":
    app.run(debug=True)