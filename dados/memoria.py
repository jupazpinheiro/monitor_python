import psutil

fator_gb = 1024 * 1024 * 1024
fator_mb = 1024 * 1024

def total_mb():
    return round(psutil.virtual_memory().total / fator_mb)


def livre_mb():
    return round(psutil.virtual_memory().free / fator_mb)


def usado_mb():
    return round(psutil.virtual_memory().used / fator_mb)


'''
    valores em GB
'''


def total_gb():
    return round(psutil.virtual_memory().total / fator_gb, 2)


def livre_gb():
    return round(psutil.virtual_memory().free / fator_gb, 2)


def usado_gb():
    return round(psutil.virtual_memory().used / fator_gb, 2)


'''
    valor em porcentagem
'''


def porcentagem():
    return psutil.virtual_memory().percent

'''
    Outras informações
'''

def memoria_swap():
    return round(psutil.swap_memory().total / fator_gb)

def memoria_swap_usada():
    return round(psutil.swap_memory().used / fator_gb)