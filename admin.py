from flask import Flask, render_template, jsonify, request, redirect, url_for
from logics.admin.IPLocation import get_ip
from logics.admin.datashare import userdt, Authentication

app = Flask(__name__)
usrdata = userdt()
verifier = Authentication()
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


@app.route('/', methods=['GET', 'POST'])
def home():
    from sqlalchemy import create_engine, Column
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.types import String, Integer

    engine = create_engine("mysql+pymysql://Sujal:9099@127.0.0.1:3306/testdb")
    Session = sessionmaker()
    db = Session(bind=engine)
    Base = declarative_base()

    class adminloginrecord(Base):
        __tablename__ = 'adminloginrecord'

        RID = Column(Integer, primary_key=True, autoincrement=True)
        AdminID = Column(String)
        AdminName = Column(String)
        LoginTime = Column(String)

    class admindata(Base):
        __tablename__ = 'admindata'

        AdminID = Column(String, primary_key=True)
        AdminName = Column(String)
        Email = Column(String)
        Password = Column(String)
        PhoneNo = Column(String)

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        data = verifier.verify(email, password)
        if data:
            return redirect(url_for('dashboard'))

    return render_template('Admin/login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('Admin/index.html')

@app.route('/messages')
def messages():
    return render_template('Admin/messages.html')


@app.route('/users')
def users():
    # dt = usrdata.getAllUser()
    dt = verifier.verify()
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
