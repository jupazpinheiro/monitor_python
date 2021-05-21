import socket, pickle
from prettytable import PrettyTable

def imprime(l):
    tp4 = PrettyTable(['IP', 'Espaço usado em disco(%)', 'Total em disco', 'Espaço usado em memória (%)',
                             'Total de memória', 'CPU consumida', 'Total CPU'])
    tp4.add_row([
        str(l[6]),
        str(round(l[0], 2)),
        str(round(l[1], 2)),
        str(round(l[2], 2)),
        str(round(l[3], 2)),
        str(round(l[4], 2)),
        str(round(l[5], 2))
        ])

    print(tp4)

    tp5 = PrettyTable(['CPU-brand-', 'CPU-arch-', 'CPU-bits-', 'Frequencia total',
                             'Frequencia corrente', 'CPU -lógicas-', 'CPU -físicas-'])
    tp5.add_row([
        str(l[7]),
        str(l[8]),
        str(l[9]),
        str(l[10]),
        str(l[11]),
        str(l[12]),
        str(l[13])
        ])

    print(tp5)

    tp6 = PrettyTable(['PID', 'Processo', 'Estado','Threads'
                             ])
    tp6.add_row([
        str(l[14]),
        str(l[15]),
        str(l[16]),
        str(l[17])

    ])
    tp6.add_row([
        str(l[18]),
        str(l[19]),
        str(l[20]),
        str(l[21])

    ])
    tp6.add_row([
        str(l[22]),
        str(l[23]),
        str(l[24]),
        str(l[25])

    ])
    tp6.add_row([
        str(l[26]),
        str(l[27]),
        str(l[28]),
        str(l[29])

    ])
    print(tp6)

    tp7 = PrettyTable(['Família',
                       'Endereço', 'Máscara', 'Broadcast', 'PTP'])
    tp7.add_row([
        str(l[30][0]),
        str(l[30][1]),
        str(l[30][2]),
        str(l[30][3]),
        str(l[30][4])

    ])
    tp7.add_row([
        str(l[30][5]),
        str(l[30][6]),
        str(l[30][7]),
        str(l[30][8]),
        str(l[30][9])

    ])
    tp7.add_row([
        str(l[30][10]),
        str(l[30][11]),
        str(l[30][12]),
        str(l[30][13]),
        str(l[30][14])

    ])




    print(tp7)

try:
    socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (socket.gethostname(), 9991)

    socketUDP.sendto('Envio do cliente'.encode('ascii'), dest)

    (msg, host) = socketUDP.recvfrom(1024)
    lista = pickle.loads(msg)
    imprime(lista)

    socketUDP.close()

except Exception as error:
    print(error)


