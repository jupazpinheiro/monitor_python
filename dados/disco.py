import psutil
import platform

unameinfo = platform.uname()

disco = psutil.disk_usage('.')
fator_gb = 1024 * 1024 * 1024
fator_mb = 1024 * 1024


def avaliar_sistema_arquivos_total():
    if unameinfo == 'Windows':
        disco_root = psutil.disk_usage('/')
        total = disco_root.total + disco.total
    else:
        total = disco.total
    return total


def avaliar_sistema_arquivos_used():
    if unameinfo == 'Windows':
        disco_root = psutil.disk_usage('/')
        total = disco_root.used + disco.used
    else:
        total = disco.used
    return total


def avaliar_sistema_arquivos_free():
    if unameinfo == 'Windows':
        disco_root = psutil.disk_usage('/')
        total = disco_root.free + disco.free
    else:
        total = disco.free
    return total


def total_mb():
    return round(avaliar_sistema_arquivos_total() / fator_mb)


def usado_mb():
    return round(avaliar_sistema_arquivos_used() / fator_mb)


def livre_mb():
    return round(avaliar_sistema_arquivos_free() / fator_mb)


def total_gb():
    return round(avaliar_sistema_arquivos_total() / fator_gb)


def usado_gb():
    return round(avaliar_sistema_arquivos_used() / fator_gb)


def livre_gb():
    return round(avaliar_sistema_arquivos_free() / fator_gb)

def porcentagem_de_uso():
    return disco.percent

