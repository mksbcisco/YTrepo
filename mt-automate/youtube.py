# This is the code we built in the YouTube Video 
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
urllib3.disable_warnings()

ipaddress = input("Please enter the IP of the router from which you want the list of bridge interfaces :")
username = input("Please enter the username of this router :")
password = input("Please enter the password of this router :")

url = 'https://'+ipaddress+'/rest'
response = requests.get(url+'/interface', auth=HTTPBasicAuth(username,password), verify=False)
for interface in response.json():
    if interface["type"]=="bridge":
        print("The ID of the bridge interface is :" + interface[".id"] +", the name of the interface is :" +interface["name"])
