from flask import Flask, render_template
# from logics.user.autobuild import logic


app = Flask(__name__)

# logic = logic()


# User Routes
@app.route('/')
def index():
    return render_template('User/index.html')


# @app.route('/test/<int:budget>')
# def test(budget):
#     return render_template('User/testHTMLs/logictest.html', data=logic.buildpc(budget))


if __name__ == '__main__':
    app.run(debug=True)
