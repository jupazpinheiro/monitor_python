import os, time
import sched

s = sched.scheduler(time.time, time.sleep)
def getInfo(i):
    print('Nome do arquivo/diretório:', os.path.basename(i))
    status = os.stat(i)
    print('Quantidade de KB:', status.st_size / 1024)
    print('Criado em:', time.ctime(os.path.getctime(i)))
    print('Editado pela última vez em:', time.ctime(status.st_mtime))
    print("\n")


def getCurrentDirFilesInfo():
    listDir = os.listdir()
    for i in listDir:
        getInfo(i)


start = time.time()
print('Início do programa: ', time.ctime(start))
s.enter (2, 1, getCurrentDirFilesInfo())

