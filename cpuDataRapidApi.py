import requests
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import String

url = "https://cpu-data.p.rapidapi.com/cpus"
headers = {
    'x-rapidapi-key': "1c2a41ba92mshec9d61014ca2e68p1e3f1cjsn84607970fe3a",
    'x-rapidapi-host': "cpu-data.p.rapidapi.com"
}
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/api_test')
Session = sessionmaker(bind=engine)
db = Session()
Base = declarative_base()


# "CPUMark": "548",
#     "Clockspeed": "1.9 GHz",
#     "Cores": 2,
#     "ID": 2501,
#     "Name": "Intel T1500 @ 1.86GHz",
#     "Platform": "",
#     "Price": "",
#     "Release": "Q2 2009",
#     "Socket": "",
#     "TDP": "",
#     "Threads": 2,
#     "Turbospeed": ""
#
class cpuData(Base):
    __tablename__ = 'cpuData'
    Clockspeed = Column(String)
    Cores = Column(String)
    ID = Column(String, primary_key=True)
    Name = Column(String)
    Platform = Column(String)
    Price = Column(String)
    ReleaseDate = Column(String)
    Socket = Column(String)
    TDP = Column(String)
    Threads = Column(String)
    Turbospeed = Column(String)


response = requests.request("GET", url, headers=headers)

# print(type(response.json())

data = response.json()
# for datas in data:
#     entry = cpuData(Clockspeed = datas.get('Cloclspeed'), Cores = datas.get('Cores'), ID = datas.get('ID'), Name = datas.get('Name'), Platform = datas.get('Platform'), Price = datas.get('Price'), ReleaseDate = datas.get('Release'), Socket = datas.get('Socket'), TDP = datas.get('TDP'), Threads = datas.get('Threads'), Turbospeed = datas.get('Turbospeed'))
#     db.add(entry)
#     db.commit()
#     print('done')
