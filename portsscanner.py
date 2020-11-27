import socket
from colorama import init 
from termcolor import colored 

def scan(target, ports):
    print('\n' + ' Starting Scan for ' + str(targets))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        # print("[-]Port Closed" + str(port))
        pass

targets = input("[*] Enter Targets to scan(split them by comma ','): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets: 

    print(colored('[*] Scanning Multiple Targets', 'blue')) 
    # print(colored("[*] Scanning Multiple Targets", '', 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else: 
    scan(targets, ports)