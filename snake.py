#####################################################
#        Snake en Python 0.2 - testing Pygame       #
#               Taller Python                       # 
#                                                   #
#   Code:   Alvaro Carrillanca P. (A.K.A. kvtral)   #
#           alvaro.carrillanca(at)gmail(dot)com     #
#           https://github.com/kvtral/snake         #
#   Sounds: kvtral (made in Beep Box)               #                                
#           https://beepbox.co                      #    
#                                                   #
#   Music:  Patrick de Arteaga.                     #
#   https://patrickdearteaga.com/es/musica-arcade/  #
#   Licenced by creative commons                    #
#                                                   #
#####################################################

import pygame, random, time, os

def loadImage (name):
    path = os.path.join('',name)
    return pygame.image.load(path).convert()

pygame.init()

intro = True

icono = pygame.image.load('icon.jpg') # No me carga el icono en la barra de la ventana
pygame.display.set_icon(icono)

# Configuracion del juego

pygame.display.set_caption("S.N.A.K.E.  v0.4")
ancho = 800
alto = 600
display =  pygame.display.set_mode((ancho, alto))
bgDisplay = loadImage('fondo.jpg')
display.blit(bgDisplay, [0,0])

clock = pygame.time.Clock()
snakeSize = 20
fuente = pygame.font.SysFont('ka1.ttf', 35)

def puntos (score):
    txt = fuente.render(str(score), True, (255,255,255))
    display.blit (txt, [280, 15])      

def pausa ():
    pausado = True
    pulsarSound = pygame.mixer.Sound('pause.ogg')
    pulsarSound.set_volume(0.50)
    pulsarSound.play(0)
    pulsarSound.stop
    while (pausado):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit ()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pausado = False
                    pulsarSound.play(0)
                    pulsarSound.stop
                elif event.key == pygame.K_m:
                    Juego()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit
                    quit ()
        bgGame = loadImage('pausa.jpg')
        display.blit (bgGame, [0,0])
        pygame.display.update()
        clock.tick(15)


def introGame():
    intro = True
    pulsarSound = pygame.mixer.Sound('intro.ogg')
    pulsarSound.set_volume(0.20)
    pulsarSound.play(10)
    while (intro):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit ()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    intro = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit
                    quit ()
        bgGame = loadImage('intro.jpg')
        display.blit (bgGame, [0,0])
        pygame.display.update()
        clock.tick(5)
    pulsarSound.stop()
        
def fin(gameOver):
    pulsarSound = pygame.mixer.Sound('gameOver.ogg')
    pulsarSound.set_volume(0.50)
    pulsarSound.play(0)
    pulsarSound.stop
    
    while (gameOver):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit ()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    gameOver = False
                    Juego()
                elif event.key == pygame.K_n:
                    gameOver = False
                    Juego (False)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit
                    quit ()
        bgGame = loadImage('gameover.jpg')
        display.blit (bgGame, [0,0])
        pygame.display.update()       

def snake (snakeSize,snakeLista):
    for i in snakeLista:
        pygame.draw.rect(display, (0,0,0), [i[0], i[1], snakeSize, snakeSize])

def txtObjeto (txt, color):
    txtDisplay = fuente.render(txt, True, color)
    return txtDisplay, txtDisplay.get_rect()

def screenMsg (msg, color, showY=0):
    textSur, textRect = txtObjeto(msg, color)
    textRect.center = (ancho / 2), (alto / 2) + showY
    display.blit (textSur, textRect)
    
    #txtToScreen = fuente.render(msg, True, color)

def Juego(intro=True):
    
    speed = 1
    fps = 10
    
    gameExit = False
    gameOver = False
    
    # Punto Inicial de la Serpiente
    moverX = 300
    moverY = 300

    #Interrupcion con teclas de direccion
    cambioX = 0
    cambioY = 0

    # Serpiente
    snakeLista = []
    snakeLen = 1
    scored = 0

    #Variable M. Roja
    rojaX = round(random.randrange(70,ancho-70)/20.0) * snakeSize
    rojaY = round(random.randrange(70,alto-70)/20.0) * snakeSize
    
    #Inicial M.Verde
    verdeX = round(random.randrange(70,ancho-70)/20.0) * snakeSize
    verdeY = round(random.randrange(70,alto-70)/20.0) * snakeSize    
    
    #Inicial M.Morada
    
    moradaX = round(random.randrange(70,ancho-70)/20.0) * snakeSize
    moradaY = round(random.randrange(70,alto-70)/20.0) * snakeSize
   
   # Tengo la idea de generar un numero aleatorio para la aparicion de Manzanas Verdes y Moradas 
   # extra = int(round(random.randrange(0,100)))
    if (intro):
        introGame()

    #Sonidos
    pulsarSound = pygame.mixer.Sound('juego.ogg')
    pulsarSound.set_volume(0.20)
    pulsarSound.play(20)
    
    
    while not gameExit:
        
        """ while (gameOver):
            
         #   display.blit(bgDisplay,[0,0])
            pulsarSound.stop()
            screenMsg("Game Over!", (255,0,0), -50)
            screenMsg("Para salir presione 'Q'",(0,0,0), 50)
            pygame.display.update()
            
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                    if event.type == pygame.K_c:
                        gameOver = False
                        Juego()
         """        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cambioX = -snakeSize
                    cambioY = 0
                elif event.key == pygame.K_RIGHT:
                    cambioX = snakeSize  
                    cambioY = 0   
                elif event.key == pygame.K_UP:
                    cambioY = -snakeSize
                    cambioX = 0
                elif event.key == pygame.K_DOWN:
                    cambioY = snakeSize
                    cambioX = 0
                elif event.key == pygame.K_p:
                    pulsarSound.set_volume(0.0)
                    pausa()
                    pulsarSound.set_volume(0.20)
                    
        if moverX >= ancho-60 or moverX < 60 or moverY >= alto-60 or moverY < 60:
            pulsarSound.stop()
            fin(True)

        moverX +=  cambioX
        moverY +=  cambioY
        display.blit(bgDisplay, [0,0])
        
        pygame.draw.rect(display, (255,0,0), [rojaX,rojaY,snakeSize,snakeSize])
         
        
        #if extra % 5 == 0:
        pygame.draw.rect(display, (0,255,0), [verdeX,verdeY,snakeSize,snakeSize])
        #elif extra % 3 == 0 and moradaEat == 1:
        pygame.draw.rect(display, (200,0,255), [moradaX,moradaY,snakeSize,snakeSize])
        
        snakeHead = []
        snakeHead.append(moverX)
        snakeHead.append(moverY)
        snakeLista.append(snakeHead)

        if len(snakeLista) > snakeLen:
            del snakeLista[0]

        #Evalua si la cabeza de la serpiente "choca" con alguna parte del cuerpo
        ########################################################################
        #                     CAMBIO IMPORTANTE PENDIENTE!                     #
        #      Evitar que "choque" cuando se presiona "hacia atras"            #
        ########################################################################
        for eachSegment in snakeLista[:-1]:
            if eachSegment == snakeHead:
                pulsarSound.stop()
                fin (True)

        snake (snakeSize,snakeLista)
        puntos (scored)
        txt = fuente.render( str (speed), True, (255,255,255))
        display.blit (txt, [700, 15])   
        pygame.display.update()

        if moverX == rojaX and moverY == rojaY:
            pygame.mixer_music.load("RojaEat.ogg")
            pygame.mixer_music.play(0)
            rojaX = round(random.randrange(70,ancho-70)/20.0) * snakeSize
            rojaY = round(random.randrange(70,alto-70)/20.0) * snakeSize
            snakeLen += 1
            scored += 1         
            if scored % 3 == 0:
                speed += 1
                fps += 1

        if moverX == verdeX and moverY == verdeY:
            pygame.mixer_music.load("VerdeEat.ogg")
            pygame.mixer_music.play(0)
            verdeX = round(random.randrange(70,ancho-70)/20.0) * snakeSize
            verdeY = round(random.randrange(70,alto-70)/20.0) * snakeSize
            speed += 1           
            
                
        if moverX == moradaX and moverY == moradaY:
            pygame.mixer_music.load("MoradaEat.ogg")
            pygame.mixer_music.play(0)
            moradaX = round(random.randrange(70,ancho-70)/20.0) * snakeSize
            moradaY = round(random.randrange(70,alto-70)/20.0) * snakeSize
            scored += 3
            snakeLen += 10


        clock.tick(fps)

Juego()

pygame.quit()
