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
        
# sample GET requests:
'''
requests.get(url, auth=HTTPBasicAuth(username,password), verify=False)
url - End-point URL, URL from where information is needed e.g. 
    https://router/rest/interface: This will get all the interface of the router
    https://router/rest/ip/address: This will get all the IP addresses of the router
username - Username of the router 
password - Password of the router 
Verify=False - To be used in case the SSL on the router is self-generated and not "known" CA 
'''

# sample PUT requests:
'''
requests.put(url, auth=HTTPBasicAuth(username,password), verify=False, data=DATA)
url - End-point URL, URL where information you need to input e.g. 
    https://router/rest/interface/vlan: Add a VLAN interface
    https://router/rest/ip/address: Add IP Address
username - Username of the router 
password - Password of the router 
Verify=False - To be used in case the SSL on the router is self-generated and not "known" CA 
DATA - Data to be added to the router. This data needs to be in JSON format, so need to convert python object to JSON object e.g.:
    data=json.dumps({"name" : "VLAN100", "vlan-id" : "100", "interface" : "ether1"})
   (Here we are sending data to the router to add VLAN ID 100 with name VLAN100 on interface ether1)
    data=json.dumps({"address" : "192.168.1.1/24" , "interface" : "VLAN100"})
   (Here we are sending data to the router to add IP address 192.168.1.1/24 on interface VLAN100
   Note: you need to use the correct endpoint
'''

# sample PATCH requests:
'''
requests.patch(url, auth=HTTPBasicAuth(username,password), verify=False, data=DATA)
url - End-point URL, URL where information you need to patch, this will include the object ID also. This information can be retrieved from GET requests e.g. 
    https://router/rest/interface/vlan/*10: Patch a VLAN interface with object ID '*10'
    https://router/rest/ip/address/*D: Patch IP address with object ID '*D'
username - Username of the router 
password - Password of the router 
Verify=False - To be used in case the SSL on the router is self-generated and not "known" CA 
DATA - Data to be updated on the router. This data needs to be in JSON format, so need to convert python object to JSON object e.g.:
    data=json.dumps({"name" : "Customer-100"})
   (Here we are sending data to the router to update the name of the VLAN to Customer-100)
    data=json.dumps({"address" : "192.168.1.1/30"})
   (Here we are sending data to the router to update IP address 192.168.1.1/30 on interface 
   Note: you need to use the correct endpoint
'''

# sample DELETE requests:
'''
requests.delete(url, auth=HTTPBasicAuth(username,password), verify=False)
url - End-point URL, URL where object you need to delete, this will include the object ID also. This information can be retrieved from GET requests e.g. 
    https://router/rest/interface/vlan/*10: Deletes the VLAN interface with object ID '*10'
    https://router/rest/ip/address/*D: Deletes IP address with object ID '*D'
username - Username of the router 
password - Password of the router 
Verify=False - To be used in case the SSL on the router is self-generated and not "known" CA 
   Note: When deleting the request will not send any JSON data back for confirmation like in other requests, to check if the request is successful the request's HTTP status-code should come back as 204 
'''
