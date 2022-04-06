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
        cpuminbudget = request.form.get('cpuMinBudget')
        cpumaxbudget = request.form.get('cpuMaxBudget')
        cpucoresingle = request.form.get('cpuCoreSingle ')
        cpucoredual = request.form.get('cpuCoreDual')
        cpucorequad = request.form.get('cpuCoreQuad')
        cpucorehexa = request.form.get('cpuCoreHexa')
        cpucoreocta = request.form.get('cpuCoreOcta')
        cpubrandamd = request.form.get('cpuBrandAMD')
        cpubrandintel = request.form.get('cpuBrandIntel')
        cpubrandothers = request.form.get('cpuBrandOthers')
        coolerminbudget = request.form.get('coolerMinBudget')
        coolermaxbudget = request.form.get('coolerMaxBudget')
        coolerbrandnoctua = request.form.get('coolerBrandNoctua')
        coolerbrandcoolermaster = request.form.get('coolerBrandCoolerMaster')
        coolerbranddeepcool = request.form.get('coolerBrandDeepCool')
        coolerbrandarctic = request.form.get('coolerBrandArctic')
        coolerbrandcorsair = request.form.get('coolerBrandCorsair')
        coolerbrandzebronics = request.form.get('coolerBrandZebronics')
        coolerbrandmsi = request.form.get('coolerBrandMSI')
        coolerbrandamd = request.form.get('coolerBrandAMD')
        ramminbudget = request.form.get('ramMinBudget')
        rammaxbudget = request.form.get('ramMaxBudget')
        ramtypeddr = request.form.get('ramTypeDDR')
        ramtypeddr2 = request.form.get('ramTypeDDR2')
        ramtypeddr3 = request.form.get('ramTypeDDR3')
        ramtypeddr4 = request.form.get('ramTypeDDR4')
        ramtypeddr5 = request.form.get('ramTypeDDR5')
        rambrandhyperx = request.form.get('ramBrandHyperX')
        rambrandcrucial = request.form.get('ramBrandCrucial')
        rambrandcorsair = request.form.get('ramBrandCorsair')
        rambrandadata = request.form.get('ramBrandADATA')
        rambrandsamsung = request.form.get('ramBrandSamsung')
        rambrandkingston = request.form.get('ramBrandKingston')
        rambrandgigabyte = request.form.get('ramBrandGigabyte')
        rambrandhp = request.form.get('ramBrandHP')
        rambrandacer = request.form.get('ramBrandAcer')
        rambrandothers = request.form.get('ramBrandOthers')
        gpuminbudget = request.form.get('gpuMinBudget')
        gpumaxbudget = request.form.get('gpuMaxBudget')
        gpuinterfacepci = request.form.get('gpuInterfacePCI')
        gpuinterfaceagp = request.form.get('gpuInterfaceAGP')
        gpubrandasus = request.form.get('gpuBrandAsus')
        gpubrandzotac = request.form.get('gpuBrandZotac')
        gpubrandgigabyte = request.form.get('gpuBrandGigabyte')
        gpubrandmsi = request.form.get('gpuBrandMSI')
        gpubrandnvidia = request.form.get('gpuBrandNvidia')
        gpubrandothers = request.form.get('gpuBrandOthers')
        boardminbudget = request.form.get('boardMinBudget')
        boardmaxbudget = request.form.get('boardMaxBudget')
        boardramddr = request.form.get('boardRAMDDR')
        boardramddr2 = request.form.get('boardRAMDDR2')
        boardramddr3 = request.form.get('boardRAMDDR3')
        boardramddr4 = request.form.get('boardRAMDDR4')
        boardramddr5 = request.form.get('boardRAMDDR5')
        boardbrandasus = request.form.get('boardBrandAsus')
        boardbrandmsi = request.form.get('boardBrandMSI')
        boardbrandgigabyte = request.form.get('boardBrandGigabyte')
        boardbrandintel = request.form.get('boardBrandIntel')
        boardbrandzebronics = request.form.get('boardBrandZebronics')
        boardbrandaorus = request.form.get('boardBrandAorus')
        storageminbudget = request.form.get('storageMinBudget')
        storagemaxbudget = request.form.get('storageMaxBudget')
        storagebrandcrucial = request.form.get('storageBrandCrucial')
        storagebrandsamsung = request.form.get('storageBrandSamsung')
        storagebrandwd = request.form.get('storageBrandWD')
        storagebrandgigabyte = request.form.get('storageBrandGigabyte')
        storagebrandseagate = request.form.get('storageBrandSeagate')
        storagebrandkingston = request.form.get('storageBrandKingston')
        storagebrandhp = request.form.get('storageBrandHP')
        storagebrandacer = request.form.get('storageBrandAcer')
        psuminbudget = request.form.get('psuMinBudget')
        psumaxbudget = request.form.get('psuMaxBudget')
        psubrandcorsair = request.form.get('psuBrandCorsair')
        psubrandartis = request.form.get('psuBrandArtis')
        psubrandcoolermaster = request.form.get('psuBrandCoolerMaster')
        psubrandasus = request.form.get('psuBrandAsus')
        psubranddeepcool = request.form.get('psuBrandDeepCool')
        psubrandgigabyte = request.form.get('psuBrandGigabyte')
        psubrandnzxt = request.form.get('psuBrandNZXT')
        psubrandgamdias = request.form.get('psuBrandGamdias')
    return render_template('User/buildpc.html')


@app.route('/autobuild', methods=['GET', 'POST'])
def autobuild():
    ipcontrol.getIP(request.remote_addr)
    if request.method == 'POST':
        pass

    return render_template('User/autobuild.html')


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
    return render_template('User/testHTMLs/logictest.html',
                           data=logic.buildpc(int(budget), bool(cpu), bool(ram), bool(hdd)))


if __name__ == '__main__':
    app.run(debug=True)
