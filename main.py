from flask import Flask, render_template, request
from logics.user.autobuild import logic
from logics.user.iplogics import ipControl

app = Flask(__name__)

logic = logic()
ipcontrol = ipControl()

# User Routes
@app.route('/')
def home():
    ipcontrol.getIP(request.remote_addr)
    return render_template('User/index.html')

@app.route('/index')
def index():
    ipcontrol.getIP(request.remote_addr)
    return render_template('User/index.html')
    
@app.route('/buildpc', methods=['GET', 'POST'])
def buildpc():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass
    return render_template('User/buildpc.html')
    


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
    app.run(host="0.0.0.0")
