import pygame, os
from pygame.locals import *
from sys import exit
from random import *

pygame.init()

# Pasta de assets
assets = os.path.join(os.getcwd(), 'Assets') #Para definir onde estão os assets, os.getcwd() pega a pasta raiz

# Musicas e Sons
pygame.mixer.music.set_volume(0.1) #valores entre 0 e 1 para o som da música
musica_de_fundo = pygame.mixer.music.load(os.path.join(assets, 'BoxCat Games - CPU Talk.mp3'))
pygame.mixer.music.play(-1) # -1 começa a tocar denovo (em looping)

Barulho_colisao = pygame.mixer.Sound(os.path.join(assets, 'smw_coin.wav'))
Barulho_colisao.set_volume(1) #valores entre 0 e 1 para o som deste barulho

# Variáveis
Largura_tela = int(input("Digite a largura da tela: ")) # 640
Altura_tela = int(input("Digite a altura da tela: ")) # 480
red = (255, 0, 0)
blue = (0,0,255)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)
larg_quad = 20
alt_quad = 20
meiox = int(Largura_tela/2 - larg_quad/2)
meioy = int(Altura_tela/2 - alt_quad/2)
y = meioy
x = meiox
x_maca = randint(0,(Largura_tela-larg_quad))
y_maca = randint(0,Altura_tela-alt_quad)
x_maca2 = randint(0,(Largura_tela-larg_quad))
y_maca2 = randint(0,Altura_tela-alt_quad)
x_maca3 = randint(0,(Largura_tela-larg_quad))
y_maca3 = randint(0,Altura_tela-alt_quad)
maca2_flag = False
maca3_flag = False
Spawn_maca_esp = 0
flag_fechar_vertical = False
flag_fechar_horizontal = False
# Pontos
pontos = 0
x_text = 400
y_text = 40

# Fonte
fonte = pygame.font.SysFont('arial', 40, True, True) #1- qual font, tamanho, negrito, itálico
#pygame.font.get_fonts() Para saber quais fontes existem no pygame
#https://freemusicarchive.org/music/BoxCat_Games - Site Para Musicas
#https://themushroomkingdom.net/media/smw/wav - Site Para Sons

tela = pygame.display.set_mode((Largura_tela, Altura_tela))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock() # Para usar o Clock

# Cobra
velocidade = 10
x_controle = velocidade
y_controle = 0

lista_cobra = []
comprimento_inicial = 5

# Funções
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x,y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(tela, green, (XeY[0], XeY[1], larg_quad, alt_quad))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x, y, lista_cobra, lista_cabeca, x_maca, y_maca, x_maca2, y_maca2, morreu, velocidade, x_maca3, y_maca3, maca2_flag, maca3_flag, Spawn_maca_esp, flag_fechar_horizontal, flag_fechar_vertical
    pontos = 0
    comprimento_inicial = 5
    x = meiox
    y = meioy
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(0,(Largura_tela-larg_quad))
    y_maca = randint(0,Altura_tela-alt_quad)

    velocidade = 10
    morreu = False
    flag_fechar_vertical = False
    flag_fechar_horizontal = False
    maca2_flag = False
    maca3_flag = False
    Spawn_maca_esp = 0

def maca2_spawn():
    global x_maca, x_maca2, y_maca, y_maca2
    x_maca2 = randint(0,(Largura_tela-larg_quad))
    y_maca2 = randint(0,Altura_tela-alt_quad)
    while x_maca == x_maca2 and y_maca == y_maca2:
        x_maca2 = randint(0,(Largura_tela-larg_quad))
        y_maca2 = randint(0,Altura_tela-alt_quad)

def maca3_spawn():
    global x_maca, x_maca2, y_maca, y_maca2, x_maca3, y_maca3
    x_maca3 = randint(0,(Largura_tela-larg_quad))
    y_maca3 = randint(0,Altura_tela-alt_quad)
    while (x_maca == x_maca3 and y_maca == y_maca3) or (x_maca2 == x_maca3 and y_maca2 == y_maca3):
        x_maca3 = randint(0,(Largura_tela-larg_quad))
        y_maca3 = randint(0,Altura_tela-alt_quad)
    
morreu = False

# While Principal
while True:
    relogio.tick(30) #quantos frames eu quero por segundo
    tela.fill(white)
    mensagem = ('Pontos : {}'.format(pontos))
    texto_formatado = fonte.render(mensagem, True, black) #mensagem, antialised(serrilhamento), cor
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Movimentação porém não dá para segurar
    
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
                
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
                
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
                
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x = x + x_controle
    y = y + y_controle

    if y > Altura_tela - 10:
        y = 0 + 10
    if y < 0 + 10:
        y = Altura_tela - 10
    if x > Largura_tela - 10:
        x = 0 + 10
    if x < 0 + 10:
        x = Largura_tela - 10
        
    
    if pontos >= 25:
        fechar_right = pygame.draw.rect(tela, black, ((Largura_tela-6),0,5, Altura_tela)) # 6 (devido ao tamanhoX que 5 + 1 de espaçamento)
        fechar_left = pygame.draw.rect(tela, black, ((1),0,5, Altura_tela))              # 1 de espaçamento e 5 de tamanhoX
        flag_fechar_horizontal = True
    if pontos >= 50:
        fechar_bottom = pygame.draw.rect(tela, black, (0,(Altura_tela-6),Largura_tela, 5)) # 6 (devido ao tamanhoX que 5 + 1 de espaçamento)
        fechar_top = pygame.draw.rect(tela, black, (0,1,Largura_tela, 5))              # 1 de espaçamento e 5 de tamanhoX
        flag_fechar_vertical = True
    
    cobra = pygame.draw.rect(tela, green, (x,y,larg_quad, alt_quad))
    maca = pygame.draw.rect(tela, red, (x_maca,y_maca,larg_quad, alt_quad))
    if maca2_flag == True:
        maca2 = pygame.draw.rect(tela, blue, (x_maca2,y_maca2,larg_quad, alt_quad))
    if maca3_flag == True:
        maca3 = pygame.draw.rect(tela, black, (x_maca3,y_maca3,larg_quad, alt_quad))
    
    

    lista_cabeca = []
    lista_cabeca.append(x)
    lista_cabeca.append(y)
    
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:                         # Morrer padrao
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! \nPressione a tecla - R -  para Jogar Novamente!'
        texto_formatado = fonte2.render(mensagem, True, black)
        ret_texto = texto_formatado.get_rect()
        
        morreu = True
        
        while morreu:
            tela.fill(white)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN: #Quando eu pressionar alguma tecla
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (Largura_tela//2, Altura_tela//2)
            tela.blit(texto_formatado, ret_texto) # // retorna o valor inteiro da divisão            
            pygame.display.update()
            
    if flag_fechar_horizontal == True:
        if cobra.colliderect(fechar_right) or cobra.colliderect(fechar_left) :                         # Morrer Borda Horizontal
            fonte2 = pygame.font.SysFont('arial', 20, True, True)
            mensagem = 'Game Over! \nPressione a tecla - R -  para Jogar Novamente!'
            texto_formatado = fonte2.render(mensagem, True, black)
            ret_texto = texto_formatado.get_rect()
        
            morreu = True
        
            while morreu:
                tela.fill(white)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN: #Quando eu pressionar alguma tecla
                        if event.key == K_r:
                            reiniciar_jogo()

                ret_texto.center = (Largura_tela//2, Altura_tela//2)
                tela.blit(texto_formatado, ret_texto) # // retorna o valor inteiro da divisão            
                pygame.display.update()
                
                
    if flag_fechar_vertical == True:
        if cobra.colliderect(fechar_top) or cobra.colliderect(fechar_bottom):                         # Morrer Borda Vertical
            fonte2 = pygame.font.SysFont('arial', 20, True, True)
            mensagem = 'Game Over! \nPressione a tecla - R -  para Jogar Novamente!'
            texto_formatado = fonte2.render(mensagem, True, black)
            ret_texto = texto_formatado.get_rect()
        
            morreu = True
        
            while morreu:
                tela.fill(white)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN: #Quando eu pressionar alguma tecla
                        if event.key == K_r:
                            reiniciar_jogo()

                ret_texto.center = (Largura_tela//2, Altura_tela//2)
                tela.blit(texto_formatado, ret_texto) # // retorna o valor inteiro da divisão            
                pygame.display.update()
    
    if cobra.colliderect(maca): #colisão
        x_maca = randint(0,(Largura_tela-larg_quad))
        y_maca = randint(0,Altura_tela-alt_quad)
        pontos += 1
        Barulho_colisao.play()
        comprimento_inicial += 1
        Spawn_maca_esp += 1
        
    if maca2_flag == True:   
        if cobra.colliderect(maca2): #colisão Maça 2
            maca2_spawn()
            pontos += 5
            Barulho_colisao.play()
            comprimento_inicial += 1
            velocidade += 2
            maca2_flag = False
            Spawn_maca_esp = 0
    
    if maca3_flag == True:    
        if cobra.colliderect(maca3): #colisão Maça 3
            maca3_spawn()
            pontos -= 1
            Barulho_colisao.play()
            comprimento_inicial += 1
            velocidade -= 0.5 
            maca3_flag = False
            Spawn_maca_esp = 0   
            
    if Spawn_maca_esp == 5:
        maca2_flag = True
        
    if Spawn_maca_esp == 10:
        maca3_flag = True

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado,(x_text,y_text))
    pygame.display.update()
