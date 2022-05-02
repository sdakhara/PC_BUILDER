from flask import Flask, render_template, request, redirect, url_for

from logics.Admin.datashare import Authentication, datatransfer
from logics.user.autobuild import logic
from logics.user.iplogics import ipControl


class globs:
    USER = None


app = Flask(__name__)
g = globs()
logic = logic()
ipcontrol = ipControl()
dataapi = datatransfer()
Authenticator = Authentication()


# User Routes
@app.route('/')
def home():
    ipcontrol.getIP(request.remote_addr)
    return render_template('User/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        useremail = request.form.get('useremail')
        userpass = request.form.get('userpass')
        data = Authenticator.verifyuser(useremail, userpass)
        if data:
            g.USER = data
            return redirect(url_for('home'))
    return render_template('User/login.html')


@app.route('/index')
def index():
    ipcontrol.getIP(request.remote_addr)
    return render_template('User/index.html')


@app.route('/buildpc', methods=['GET', 'POST'])
def buildpc():
    ipcontrol.getIP(request.remote_addr)
    cpu = None
    if request.method == 'POST':
        if request.form.get('btn') == 'cpu':
            cpuMinBudget = int(request.form.get('cpuMinBudget'))
            cpuMaxBudget = int(request.form.get('cpuMaxBudget'))
            cpuCoreSingle = bool(request.form.get('cpuCoreSingle '))
            cpuCoreDual = bool(request.form.get('cpuCoreDual'))
            cpuCoreQuad = bool(request.form.get('cpuCoreQuad'))
            cpuCoreHexa = bool(request.form.get('cpuCoreHexa'))
            cpuCoreOcta = bool(request.form.get('cpuCoreOcta'))
            cpuBrandAMD = bool(request.form.get('cpuBrandAMD'))
            cpuBrandIntel = bool(request.form.get('cpuBrandIntel'))
            cpu = dataapi.getCPUs(min=cpuMinBudget, max=cpuMaxBudget)
    return render_template('User/buildpc.html', data=cpu)


@app.route('/autobuild', methods=['GET', 'POST'])
def autobuild():
    ipcontrol.getIP(request.remote_addr)
    pcs = [1]
    if request.method == 'POST':
        budget = int(request.form.get('budget'))
        pcs = logic.autobuild(budget)
    return render_template('User/autobuild.html', pcs=pcs)


@app.route('/about', methods=['GET', 'POST'])
def about():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass
    return render_template('User/about.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/signup.html')


@app.route('/buildguide', methods=['GET', 'POST'])
def buildguide():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/buildguide.html')


@app.route('/viewbuilds', methods=['GET', 'POST'])
def viewbuilds():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/viewbuilds.html')


@app.route('/buildhistory', methods=['GET', 'POST'])
def buildhistory():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass
    return render_template('User/buildhistory.html')


@app.route('/searchparts', methods=['GET', 'POST'])
def searchparts():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/searchparts.html')


@app.route('/secondhandpc', methods=['GET', 'POST'])
def secondhandpc():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/secondhandpc.html')


@app.route('/sell', methods=['GET', 'POST'])
def sell():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/sellpc.html')


@app.route('/usersbuilds', methods=['GET', 'POST'])
def usersbuilds():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/usersbuilds.html')


@app.route('/ratebuilds', methods=['GET', 'POST'])
def ratebuilds():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/ratebuilds.html')


@app.route('/cpuselect', methods=['GET', 'POST'])
def cpuselect():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/cpuselect.html')


if __name__ == '__main__':
    app.run(debug=True)
