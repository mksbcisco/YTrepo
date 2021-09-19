# BGP Introduction (comparison between MikroTik RouterOS v6.x and V7.x
<p>MikroTik CHR version used are 6.45.8 and 7.1rc2</p>

### Configuration for RouterOS v6.x 
```
/interface bridge add name=lo disabled=no
/ip address add address=172.16.1.1/32 interface=lo disabled=no
/ip address add address=10.0.0.1/30 interface=ether1 disabled=no
/ip address add address=192.168.10.1/24 interface=ether2 disabled=no
/routing bgp instance add disabled=no as=100 name=AS100 router-id=172.16.1.1
/routing bgp network add disabled=no network=192.168.10.0/24 
/routing bgp peer add disabled=no instance=AS100 remote-address=10.0.0.2 remote-as=200 name=Peer200 
```

### Configuration for RouterOS v7.x
```
/interface/bridge/add name=lo disabled=no
/ip/address/add address=172.16.2.2/32 interface=lo disabled=no
/ip/address/add address=10.0.0.2/30 interface=ether1 disabled=no
/ip/address/add address=192.168.20.1/24 interface=ether2 disabled=no
/ip/firewall/address-list/add disabled=no list=bgp_advertise address=192.168.20.0/24
/routing/bgp/connection/add disabled=no address-families=ip as=200 connect=yes listen=yes local.role=ebgp name=Peer100 remote.address=10.0.0.1 remote.as=100 router-id=172.16.2.2 output.network=bgp_advertise  
```
