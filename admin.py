from flask import Flask, render_template

app = Flask(__name__)

counter = 1
@app.before_request
def countVisitor():
    global counter
    counter +=1
    counterFile = open('counter.txt', 'w')
    counterFile.write(str(counter))
    counterFile.close()


@app.route('/')
def home():
    return render_template('Admin/index.html')


@app.route('/messages')
def messages():
    return render_template('Admin/messages.html')


@app.route('/users')
def users():
    return render_template('Admin/users.html')


@app.route('/inventory')
def inventory():
    return render_template('Admin/inventory.html')


@app.route('/statistics')
def statistics():
    return render_template('Admin/statistics.html')


@app.route('/system')
def system():
    return render_template('Admin/system.html')


if __name__ == '__main__':
    app.run(debug=True)
