import psutil
from prettytable import PrettyTable
import netifaces

def test():
    print (psutil.net_io_counters(pernic=True))

def proc_redes():
    pro_table = PrettyTable(['Endereço', 'Mascara', 'Gateway'])
    for i in netifaces.interfaces():
        try:
            pro_table.add_row([
                netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'],
                netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'],
                netifaces.gateways()['default'][netifaces.AF_INET][0],

            ])

        except Exception as e:
            pass
    print(pro_table)


def conexao():
    table = PrettyTable(['Conexão', 'Status', 'Velocidade'])
    for key in psutil.net_if_stats().keys():
        name = key
    up = "Up" if psutil.net_if_stats()[key].isup else "Down"
    speed = psutil.net_if_stats()[key].speed
    table.add_row([name, up, speed])
    print(table)


def processos():
    process_table = PrettyTable(['PID', 'PNAME', 'STATUS', 'NUM THREADS'])
    for process in psutil.pids()[-10:]:
        try:
            p = psutil.Process(process)
            process_table.add_row([
                str(process),
                p.name(),
                p.status(),
                p.num_threads()
            ])

        except Exception as e:
            pass
    print(process_table)

print("----Procesos de rede----")
proc_redes()
print("----Conexão----")
conexao()
print("----Processos----")
processos()
print("----Todos os processos na máquina----")
test()