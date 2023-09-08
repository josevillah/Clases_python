import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la pantalla
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de la Serpiente")

# Definir los colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Definir las variables de la serpiente
snake_size = 10
snake_speed = 15

# Función para mostrar el mensaje en la pantalla
def message(msg, color, font_size):
    font = pygame.font.SysFont(None, font_size)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width / 6, screen_height / 3])

# Función principal del juego
def gameLoop():
    # Definir las variables del juego
    game_over = False
    game_close = False

    # Inicializar la posición de la serpiente
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0       
    y1_change = 0

    # Inicializar la posición de la comida
    foodx = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0

    # Inicializar la longitud de la serpiente
    snake_List = []
    Length_of_snake = 1

    # Bucle principal del juego
    while not game_over:

        # Si el juego se ha cerrado, mostrar el mensaje
        while game_close == True:
            screen.fill(white)
            message("Has perdido. Presiona Q para salir o C para jugar de nuevo", red, 40)
            pygame.display.update()

            # Comprobar si el jugador quiere salir o jugar de nuevo
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Mover la serpiente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        # Comprobar si la serpiente ha chocado con los bordes
        # if x1 >= screen_width or x1 < 0