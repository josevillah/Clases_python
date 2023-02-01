import pygame
import random
import math
from pygame import mixer
import io
from pathlib import Path

# Crear ejecutable pyinstaller --clean --onefile --windowed nombre.py

#inicializar a pygame
pygame.init()

# crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

url = Path('C:\Programacion\Clases_python\Dia 10 juego espacial')



#Titulo e Icono
pygame.display.set_caption('Invasión Espacial')
icono = Path(url,'cohete.png')
icono = pygame.image.load(icono)
pygame.display.set_icon(icono)

fondo = Path(url,'espacio.png')
fondo = pygame.image.load(fondo)

# musica
musica = Path(url,'MusicaFondo.mp3')
mixer.music.load(musica)
mixer.music.set_volume(0.03)
mixer.music.play(-1)

# Variables del jugador
jugadorImg = Path(url,'jugador.png')
jugadorImg = pygame.image.load(jugadorImg)
jugador_x = 368
jugador_x_cambio = 0
jugador_y = 536
jugador_y_cambio = 0


def fuente_bytes(fuente):
    with open(fuente,'rb') as f:
        ttf_bytes = f.read()
        return io.BytesIO(ttf_bytes)

# Puntaje
puntaje = 0
letra = Path(url, 'freesansbold.ttf')
fuente_como_bytes = fuente_bytes(letra)
fuente = pygame.font.Font(fuente_como_bytes, 32)
# fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10



# mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255,255,255))
    pantalla.blit(texto, (x, y))

# el jugador
def jugador(x,y):
    pantalla.blit(jugadorImg, (x, y))


# Variables del Enemigo

enemigoImg = []
enemigo_x = []
enemigo_x_cambio = []
enemigo_y = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    enemigoPath = Path(url, 'enemigo.png')
    enemigoPath = pygame.image.load(enemigoPath)
    enemigoImg.append(enemigoPath)
    enemigo_x.append(random.randint(0,736))
    enemigo_x_cambio.append(0.3)
    enemigo_y.append(random.randint(0,200))
    enemigo_y_cambio.append(50)


# los enemigos
def enemigo(x, y, e):
    pantalla.blit(enemigoImg[e], (x, y))



# Variables de la Bala
balaImg = Path(url, 'bala.png')
balaImg = pygame.image.load(balaImg)
bala_x = 0
bala_x_cambio = 0
bala_y = 500
bala_y_cambio = 1.3
bala_visible = False


# Disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(balaImg, (x + 16, y + 10))


# Funcion detectar impacto
def impacto_bala(x_1, x_2, y_1, y_2):
    d = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if d < 27:
        return True
    else:
        return False

# Texto final del juego
fuente_final = pygame.font.Font(fuente_como_bytes, 60)

def texto_final():
    ff = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(ff, (100, 300))


# ciclo del juego
ejecucion = True

while ejecucion:

    # agregando color de la pantalla
    # pantalla.fill((205,144,228))

    #agregando imagen de fondo
    pantalla.blit(fondo, (0,0))

    # Iterar eventos
    for evento in pygame.event.get():

        # Cerrar Programa
        if evento.type == pygame.QUIT:
            ejecucion = False
        
        # eventos de movimiento cuando se presiona el boton w a s d
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                jugador_x_cambio = -0.4
            if evento.key == pygame.K_d:
                jugador_x_cambio = 0.4
            if evento.key == pygame.K_w:
                jugador_y_cambio = -0.4
            if evento.key == pygame.K_s:
                jugador_y_cambio = 0.4
            if evento.key == pygame.K_SPACE:
                disparo = Path(url, 'disparo.mp3')
                disparo = mixer.Sound(disparo)
                disparo.set_volume(0.03)
                disparo.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # eventos de movimiento cuando se suelta el boton w a s d
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a:
                jugador_x_cambio = 0
            if evento.key == pygame.K_d:
                jugador_x_cambio = 0
            if evento.key == pygame.K_w:
                jugador_y_cambio = 0
            if evento.key == pygame.K_s:
                jugador_y_cambio = 0

    # Movimientos del jugador
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio

    # Mantener dentro de los bordes x jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
    
    # Mantener dentro de los bordes y jugador
    if jugador_y <= 0:
        jugador_y = 0
    elif jugador_y >= 536:
        jugador_y = 536

    # Movimientos del enemigo
    for e in range(cantidad_enemigos):

        # Fin del Juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]
    
        # Mantener dentro de los bordes x ENEMIGO
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            if enemigo_y[e] < 700:
                enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # Mantener dentro de los bordes y ENEMIGO
        if enemigo_y[e] <= 0:
            enemigo_y_cambio[e] = 0.3
        elif enemigo_y[e] >= 700:
            enemigo_y_cambio[e] = -0.3
        
        # verificar impacto
        impacto = impacto_bala(enemigo_x[e], bala_x, enemigo_y[e], bala_y)
        if impacto:
            sonido_impacto = Path(url, 'Golpe.mp3')
            sonido_impacto = mixer.Sound(sonido_impacto)
            sonido_impacto.set_volume(0.03)
            sonido_impacto.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(0,200)
        
        enemigo(enemigo_x[e],enemigo_y[e], e)

    # Movimiento de la bala
    if bala_y <= -64:
        bala_y = jugador_y
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    # Mostrar al jugador con su posicion actual
    jugador(jugador_x,jugador_y)


    #mostrar Puntaje
    mostrar_puntaje(texto_x, texto_y)
    # Actualizar los cambios de la pantalla
    pygame.display.update()