from flask import Flask, render_template, jsonify, request, redirect, url_for

from logics.admin.IPLocation import get_ip
from logics.admin.datashare import datatransfer, Authentication

app = Flask(__name__)
dataapi = datatransfer()
verifier = Authentication()
# visitor counter

counter = 0


@app.before_request
def countVisitor():
    global counter
    counter += 1
    total = counter / 48
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


class globs:
    ADMIN = None


g = globs()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        data = verifier.verify(email, password)
        if data:
            g.ADMIN = data
            return redirect(url_for('dashboard'))

    return render_template('Admin/login.html')


@app.route('/logout')
def logout():
    g.ADMIN = None
    return redirect(url_for('home'))


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    dt = dataapi.getAllAdmin()
    last = dataapi.getLastLogin()
    buildedPC = dataapi.getCountBuildedPC()
    todaysbuild = dataapi.getTodayBuild()

    try:
        return render_template('Admin/index.html', adminname=g.ADMIN.AdminName, data=dt, last=last, buildedPC=buildedPC,
                               todaysbuild=todaysbuild)
    except:
        return redirect(url_for('home'))


@app.route('/adminregister', methods=['GET', 'POST'])
def adminregister():
    err = None
    if request.method == 'POST':
        adminname = request.form.get('adminname')
        adminemail = request.form.get('adminemail')
        adminphoneno = request.form.get('adminphoneno')
        adminpass = request.form.get('adminpass')
        adminconpass = request.form.get('adminconpass')
        currentpass = request.form.get('currentadminpass')
        if g.ADMIN.Password == currentpass:
            err = "wrong admin password"
            if adminpass == adminconpass:
                verifier.addAdmin(adminname, adminpass, adminemail, adminphoneno)
            else:
                err = "Password Didn't match"
    return render_template('Admin/addadmin.html', err=err)


@app.route('/messages')
def messages():
    return render_template('Admin/messages.html')


@app.route('/users')
def users():
    dt = dataapi.getAllUser()
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
