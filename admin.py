from flask import Flask, render_template, jsonify, request
from logics.admin.IPLocation import get_ip
from logics.admin.datashare import userdt

app = Flask(__name__)
usrdata = userdt()
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

# count build
"""
create = 0
@app.before_request
def countBuild():
    global create
    create = create + # pass variable to build button
    print()
"""

@app.route('/getip')
def getIP():
    country = get_ip(request.remote_addr)
    return jsonify(country)

@app.route('/')
def home():
    return render_template('Admin/index.html')


@app.route('/messages')
def messages():
    return render_template('Admin/messages.html')


@app.route('/users')
def users():
    dt = usrdata.getAllUser()
    return render_template('Admin/users.html', dt=dt)


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
