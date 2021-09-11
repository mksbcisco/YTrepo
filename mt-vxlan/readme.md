# README

<p>
  GNS3 project dump file is included in this folder you can load this on your GNS3 to test it.<br>
  GNS3 version used is 2.2.23 <br>
  MikroTik CHR version used is 7.1rc2 <br>
  Default username and password of MikroTik images is admin:admin
</p>
    
<p> You will need to add IP addresses to VPCs</p>

## Configuration for Site-1
```
      /interface bridge
add name=BRIDGE-VxLAN-VNI-100
add name=loopback
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no
set [ find default-name=ether2 ] disable-running-check=no
/interface vxlan
add group=239.0.0.1 interface=ether1 mtu=1400 name=vxlan-vni-100 port=8572 \
    vni=100
/disk
set sata1 disabled=no
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/routing ospf instance
add name=Area0 router-id=192.168.1.1
/routing ospf area
add instance=Area0 name=Area0
/interface bridge port
add bridge=BRIDGE-VxLAN-VNI-100 interface=vxlan-vni-100
add bridge=BRIDGE-VxLAN-VNI-100 interface=ether2
/interface l2tp-server server
set l2tpv3-circuit-id="" l2tpv3-cookie-length=0 l2tpv3-digest-hash=md5
/interface vxlan vteps
add interface=vxlan-vni-100 remote-ip=192.168.2.2
add interface=vxlan-vni-100 remote-ip=192.168.3.3
/ip address
add address=192.168.1.1 interface=loopback network=192.168.1.1
add address=172.168.0.1/24 interface=ether1 network=172.168.0.0
/ip dhcp-client
add interface=ether1
/routing ospf interface-template
add area=Area0 interfaces=loopback networks=192.168.1.1/32
add area=Area0 interfaces=ether1 networks=172.168.0.0/24
/system identity
set name=SITE-1
```
 
## Configuration fro Site-2

```
/interface bridge
add name=BRIDGE-VXLAN-VNI-100
add name=loopback
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no
set [ find default-name=ether2 ] disable-running-check=no
/interface vxlan
add group=239.0.0.1 interface=ether1 mtu=1400 name=vxlan-vni-100 port=8572 \
    vni=100
/disk
set sata1 disabled=no
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/routing ospf instance
add name=Area0 router-id=192.168.2.2
/routing ospf area
add instance=Area0 name=Area0
/interface bridge port
add bridge=BRIDGE-VXLAN-VNI-100 interface=vxlan-vni-100
add bridge=BRIDGE-VXLAN-VNI-100 interface=ether2
/interface l2tp-server server
set l2tpv3-circuit-id="" l2tpv3-cookie-length=0 l2tpv3-digest-hash=md5
/interface vxlan vteps
add interface=vxlan-vni-100 remote-ip=192.168.1.1
add interface=vxlan-vni-100 remote-ip=192.168.3.3
/ip address
add address=172.168.0.2/24 interface=ether1 network=172.168.0.0
add address=192.168.2.2 interface=loopback network=192.168.2.2
/ip dhcp-client
add interface=ether1
/routing ospf interface-template
add area=Area0 interfaces=loopback networks=192.168.2.2
add area=Area0 interfaces=ether1 networks=172.168.0.0/24
/system identity
set name=SITE-2
```

## Configuration for Site-3
```
/interface bridge
add name=BRIDGE-VXLAN-VNI-100
add name=loopback
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no
set [ find default-name=ether2 ] disable-running-check=no
/interface vxlan
add group=239.0.0.1 interface=ether1 mtu=1400 name=vxlan-vni-100 port=8572 vni=100
/disk
set sata1 disabled=no
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/routing ospf instance
add name=Area0 router-id=192.168.3.3
/routing ospf area
add instance=Area0 name=Area0
/interface bridge port
add bridge=BRIDGE-VXLAN-VNI-100 interface=ether2
add bridge=BRIDGE-VXLAN-VNI-100 interface=vxlan-vni-100
/interface l2tp-server server
set l2tpv3-circuit-id="" l2tpv3-cookie-length=0 l2tpv3-digest-hash=md5
/interface vxlan vteps
add interface=vxlan-vni-100 remote-ip=192.168.1.1
add interface=vxlan-vni-100 remote-ip=192.168.2.2
/ip address
add address=192.168.3.3 interface=loopback network=192.168.3.3
add address=172.168.0.3/24 interface=ether1 network=172.168.0.0
/ip dhcp-client
add interface=ether1
/routing ospf interface-template
add area=Area0 interfaces=loopback networks=192.168.3.3
add area=Area0 interfaces=ether1 networks=172.168.0.0/24
/system identity
set name=SITE-3
```
