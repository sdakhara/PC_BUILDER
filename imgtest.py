import base64

from flask import Flask, render_template, request
from sqlalchemy import create_engine, Integer, BLOB, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
engine = create_engine("mysql+pymysql://Sujal:9099@127.0.0.1:3306/test")
Base = declarative_base()
Session = sessionmaker(bind=engine)
db = Session()


class new(Base):
    __tablename__ = 'new'
    vid = Column(Integer, primary_key=True)
    images = Column(BLOB)


@app.route('/', methods=['GET', 'POST'])
def home():
    n = 1
    if request.method == 'POST':
        img = request.files['img'].read()
        # file = base64.b64encode(img)
        print(img)
        add = new(vid=n, images=img)
        db.add(add)
        db.commit()
    return render_template('new.html')


app.run(debug=True)
