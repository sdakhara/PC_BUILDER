from datetime import date
from flask_session import Session

from flask import Flask, render_template, jsonify, request, redirect, url_for

from logics.admin.IPLocation import get_ip
from logics.admin.datashare import datatransfer, Authentication


class globs:
    ADMIN = None


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
dataapi = datatransfer()
Authenticator = Authentication()
g = globs()


@app.route('/getip')
def getIP():
    country = get_ip(request.remote_addr)
    return jsonify(country)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        data = Authenticator.verifyadmin(email, password)
        if data:
            g.ADMIN = data
            return redirect(url_for('dashboard'))

    return render_template('admin/login.html')


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
    totvisit = dataapi.getTotVisit()
    todayvisit = dataapi.getTodayVisit()
    msgs = dataapi.getMessages()
    countrys = dataapi.getcountrydata()
    try:
        return render_template('admin/index.html', adminname=g.ADMIN.AdminName, data=dt, last=last, buildedPC=buildedPC,
                               todaysbuild=todaysbuild, adminrole=g.ADMIN.Role, totvisitor=totvisit,
                               todaysvisit=todayvisit, countrys=countrys,
                               date=date.today(), msgs=msgs)
    except:
        return redirect(url_for('home'))


@app.route('/adminregister', methods=['GET', 'POST'])
def adminregister():
    err = None
    try:
        if request.method == 'POST':
            adminname = request.form.get('adminname')
            adminemail = request.form.get('adminemail')
            adminphoneno = request.form.get('adminphoneno')
            adminpass = request.form.get('adminpass')
            adminconpass = request.form.get('adminconpass')
            currentpass = request.form.get('currentadminpass')
            if g.ADMIN.Password == currentpass:
                if adminpass == adminconpass:
                    Authenticator.addAdmin(adminname, adminpass, adminemail, adminphoneno)
                    return redirect(url_for('dashboard'))
                else:
                    err = "Password Didn't match"
            else:
                err = "wrong admin password"
        return render_template('admin/addadmin.html', err=err)
    except:
        return redirect(url_for('home'))


@app.route('/messages')
def messages():
    return render_template('admin/messages.html')


@app.route('/users', methods=['GET', 'POST'])
def users():
    dt = dataapi.getAllUser()
    if request.method == 'POST':
        name = request.form.get('requesteduser')
        dt = dataapi.srchusrname(name)
    return render_template('admin/users.html', dt=dt)


@app.route('/usermodify/<userid>', methods=['GET', 'POST'])
def usermodify(userid):
    dt = dataapi.srchusrid(userid)
    return render_template('admin/usermodify.html', dt=dt)


@app.route('/usermodify/<userid>/<username>', methods=['GET', 'POST'])
def usermodifyreq(userid, username):
    if request.method == 'POST':
        isDelete = bool(request.form.get('delete'))
        isCancel = bool(request.form.get('cancel'))
        usrname = request.form.get('username')
        usremail = request.form.get('useremail')
        usrphone = request.form.get('userphone')
        usrpass = request.form.get('userpass')
        if isDelete:
            Authenticator.deleteUser(userid)
            return redirect(url_for('users'))
        if isCancel:
            return redirect(url_for('users'))

        Authenticator.updateUser(userid, usrname, usrphone, usremail, usrpass)
        return redirect(url_for('users'))

    dt = dataapi.srchusrid(userid)
    return render_template('admin/usermodify.html', dt=dt)


@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    component = None
    req = None
    if request.method == 'POST':
        cpu = request.form.get('cpu')
        gpu = request.form.get('gpu')
        board = request.form.get('board')
        ram = request.form.get('ram')
        cooler = request.form.get('cooler')
        storage = request.form.get('storage')
        cabinet = request.form.get('cabinet')
        psu = request.form.get('psu')
        if cpu == 'cpu':
            req = 'cpu'
            component = dataapi.getCPUs()
        if gpu == 'gpu':
            req = 'gpu'
            component = dataapi.getGPUs()
        if ram == 'ram':
            req = 'ram'
            component = dataapi.getRAMs()
        if board == 'board':
            req = 'board'
            component = dataapi.getBOARDs()
        if cooler == 'cooler':
            req = 'cooler'
            component = dataapi.getCOOLERs()
        if storage == 'storage':
            req = 'storage'
            component = dataapi.getSTORAGEs()
        if cabinet == 'cabinet':
            req = 'cabinet'
            component = dataapi.getCABINETs()
        if psu == 'psu':
            req = 'psu'
            component = dataapi.getPSUs()

    return render_template('admin/inventory.html', req=req, component=component)


@app.route('/statistics')
def statistics():
    return render_template('admin/statistics.html')


@app.route('/system')
def system():
    return render_template('admin/system.html')


if __name__ == '__main__':
    app.run(debug=True)
