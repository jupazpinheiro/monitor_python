import psutil
import os
import cpuinfo

info = cpuinfo.get_cpu_info()


# modulo de operaçoes para cheque da cpu

def frequencia():
    return psutil.cpu_freq().max / 1000
    #return str(round(psutil.cpu_freq().current, 2))


def nome_cpu():
    return info['brand_raw']


def sistema_operacional():
    return os.uname().sysname


def cores():
    return psutil.cpu_count()


def cores_fisicos():
    return psutil.cpu_count(logical=False)


def consumo_cpu_percentagem():
    return psutil.cpu_times_percent()


def consumo_cpu_porcentagem_formatado():
    consumo = consumo_cpu_percentagem()
    return consumo.user + consumo.system


def cpu_livre_porcentagem():
    return consumo_cpu_percentagem().idle


def arquitetura():
    return info['arch']


def palavra():
    return info['bits']
