# Readme

## Problem Statement
1. All devices are not on, explore Packet Tracer and switch on all the devices
2. Student – 1 and Teacher -1, refer to network on the left side and we need to pass VLANs for the same from the server to the Access Switch, such that Students get port 1-5 and Teachers get port 6-10. Student -1 have VLAN 11, Teacher-1 have VLAN 12
3. Same network as above for 2nd building only change will be Student 2 to get VLAN 21 and Teacher 2 to get VLAN 22
4. If all tasks are done correctly the servers and Student’s device will get IP address from range 192.168.xy.0/24 where xy is VLAN ID.
5. In case there is a problem try to debug the same from switches using various show commands
6. Administrator on both the building will have common VLAN 100 and will have to be connected to the Phones in the network. They will access ports 11-15 only. Once the phones are connected properly to the network, they should get IP address and a number with which they can dial each other.
Note: provision for one phone in each building must be done. We have only 2 phones configured in our router. 

[VLAN_practice lab.pkt](https://github.com/mksbcisco/YTrepo/blob/main/CCNA/VLAN_practice%20lab.pkt) is the un-configured file and the [VLAN_practice lab_execute.pkt](https://github.com/mksbcisco/YTrepo/blob/main/CCNA/VLAN_practice%20lab_execute.pkt) is the solution file 

### For Problems related to Voice VLAN
You may have to execute follwing configuration in 2811 Router 
```
ephone 1
 mac-address 00D0.BA14.8E2C (change this mac-address, use of your phone in Packet Tracer)
 button 1:2 (the number after : will be the extension used by above mentioned mac-address)
ephone 2
 mac-address 00D0.FF96.4E13 (change this mac-address, use of your phone in Packert Tracer)
 button 1:1 (the number after : will be the extension used by above mentioned mac-address)
 ```
