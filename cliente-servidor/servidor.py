import socket, psutil, pickle, cpuinfo

def listCon():
    interfaces = psutil.net_if_addrs()
    nomes = []
    array = []
    for i in interfaces:
        nomes.append(str(i))
    for i in nomes:
        for j in interfaces[i]:
            array.append(str(j.family))
            array.append(str(j.address))
            array.append(str(j.netmask)) if j.netmask is not None else array.append('None')
            array.append(str(j.broadcast)) if j.broadcast is not None else array.append('None')
            array.append(str(j.ptp)) if j.ptp is not None else array.append('None')
        return array



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
porta = 9991
host = socket.gethostname()
dest = (host, porta)
s.bind(dest)
print("Servidor conectado!")

(msg, host) = s.recvfrom(1024)



resposta = []
##########TP4
resposta.append(psutil.disk_usage(path='D:').percent)
resposta.append(psutil.disk_usage(path='D:').total / 1024**3.0)
resposta.append(psutil.virtual_memory().percent)
resposta.append(psutil.virtual_memory().total / 1024**3.0)
resposta.append(int(psutil.cpu_freq().current))
resposta.append(int(psutil.cpu_freq().max))
resposta.append(psutil.net_if_addrs()['Ethernet'][1].address)
##########TP5
cpuInfo = cpuinfo.get_cpu_info()
resposta.append(cpuInfo['brand_raw'])
resposta.append(cpuInfo['arch'])
resposta.append(cpuInfo['bits'])
resposta.append(round(psutil.cpu_freq().max))
resposta.append(round(psutil.cpu_freq().current, 2))
resposta.append(psutil.cpu_count())
resposta.append(psutil.cpu_count(logical=False))
##########TP6

for process in psutil.pids()[-4:]:
    try:
        p = psutil.Process(process)
        resposta.append(str(process)),
        resposta.append(p.name()),
        resposta.append(p.status()),
        resposta.append(p.num_threads())

    except Exception as e:
        pass

#########TP7

resposta.append(listCon())
bytes_resp = pickle.dumps(resposta)
s.sendto(bytes_resp, host)
print("Dados enviados para o cliente")
s.close()
