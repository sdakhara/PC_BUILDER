from flask import Flask, render_template

app = Flask(__name__)


# User Routes
@app.route('/')
def index():
    return render_template('User/index.html')


if __name__ == '__main__':
    app.run(debug=True)
