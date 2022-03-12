import requests

#single ip request


response = requests.get("http://ip-api.com/json/24.48.0.1").json()
print(response)

print(response['country'])



#batch ip  request

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