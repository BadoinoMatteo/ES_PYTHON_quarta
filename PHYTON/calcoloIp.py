import subprocess

ipaddress = "192.168.88.0"
mask = 24

ipaddress_splitted = [int(i) for i in ipaddress.split(".")]

ipaddress_bin = 0
for e, group in enumerate(ipaddress_splitted):
    ipaddress_bin = ipaddress_bin + group*(2**(((3-e)*8)))

ipaddress_host = ipaddress_bin
for c in range(1,2**(32-mask)-1):
    ipaddress_host = ipaddress_host + 1
    l = '.'.join([str(int(bin(ipaddress_host)[i:i+8],2)) for i in range(2,34,8)])
    p = subprocess.Popen(['ping', l], stdout=subprocess.PIPE)
    ping = p.communicate()
    print(ping[0].decode())
    #print(ping[0].decode().count('Tempo approssimativo'))
    if(ping[0].decode().count('Tempo approssimativo')>=1):
        print(f"{l} ping andato a buon fine")
    else:
        print(f"{l} host non raggiungibile")
    

