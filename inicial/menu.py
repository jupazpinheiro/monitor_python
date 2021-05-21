import pygame
from pygame import Surface
from dados import memoria
from dados import cpu
from dados import disco
from dados import rede


azul = (246, 244, 243)
vermelho = (236, 11, 67)
roxo = (216,191,216)
indigo = ((75,0,130))

#dimensões
largura_tela = 800
altura_tela = 600

pygame.font.init()
font = pygame.font.Font(None, 35)
font_info=pygame.font.Font("Lobster-Regular.ttf", 22)

tela = pygame.display.set_mode((largura_tela, altura_tela))
tela.fill(roxo)
pygame.display.set_caption("Projeto de Bloco - Julia Paz")


def texto(t, texto, pos_y): #informações das camadas
    texto_final = font_info.render(texto, True, indigo)
    t.blit(texto_final, (60, pos_y))



def menu_display(t): #1a camada
    t.fill(roxo)
    texto(t, "1 - CPU.", 10)
    texto(t, "2 - MEMÓRIA.", 30)
    texto(t, "3 - DISCO.", 50)
    texto(t, "4 - REDE.", 70)
    texto(t, "5 - RESUMO.", 90)
    texto(t, "----------------------------------", 110)
    tela.blit(t, (0, 10))


def info_cpu_display(t): #informações do processador
    t.fill(roxo)
    texto(t, "Processador: {}".format(cpu.nome_cpu()), 10)
    texto(t, "Arquitetura: {}".format(cpu.arquitetura()), 30)
    texto(t, "Palavra: {} bits".format(cpu.palavra()), 50)
    texto(t, "Velocidade: {} GHz".format(cpu.frequencia()), 70)
    texto(t, "Cores (Físicos): {} ({})".format(cpu.cores(), cpu.cores_fisicos()), 90)
    texto(t, "----------------------------------", 110)

    tela.blit(t, (0, altura_tela / 3))


def info_memoria_display(t): #informações de memória
    t.fill(roxo)
    texto(t, "Total  de memória: {} GB".format(memoria.total_gb()), 10)
    texto(t, "Total de memória virtual: {} GB".format(memoria.memoria_swap()), 30)
    texto(t, "Memória virtual consumida: {} GB".format(memoria.memoria_swap_usada()), 50)
    texto(t, "Memória consumida: {}%".format(memoria.porcentagem()), 70)
    texto(t, "----------------------------------", 110)
    tela.blit(t, (0, altura_tela / 3))

def info_disco_display(t): #informações de disco
    t.fill(roxo)
    texto(t, "Total do disco: {} GB".format(disco.total_gb()), 10)
    texto(t, "Total de disco em uso: {} GB".format(disco.usado_gb()), 30)
    texto(t, "Total de espaço livre em disco: {} GB".format(disco.livre_gb()), 50)
    texto(t, "Consumo atual do disco: {}%".format(disco.porcentagem_de_uso()), 70)
    texto(t, "----------------------------------", 110)
    tela.blit(t, (0, altura_tela / 3))

def info_rede_display(t): #informações de rede
    t.fill(roxo)
    texto(t, "Endereço IP: {}".format(rede.get_ip_address()), 10)
    texto(t,"Local host IPv4:  {}".format(rede.localipv4()),30)
    texto(t, "Local host IPv6:  {}".format(rede.localipv6()), 50)
    texto(t, "Rede Privada:  {}".format(rede.rede_privada()), 70)
    texto(t, "Máscara IPv4: {}".format(rede.ipv4()), 90)
    texto(t, "----------------------------------", 110)
    tela.blit(t, (0, altura_tela / 3))

def info_resumo_display(t): #informações gerais
    t.fill(roxo)
    texto(t, "Processador: " + str(cpu.nome_cpu()), 10)
    texto(t, "Velocidade: {} GHz".format(cpu.frequencia()), 30)
    texto(t, "Arquitetura do processador: " + str(cpu.arquitetura()), 50)
    texto(t, "Total  de memória: {} GB".format(memoria.total_gb()), 70)
    texto(t, "Total de memória virtual: {} GB".format(memoria.memoria_swap()), 90)
    texto(t, "Total do disco: {} GB".format(disco.total_gb()), 110)
    texto(t, "Endereço IP: {}".format(rede.get_ip_address()), 130)
    texto(t, "----------------------------------", 150)
    tela.blit(t, (0, altura_tela / 3))

def disks_display(t):
    d = disco.porcentagem_de_uso()
    larg = largura_tela - 2 * 20
    t.fill(roxo)
    pygame.draw.rect(t, azul, (20, 50, larg, 70))
    larg = larg * d / 100
    pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
    total = disco.total_gb()
    texto_titulo = "Consumo de Disco ( Total: " + str(total) + " GB):"
    texto_final = font.render(texto_titulo, 1, indigo)
    t.blit(texto_final, (20, 10))
    tela.blit(t, (0, 3 * altura_tela / 4))


def cpu_display(t):
    procss = cpu.consumo_cpu_porcentagem_formatado()
    larg = largura_tela - 2 * 20
    t.fill(roxo)
    pygame.draw.rect(t, azul, (20, 50, larg, 70))
    larg = larg * procss / 100
    pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
    total = cpu.frequencia()
    texto_titulo = "Consumo de cpu ( Frequencia: " + str(total) + " GHz):"
    texto_final = font.render(texto_titulo, 1, indigo)
    t.blit(texto_final, (20, 10))
    tela.blit(t, (0, 2 * altura_tela / 3))


def memoria_display(t):
    mem = memoria.porcentagem()
    larg = largura_tela - 2 * 20
    t.fill(roxo)
    pygame.draw.rect(t, azul, (20, 50, larg, 70))
    larg = larg * mem / 100
    pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
    total = memoria.total_gb()
    texto_titulo = "Consumo de memoria ( Total: " + str(total) + " GB):"
    texto_final = font.render(texto_titulo, 1, indigo)
    t.blit(texto_final, (20, 10))
    tela.blit(t, (0, 2 * altura_tela / 3))


def iniciar_app(): #inicio do loop para a tela pygame
    pygame.display.init()

    s1 = Surface((largura_tela, altura_tela/3))
    s2 = Surface((largura_tela, altura_tela/4))

    clock = pygame.time.Clock()
    contador = 60

    terminou = False

    opcao = 1
    while not terminou:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    opcao = 1
                elif event.key == pygame.K_2:
                    opcao = 2
                elif event.key == pygame.K_3:
                    opcao = 3
                elif event.key == pygame.K_4:
                    opcao = 4
                elif event.key == pygame.K_5:
                    opcao = 5

        if contador == 60:
            tela.fill(roxo)
            menu_display(s1)

            if opcao == 1:
                info_cpu_display(s1)
                cpu_display(s1)
            elif opcao == 2:
                info_memoria_display(s1)
                memoria_display(s1)
            elif opcao == 3:
                info_disco_display(s1)
                disks_display(s1)
            elif opcao == 4:
                info_rede_display(s1)
            elif opcao == 5:
                info_resumo_display(s1)
            contador = 0

        pygame.display.update()
        clock.tick(60)
        contador = contador + 1

    pygame.display.quit()


if __name__ == '__main__':
    iniciar_app()
