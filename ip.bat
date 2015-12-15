netsh interface ipv4 set address name="Ethernet 2" source=static 192.168.0.56 255.255.255.0 192.168.0.1 1
netsh interface ipv4 set dns name="Ethernet 2" static 62.81.16.164
netsh interface ipv4 add dns name="Ethernet 2" 62.81.16.213 index=2