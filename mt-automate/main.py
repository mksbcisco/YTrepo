
#This is a sample code for Mikrotik Router Automation
from requests.auth import HTTPBasicAuth
import requests
import json
from IPy import IP 
import urllib3
import ipaddress

urllib3.disable_warnings()
apiURL = 'https://IPADDRESS/rest' # Please enter your IP address 
apiUsername = 'USERNAME' # Input your username here 
apiPassword = 'PASSWORD' # Input your password here 

def getInterface():
    response = requests.get(apiURL+'/interface', auth=HTTPBasicAuth(apiUsername, apiPassword), verify=False)
    for jo in response.json():
        print("The interface id is " + jo[".id"] + " interface name is " + jo["name"])

def checkInterfaceExist(newBridgeName):
    response = requests.get(apiURL+'/interface', auth=HTTPBasicAuth(apiUsername,apiPassword), verify=False)
    for jo in response.json():
        if jo["name"] == newBridgeName:
            return False
            break
        else:
            return True

def getInterfaceName(interfaceID):
    interfaceID = "*"+ str(interfaceID)
    response = requests.get(apiURL+'/interface', auth=HTTPBasicAuth(apiUsername,apiPassword), verify=False)
    for interface in response.json():
        if interface[".id"] == interfaceID:
            return interface["name"],True
            break



def addBridgeInterface():
    newBridgeName=input("\n Please specify the name of new Bridge Interface : ")
    print(checkInterfaceExist(newBridgeName))
    response = requests.put(apiURL+'/interface/bridge', auth=HTTPBasicAuth(apiUsername,apiPassword), verify=False, data=json.dumps({"name":newBridgeName}))
    if response.status_code == 201:
        print("A new bridge interface has been created with id: "+response.json()[".id"])
    else:
        print("Oops Something went wrong, please contact administrator. The server says : "+response.json()["detail"])

def capture_userInput():
    print("Welcome to the MikroTik Automation, \nWhat operation will you like to do:(Choose One) \n\n [1] Get a List of Interfaces \n [2] Add a new bridge interface \n [3] Add IP address to an interface \n [99] Exit this menu")
    user_input = int(input(" \n\n Please enter a number(1-99)[Default is 99]: ") or 99)
    return(user_input)

def addIPaddressInterface():
    getInterface()
    i = 0
    while i==0:
        interfaceToAddIP = input("Please enter the interface id on which you want to input the IP address: *")
        interfaceName = getInterfaceName(interfaceToAddIP)
        if type(interfaceName) == tuple:
            interfaceName = interfaceName[0]
            i=1
        else:
            input ("You have entered an invalid input, press ENTER to continue ...")
            continue
    goodIP = True
    while goodIP:
        try:
            getIPAddress = input ("Enter the IP Address you want to assign to " + interfaceName + " use format(A.B.C.D/E, e.g. 192.168.0.1/24):")
            getIPAddress = ipaddress.IPv4Interface(getIPAddress)
            goodIP = False
            response = requests.get(apiURL+'/ip/address', auth=HTTPBasicAuth(apiUsername,apiPassword), verify=False)
            for ipQuery in response.json():
                if str(getIPAddress) == ipQuery["address"]:
                    goodIP = True
                    input("This IP address is already in use with the interface " + ipQuery["interface"] + " press ENTER to continue to assigna new IP address...")
                    break
        except ipaddress.AddressValueError as err:
            print(err)
            continue
        except ipaddress.NetmaskValueError as err:
            print(err)
            continue
    getIPAddress = str(getIPAddress)
    response=requests.put(apiURL+'/ip/address', auth=HTTPBasicAuth(apiUsername,apiPassword), verify=False, data=json.dumps({"interface":interfaceName , "disabled": "false", "address": getIPAddress}))

    

user_input = capture_userInput()
while user_input != 99:
    if (user_input == 1):
        getInterface()
        input("press any key to continue...")
    elif(user_input == 2):
        addBridgeInterface()
        input("press any key to continue...")
    elif(user_input == 3):
        addIPaddressInterface()
        input("press any key to continue...")
    else:
        input("Your input has is not valid, press any key to continue...")
    user_input = capture_userInput()
else:
    print("You wanted to exit the program")
