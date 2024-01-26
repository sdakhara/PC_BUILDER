from flask import *

# from flask_session import Session
from logics.Admin.datashare import Authentication, datatransfer
from logics.user.autobuild import logic


class globs:
    USER = None


app = Flask(__name__)
g = globs()
logic = logic()
dataapi = datatransfer()
authenticator = Authentication()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Session(app)


# User Routes
@app.route('/')
def home():
    return render_template('User/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
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
    return render_template('User/index.html')


@app.route('/buildpc', methods=['GET', 'POST'])
def buildpc():
    return render_template('User/buildpc.html')


@app.route('/cpuselect/<query>', methods=['GET', 'POST'])
def cpuselect(query):
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
        price = 0
        cpuid = boardid = psuid = ramid = hddid = coolerid = cabid = gpuid = 0
        try:
            cpuid = session.get('cpu')[0][1]
            price += session['cpu'][0][-1]
            boardid = session.get('board')[0][1]
            price += session['board'][0][-1]
            psuid = session.get('psu')[0][1]
            price += session['psu'][0][-1]
            ramid = session.get('ram')[0][1]
            price += session['ram'][0][-1]
            hddid = session.get('hdd')[0][1]
            price += session['hdd'][0][-1]
            coolerid = session.get('cooler')[0][1]
            price += session['cooler'][0][-1]
            cabid = session.get('cab')[0][1]
            price += session['cab'][0][-1]
            gpuid = session.get('gpu')[0][1]
            price += session['gpu'][0][-1]

            authenticator.addpc(userid=userid, cpuid=cpuid, hddid=hddid, boardid=boardid, cabid=cabid, psuid=psuid,
                                gpuid=gpuid, ramid=ramid, coolerid=coolerid, price=price)
            if session.get('cpu'):
                session.pop('cpu')
            if session.get('board'):
                session.pop('board')
            if session.get('ram'):
                session.pop('ram')
            if session.get('hdd'):
                session.pop('hdd')
            if session.get('psu'):
                session.pop('psu')
            if session.get('cooler'):
                session.pop('cooler')
            if session.get('cab'):
                session.pop('cab')
            if session.get('gpu'):
                session.pop('gpu')
            price = 0
            return redirect(url_for('home'))
        except:
            return redirect(url_for('home'))


@app.route('/clearpc')
def clearpc():
    if session.get('cpu'):
        session.pop('cpu')
    if session.get('board'):
        session.pop('board')
    if session.get('ram'):
        session.pop('ram')
    if session.get('hdd'):
        session.pop('hdd')
    if session.get('psu'):
        session.pop('psu')
    if session.get('cooler'):
        session.pop('cooler')
    if session.get('cab'):
        session.pop('cab')
    if session.get('gpu'):
        session.pop('gpu')
    return redirect(url_for('buildpc'))


@app.route('/autobuild', methods=['GET', 'POST'])
def autobuild():
    pcs = None
    if request.method == 'POST':
        try:
            budget = int(request.form.get('budget'))
        except:
            return redirect(url_for('autobuild'))
        pcs = logic.autobuild(budget)
    return render_template('User/autobuild.html', pcs=pcs)


@app.route('/addpc/<cpu>/<board>/<ram>/<hdd>/<psu>/<cab>/<price>')
def addpc(cpu, board, ram, hdd, psu, cab, price):
    authenticator.addautobuild(userid=session.get('userid'), cpuid=cpu, boardid=board, ramid=ram, hddid=hdd, psuid=psu,
                               cabid=cab, price=price)
    return redirect(url_for('viewbuilds'))


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        pass
    return render_template('User/about.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('number')
        password = request.form.get('password')
        conpass = request.form.get('conpass')
        authenticator.addUser(name, email, password, conpass, phone)
        return redirect('/login')
    return render_template('User/signup.html')


@app.route('/buildguide', methods=['GET', 'POST'])
def buildguide():
    if request.method == 'POST':
        pass

    return render_template('User/buildguide.html')


@app.route('/viewbuilds', methods=['GET', 'POST'])
def viewbuilds():
    pc = None
    if not session.get('userid'):
        return redirect('login')
    if session['userid']:
        pc = dataapi.getPCS(userid=session['userid'])
    return render_template('User/viewbuilds.html', pcs=pc)


@app.route('/buildhistory', methods=['GET', 'POST'])
def buildhistory():
    if request.method == 'POST':
        pass
    return render_template('User/buildhistory.html')


@app.route('/searchparts', methods=['GET', 'POST'])
def searchparts():
    comp = None
    dt = None
    if request.method == 'POST':
        comp = request.form.get('component')
        txt = request.form.get('searchtext')
        if not comp:
            return render_template('User/searchparts.html', data='None')
        dt = dataapi.getComponent(component=comp, srchtxt=txt)
        print(comp)
        print(txt)
    return render_template('User/searchparts.html', dt=dt, comp=comp)


@app.route('/showcomponent/<comp>/<id>', methods=['GET', 'POST'])
def component(comp, id):
    data = dataapi.getComponent(component=comp, id=id)
    return render_template('/User/componentdata.html', data=data, comp=comp)


@app.route('/usersbuilds', methods=['GET', 'POST'])
def usersbuilds():
    pcs = dataapi.getPCS()
    return render_template('User/usersbuilds.html', pcs=pcs)


@app.route('/ratebuilds/<pcid>', methods=['GET', 'POST'])
def ratebuilds(pcid):
    pc = dataapi.getPCS(pcid=int(pcid))
    return render_template('User/ratebuilds.html', pc=pc)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        message = request.form.get('message')
        authenticator.addMsg(username=username, email=email, message=message, ip=request.remote_addr)
    return render_template('User/contactus.html')


if __name__ == '__main__':
    app.run(port=80)
