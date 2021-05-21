import psutil
import socket
import ipaddress

socket_connections = psutil.net_connections(kind='inet')

def ip_adress():
    return psutil.net_if_addrs()['em1'][0][1]

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def localipv4():
    ips = psutil.net_if_addrs()
    ips4v = []
    mac = []
    for ip in ips:
        for nic in ips[ip]:
            if nic.family == 2:
                ips4v = [nic.address]
            elif nic.family == 23:
                mac = [nic.address]
    return (','.join(ips4v))
def localipv6():
    ips = psutil.net_if_addrs()
    ips4v = []
    mac = []
    for ip in ips:
        for nic in ips[ip]:
            if nic.family == 2:
                ips4v = [nic.address]
            elif nic.family == 23:
                mac = [nic.address]
    return (','.join(mac))
def rede_privada():
    return format(ipaddress.IPv4Address(get_ip_address()).is_private)


def ipv4():
    return ipaddress.ip_network(get_ip_address())



