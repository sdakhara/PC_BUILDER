from flask import Flask, render_template, request
from logics.user.autobuild import logic


app = Flask(__name__)

logic = logic()


# User Routes
@app.route('/')
def index():
    return render_template('User/index.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    budget = 0
    cpu = 0
    ram = 0
    hdd = 0
    if request.method == 'POST':
        budget = request.form.get('budget')
        cpu = request.form.get('CPU')
        ram = request.form.get('RAM')
        hdd = request.form.get('HDD')
    return render_template('User/testHTMLs/logictest.html', data=logic.buildpc(int(budget), bool(cpu), bool(ram), bool(hdd)))


if __name__ == '__main__':
    app.run(debug=True)
