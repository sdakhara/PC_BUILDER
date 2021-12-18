from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# visitor counter

counter = 0
@app.before_request
def countVisitor():
    global counter
    counter += 1
    total = counter/48
    counterFile = open('counter.txt', 'w')
    counterFile.write(str(total))
    counterFile.close()



@app.route('/getip')
def getIP():
    return jsonify({"ip":request.remote_addr, 'user':request.remote_user})

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
    app.run(host= "0.0.0.0")
