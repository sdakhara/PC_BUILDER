from flask import Flask, render_template, request, redirect, url_for

from logics.Admin.datashare import Authentication
from logics.user.autobuild import logic
from logics.user.iplogics import ipControl


class globs:
    USER = None


app = Flask(__name__)
g = globs()
logic = logic()
ipcontrol = ipControl()
# dataapi = datatransfer()
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
    if request.method == 'POST':
        cpuMinBudget = request.form.get('cpuMinBudget')
        cpuMaxBudget = request.form.get('cpuMaxBudget')
        cpuCoreSingle = bool(request.form.get('cpuCoreSingle '))
        cpuCoreDual = bool(request.form.get('cpuCoreDual'))
        cpuCoreQuad = bool(request.form.get('cpuCoreQuad'))
        cpuCoreHexa = bool(request.form.get('cpuCoreHexa'))
        cpuCoreOcta = bool(request.form.get('cpuCoreOcta'))
        cpuBrandAMD = bool(request.form.get('cpuBrandAMD'))
        cpuBrandIntel = bool(request.form.get('cpuBrandIntel'))
        cpuBrandOthers = bool(request.form.get('cpuBrandOthers'))
        coolerMinBudget = request.form.get('coolerMinBudget')
        coolerMaxBudget = request.form.get('coolerMaxBudget')
        coolerBrandNoctua = bool(request.form.get('coolerBrandNoctua'))
        coolerBrandCoolerMaster = bool(request.form.get('coolerBrandCoolerMaster'))
        coolerBrandDeepCool = bool(request.form.get('coolerBrandDeepCool'))
        coolerBrandArctic = bool(request.form.get('coolerBrandArctic'))
        coolerBrandCorsair = bool(request.form.get('coolerBrandCorsair'))
        coolerBrandZebronics = bool(request.form.get('coolerBrandZebronics'))
        coolerBrandMSI = bool(request.form.get('coolerBrandMSI'))
        coolerBrandAMD = bool(request.form.get('coolerBrandAMD'))
        ramMinBudget = request.form.get('ramMinBudget')
        ramMaxBudget = request.form.get('ramMaxBudget')
        ramTypeDDR = bool(request.form.get('ramTypeDDR'))
        ramTypeDDR2 = bool(request.form.get('ramTypeDDR2'))
        ramTypeDDR3 = bool(request.form.get('ramTypeDDR3'))
        ramTypeDDR4 = bool(request.form.get('ramTypeDDR4'))
        ramTypeDDR5 = bool(request.form.get('ramTypeDDR5'))
        ramBrandHyperX = bool(request.form.get('ramBrandHyperX'))
        ramBrandCrucial = bool(request.form.get('ramBrandCrucial'))
        ramBrandCorsair = bool(request.form.get('ramBrandCorsair'))
        ramBrandADATA = bool(request.form.get('ramBrandADATA'))
        ramBrandSamsung = bool(request.form.get('ramBrandSamsung'))
        ramBrandKingston = bool(request.form.get('ramBrandKingston'))
        ramBrandGigabyte = bool(request.form.get('ramBrandGigabyte'))
        ramBrandHP = bool(request.form.get('ramBrandHP'))
        ramBrandAcer = bool(request.form.get('ramBrandAcer'))
        ramBrandOthers = bool(request.form.get('ramBrandOthers'))
        gpuMinBudget = request.form.get('gpuMinBudget')
        gpuMaxBudget = request.form.get('gpuMaxBudget')
        gpuInterfacePCI = bool(request.form.get('gpuInterfacePCI'))
        gpuInterfaceAGP = bool(request.form.get('gpuInterfaceAGP'))
        gpuBrandAsus = bool(request.form.get('gpuBrandAsus'))
        gpuBrandZotac = bool(request.form.get('gpuBrandZotac'))
        gpuBrandGigabyte = bool(request.form.get('gpuBrandGigabyte'))
        gpuBrandMSI = bool(request.form.get('gpuBrandMSI'))
        gpuBrandNvidia = bool(request.form.get('gpuBrandNvidia'))
        gpuBrandOthers = bool(request.form.get('gpuBrandOthers'))
        boardMinBudget = request.form.get('boardMinBudget')
        boardMaxBudget = request.form.get('boardMaxBudget')
        boardRAMDDR = bool(request.form.get('boardRAMDDR'))
        boardRAMDDR2 = bool(request.form.get('boardRAMDDR2'))
        boardRAMDDR3 = bool(request.form.get('boardRAMDDR3'))
        boardRAMDDR4 = bool(request.form.get('boardRAMDDR4'))
        boardRAMDDR5 = bool(request.form.get('boardRAMDDR5'))
        boardBrandAsus = bool(request.form.get('boardBrandAsus'))
        boardBrandMSI = bool(request.form.get('boardBrandMSI'))
        boardBrandGigabyte = bool(request.form.get('boardBrandGigabyte'))
        boardBrandIntel = bool(request.form.get('boardBrandIntel'))
        boardBrandZebronics = bool(request.form.get('boardBrandZebronics'))
        boardBrandAorus = bool(request.form.get('boardBrandAorus'))
        storageMinBudget = request.form.get('storageMinBudget')
        storageMaxBudget = request.form.get('storageMaxBudget')
        storageBrandCrucial = bool(request.form.get('storageBrandCrucial'))
        storageBrandSamsung = bool(request.form.get('storageBrandSamsung'))
        storageBrandWD = bool(request.form.get('storageBrandWD'))
        storageBrandGigabyte = bool(request.form.get('storageBrandGigabyte'))
        storageBrandSeagate = bool(request.form.get('storageBrandSeagate'))
        storageBrandKingston = bool(request.form.get('storageBrandKingston'))
        storageBrandHP = bool(request.form.get('storageBrandHP'))
        storageBrandAcer = bool(request.form.get('storageBrandAcer'))
        psuMinBudget = request.form.get('psuMinBudget')
        psuMaxBudget = request.form.get('psuMaxBudget')
        psuBrandCorsair = bool(request.form.get('psuBrandCorsair'))
        psuBrandArtis = bool(request.form.get('psuBrandArtis'))
        psuBrandCoolerMaster = bool(request.form.get('psuBrandCoolerMaster'))
        psuBrandAsus = bool(request.form.get('psuBrandAsus'))
        psuBrandDeepCool = bool(request.form.get('psuBrandDeepCool'))
        psuBrandGigabyte = bool(request.form.get('psuBrandGigabyte'))
        psuBrandNZXT = bool(request.form.get('psuBrandNZXT'))
        psuBrandGamdias = bool(request.form.get('psuBrandGamdias'))
    # cpus = dataapi.getCPUs()
    return render_template('User/buildpc.html')


@app.route('/autobuild', methods=['GET', 'POST'])
def autobuild():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass
    return render_template('User/autobuild.html')


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



if __name__ == '__main__':
    app.run(debug=True)
