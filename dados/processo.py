import psutil
import time
import sched

s = sched.scheduler(time.time, time.sleep)

def imprime_processo(pid):
    for process in psutil.pids()[-10:]:
        try:
            p = psutil.Process(pid)
            texto = ('{:6}'.format(pid))
            texto = (texto + '{:11}'.format(p.num_threads()))
            texto = (texto + " " + time.ctime(p.create_time()) + " ")
            texto = (texto + '{:8.2f}'.format(p.cpu_times().user))
            texto = (texto + '{:8.2f}'.format(p.cpu_times().system))
            texto = (texto + '{:10.2f}'.format(p.memory_percent()) + " MB")
            rss = p.memory_info().rss / 1024 / 1024
            texto = (texto + '{:10.2f}'.format(rss) + " MB")
            vms = p.memory_info().vms / 1024 / 1024
            texto = (texto + '{:10.2f}'.format(vms) + " MB")
            texto = (texto + " " + p.exe())
            print(texto)
        except:
            pass

def listar_processos():
    lista = psutil.pids()
    titulo = '{:^7}'.format("PID")
    titulo = titulo + '{:^11}'.format("# Threads")
    titulo = titulo + '{:^26}'.format("Criação")
    titulo = titulo + '{:^9}'.format("T. Usu.")
    titulo = titulo + '{:^9}'.format("T. Sis.")
    titulo = titulo + '{:^12}'.format("Mem. (%)")
    titulo = titulo + '{:^12}'.format("RSS")
    titulo = titulo + '{:^12}'.format("VMS")
    titulo = titulo + " Executável"
    print(titulo)


    for i in lista:
        imprime_processo(i)


start = time.time()
print('Início do programa: ', time.ctime(start))
s.enter (2, 1,listar_processos())





