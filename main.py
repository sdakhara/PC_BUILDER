from flask import *

from flask_session import Session
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
authenticator = Authentication()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


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
        data = authenticator.verifyuser(useremail, userpass)
        if data:
            session['username'] = data.UserName
            session['userid'] = data.UserID
            return redirect(url_for('home'))
    return render_template('User/login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/index')
def index():
    ipcontrol.getIP(request.remote_addr)
    return render_template('User/index.html')


@app.route('/buildpc', methods=['GET', 'POST'])
def buildpc():
    ipcontrol.getIP(request.remote_addr)
    return render_template('User/buildpc.html')


@app.route('/cpuselect/<query>', methods=['GET', 'POST'])
def cpuselect(query):
    ipcontrol.getIP(request.remote_addr)
    data = None
    if query == 'cpu':
        data = dataapi.getCPUs()
        session['cpu'] = None
    if query == 'board':
        data = dataapi.getBOARDs()
    if query == 'ram':
        data = dataapi.getRAMs()
    if query == 'hdd':
        data = dataapi.getSTORAGEs()
    if query == 'gpu':
        data = dataapi.getGPUs()
    if query == 'psu':
        data = dataapi.getPSUs()
    if query == 'cab':
        data = dataapi.getCABINETs()
    if query == 'cooler':
        data = dataapi.getCOOLERs()
    return render_template('User/cpuselect.html', data=data, type=query)


@app.route('/cpuselect/componentadder/<comptype>/<compid>')
def componentadder(comptype, compid):
    if comptype == 'cpu':
        session['cpu'] = dataapi.getCPUs(cpuid=int(compid))
    if comptype == 'board':
        session['board'] = dataapi.getBOARDs(boardid=int(compid))
    if comptype == 'ram':
        session['ram'] = dataapi.getRAMs(ramid=int(compid))
    if comptype == 'hdd':
        session['hdd'] = dataapi.getSTORAGEs(strgid=int(compid))
    if comptype == 'gpu':
        session['gpu'] = dataapi.getGPUs(gpuid=int(compid))
    if comptype == 'psu':
        session['psu'] = dataapi.getPSUs(psuid=int(compid))
    if comptype == 'cab':
        session['cab'] = dataapi.getCABINETs(cabid=int(compid))
    if comptype == 'cooler':
        session['cooler'] = dataapi.getCOOLERs(coolerid=int(compid))
    return redirect(url_for('buildpc'))


@app.route('/addthispc')
def addthispc():
    if not session.get('userid'):
        return redirect('login')
    if session['userid']:
        userid = session['userid']
        price=0
        cpuid = boardid = psuid = ramid = hddid = coolerid = cabid = gpuid = 0
        if session.get('cpu'):
            cpuid = session.get('cpu')[0][1]
            price+=session['cpu'][0][-1]
        if session.get('board'):
            boardid = session.get('board')[0][1]
            price += session['board'][0][-1]
        if session.get('psu'):
            psuid = session.get('psu')[0][1]
            price += session['psu'][0][-1]
        if session.get('ram'):
            ramid = session.get('ram')[0][1]
            price += session['ram'][0][-1]
        if session.get('hdd'):
            hddid = session.get('hdd')[0][1]
            price += session['hdd'][0][-1]
        if session.get('cooler'):
            coolerid = session.get('cooler')[0][1]
            price += session['cooler'][0][-1]
        if session.get('cab'):
            cabid = session.get('cab)')[0][1]
            price += session['cab'][0][-1]
        if session.get('gpu'):
            gpuid = session.get('gpu')[0][1]
            price += session['gpu'][0][-1]
        authenticator.addpc(userid=userid, cpuid=cpuid, hddid=hddid, boardid=boardid, cabid=cabid, psuid=psuid,
                            gpuid=gpuid, ramid=ramid, coolerid=coolerid, price=price)
        session.clear()
        return redirect(url_for('home'))


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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/contactus.html')


if __name__ == '__main__':
    app.run(debug=True)
