import requests


# single ip request

def get_ip(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}").json()
    return response


# batch ip  request

'''
response = requests.post("http://ip-api.com/batch", json=[
    {"query":"208.80.152.201"},
    {"query":"168.71.3.52"},
    {"query":"206.189.198.234"},
    {"query":"157.230.75.212"}
]).json()

for ip_info in response:
        print(ip_info["country"])
        print(ip_info["country"])

'''
