import pygame
from pygame import mixer
from pathlib import Path
from random import randint
import math

ruta = Path(__file__).parent / "materiales"

# Inicializo el juego
pygame.init()

# Creo la pantalla, seteo el título e ícono
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders Piggy's Version")
icono = pygame.image.load(ruta / "cerdito_icon.png")
pygame.display.set_icon(icono)

# Fondo de pantalla
fondo = pygame.image.load(ruta / "Fondo.jpg")  

# Agrego música de fondo
mixer.music.load(ruta / "MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Creo y posiciono al jugador
img_jugador = pygame.image.load(ruta / "cerdito.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Creo y configuro a los enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 7
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load(ruta / "zorro.png"))
    enemigo_x.append(randint(0, 736))
    enemigo_y.append(randint(50, 200))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)

# Configuración de la bala
img_bala = pygame.image.load(ruta / "bala_heart.png")  
balas = []

# Seteo del puntaje, fuente y ubicación en la pantalla
puntaje = 0
fuente = pygame.font.Font(None, 32)
texto_x = 10
texto_y = 10

# Cargo imagen de game over
game_over_img = pygame.image.load(ruta / "game_over.png")

# Funciones para mostrar los elementos en pantalla
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# Función para mostrar las vidas 
def mostrar_vidas(cantidad):
    for i in range(cantidad):
        pantalla.blit(img_vida, (750 - i * 40, 10))  # Ajusta la posición de los iconos

# Función para mostrar el mensaje de Game Over
def mostrar_game_over():
    pantalla.blit(game_over_img, (144, 44)) 

# Detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    return distancia < 27

# Inicializo las vidas y asigno imagen
vidas = 5
img_vida = pygame.image.load(ruta / "tocino.png") 

# Función principal
se_ejecuta = True
while se_ejecuta:
    # Muestra el fondo
    pantalla.blit(fondo, (0, 0))

    # Distintas reacciones para cada evento con el teclado
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound(ruta / "disparo.mp3")
                sonido_bala.play()
                nueva_bala = {"x": jugador_x, "y": jugador_y, "velocidad": -5}
                balas.append(nueva_bala)
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                jugador_x_cambio = 0

    # Actualización de posición del jugador
    jugador_x += jugador_x_cambio
    jugador_x = max(0, min(jugador_x, 736))  
    # Muestra y mueve a los enemigos
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]
        if enemigo_x[e] <= 0 or enemigo_x[e] >= 736:
            enemigo_x_cambio[e] *= -1
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # Verifico si el enemigo toca al jugador
        if hay_colision(jugador_x, jugador_y, enemigo_x[e], enemigo_y[e]):
            vidas -= 1  
            enemigo_x[e] = randint(0, 736) 
            enemigo_y[e] = randint(50, 200)

            # Verificar si aún quedan vidas
            if vidas == 0:
                mostrar_game_over()
                pygame.display.update()
                pygame.time.wait(5000)  # Espera 5 segundos antes de cerrarse
                se_ejecuta = False  # Termina el juego
        
        # Dibuja al enemigo en su nueva posición
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # mueve las balas y detecta colisiones
    for bala in balas[:]:
        bala["y"] += bala["velocidad"]
        if bala["y"] < 0:
            balas.remove(bala)
        else:
            pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
            # Verifica colisiones con enemigos
            for e in range(cantidad_enemigos):
                if hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"]):
                    sonido_colision = mixer.Sound(ruta / "Golpe.mp3")
                    sonido_colision.play()
                    if bala in balas:
                        balas.remove(bala)
                    puntaje += 1
                    enemigo_x[e] = randint(0, 736)
                    enemigo_y[e] = randint(50, 200)

    # muestra al jugador, puntaje y vidas restantes
    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)
    mostrar_vidas(vidas) 

    # Actualiza la pantalla
    pygame.display.update()
