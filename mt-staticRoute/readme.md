# MikroTik-Static Route

RouterOS - v6.45.8 LTS 
GNS3 - v2.2.24

#### Router 1
```
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no
set [ find default-name=ether2 ] disable-running-check=no
set [ find default-name=ether3 ] disable-running-check=no
set [ find default-name=ether4 ] disable-running-check=no
set [ find default-name=ether5 ] disable-running-check=no
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=DHCP ranges=192.168.1.100-192.168.1.199
/ip dhcp-server
add address-pool=DHCP always-broadcast=yes disabled=no interface=ether5 name=\
    dhcp
/ip address
add address=192.168.1.1/24 interface=ether5 network=192.168.1.0
add address=10.0.12.1/30 interface=ether1 network=10.0.12.0
add address=10.0.13.1/30 interface=ether2 network=10.0.13.0
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=ether1
/ip dhcp-server network
add address=192.168.1.0/24 gateway=192.168.1.1 netmask=24
/system identity set name=Router1
```

#### Router 2
```
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no
set [ find default-name=ether2 ] disable-running-check=no
set [ find default-name=ether3 ] disable-running-check=no
set [ find default-name=ether4 ] disable-running-check=no
set [ find default-name=ether5 ] disable-running-check=no
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=DHCP ranges=192.168.2.100-192.168.2.199
/ip dhcp-server
add address-pool=DHCP always-broadcast=yes disabled=no interface=ether5 name=\
    dhcp
/ip address
add address=192.168.2.1/24 interface=ether5 network=192.168.2.0
add address=10.0.12.2/30 interface=ether1 network=10.0.12.0
add address=10.0.24.1/30 interface=ether2 network=10.0.24.0
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=ether1
/ip dhcp-server network
add address=192.168.2.0/24 gateway=192.168.2.1 netmask=24
/system identity set name=Router2
```

#### Router 3
```
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no
set [ find default-name=ether2 ] disable-running-check=no
set [ find default-name=ether3 ] disable-running-check=no
set [ find default-name=ether4 ] disable-running-check=no
set [ find default-name=ether5 ] disable-running-check=no
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=DHCP ranges=192.168.3.100-192.168.3.199
/ip dhcp-server
add address-pool=DHCP always-broadcast=yes disabled=no interface=ether5 name=\
    dhcp
/ip address
add address=192.168.3.1/24 interface=ether5 network=192.168.3.0
add address=10.0.34.1/30 interface=ether1 network=10.0.34.0
add address=10.0.13.2/30 interface=ether2 network=10.0.13.0
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=ether1
/ip dhcp-server network
add address=192.168.3.0/24 gateway=192.168.3.1 netmask=24
/system identity set name=Router3
```

#### Router 4
```
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no
set [ find default-name=ether2 ] disable-running-check=no
set [ find default-name=ether3 ] disable-running-check=no
set [ find default-name=ether4 ] disable-running-check=no
set [ find default-name=ether5 ] disable-running-check=no
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=DHCP ranges=192.168.4.100-192.168.4.199
/ip dhcp-server
add address-pool=DHCP always-broadcast=yes disabled=no interface=ether5 name=\
    dhcp
/ip address
add address=192.168.4.1/24 interface=ether5 network=192.168.4.0
add address=10.0.34.2/30 interface=ether1 network=10.0.34.0
add address=10.0.24.2/30 interface=ether2 network=10.0.24.0
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=ether1
/ip dhcp-server network
add address=192.168.4.0/24 gateway=192.168.4.1 netmask=24
/system identity set name=Router4
```
