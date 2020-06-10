import pygame, random, time, os

def loadImage (name):
    path = os.path.join('',name)
    return pygame.image.load(path).convert()

pygame.init() 

icono = pygame.image.load('icon.jpg')
pygame.display.set_icon(icono)

# Configuracion del juego

pygame.display.set_caption("Serpiente")
ancho = 800
alto = 600
display =  pygame.display.set_mode((ancho, alto))
bgDisplay = loadImage('fondo.jpg')
display.blit(bgDisplay, [0,0])

speed = pygame.time.Clock()
snakeSize = 20
fuente = pygame.font.SysFont('ka1.ttf', 35)

def puntos (score):
    txt = fuente.render(str(score), True, (255,255,255))
    display.blit (txt, [280, 15])      

def pausa ():
    pausado = True
    while (pausado):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit ()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit
                    quit ()
        bgGame = loadImage('pausa.jpg')
        display.blit (bgGame, [0,0])
        pygame.display.update()
        speed.tick(15)

def introGame():
    intro = True
    while (intro):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit ()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit
                    quit ()
        bgGame = loadImage('intro.jpg')
        display.blit (bgGame, [0,0])
        pygame.display.update()
        speed.tick(5)
        
def fin(gameOver):
    while (gameOver):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit ()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                    gameOver = False
                    Juego()
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

def Juego():
    
    level = 1
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

    #Variable Manzana
    ManzaX = round(random.randrange(70,ancho-70)/20.0) * snakeSize
    ManzaY = round(random.randrange(70,alto-70)/20.0) * snakeSize
    
    #Sonidos
    pulsarSound = pygame.mixer.Sound('song.ogg')
    pulsarSound.set_volume(0.20)
    pulsarSound.play(20)
    
    introGame()
    
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
        
        pygame.draw.rect(display, (255,0,0), [ManzaX,ManzaY,snakeSize,snakeSize])
        
        snakeHead = []
        snakeHead.append(moverX)
        snakeHead.append(moverY)
        snakeLista.append(snakeHead)

        if len(snakeLista) > snakeLen:
            del snakeLista[0]

        #Evaluar si la cabeza de la serpiente "choca" con alguna parte del cuerpo
        for eachSegment in snakeLista[:-1]:
            if eachSegment == snakeHead:
                pulsarSound.stop()
                fin (True)


        snake (snakeSize,snakeLista)
        puntos (snakeLen-1)
        txt = fuente.render( str (level), True, (255,255,255))
        display.blit (txt, [700, 15])   
        pygame.display.update()

        if moverX == ManzaX and moverY == ManzaY:
            pygame.mixer_music.load("eat.ogg")
            pygame.mixer_music.play(0)
            ManzaX = round(random.randrange(70,ancho-70)/20.0) * snakeSize
            ManzaY = round(random.randrange(70,alto-70)/20.0) * snakeSize
            snakeLen += 1
            
            if len(snakeLista) % 4 == 0:
                level += 1
                fps += 2

        speed.tick(fps)

Juego()

pygame.quit()
