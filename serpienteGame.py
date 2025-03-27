import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Definir colores
blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la pantalla
ancho_pantalla = 600
alto_pantalla = 400

# Inicializar pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Serpiente con Bordes Infinitos')

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Tamaño del bloque de la serpiente y velocidad
tamano_bloque = 20
velocidad_serpiente = 15

# Fuentes
fuente_estilo = pygame.font.SysFont("bahnschrift", 25)
fuente_puntos = pygame.font.SysFont("comicsansms", 35)


def mostrar_puntos(puntos):
    valor = fuente_puntos.render("Puntos: " + str(puntos), True, amarillo)
    pantalla.blit(valor, [0, 0])


def dibujar_serpiente(tamano_bloque, lista_serpiente, color_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(pantalla, color_serpiente, [
                         x[0], x[1], tamano_bloque, tamano_bloque])


def mensaje(msg, color):
    mesg = fuente_estilo.render(msg, True, color)
    pantalla.blit(mesg, [ancho_pantalla / 6, alto_pantalla / 3])


# Colores de la comida
colores_comida = [amarillo, rojo, verde,
                  (128, 0, 128), (165, 42, 42)]  # Incluye morado y marrón


def juego():
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x1 = ancho_pantalla / 2
    y1 = alto_pantalla / 2

    # Cambio en la posición
    x1_cambio = 0
    y1_cambio = 0

    # Cuerpo de la serpiente
    lista_serpiente = []
    largo_serpiente = 1

    # Posición de la comida
    comida_x = round(random.randrange(0, ancho_pantalla -
                     tamano_bloque) / tamano_bloque) * tamano_bloque
    comida_y = round(random.randrange(0, alto_pantalla -
                     tamano_bloque) / tamano_bloque) * tamano_bloque

    # Color inicial de la comida y la serpiente
    color_comida = random.choice(colores_comida)
    color_serpiente = verde

    while not game_over:

        while game_close == True:
            pantalla.fill(azul)
            mensaje("Perdiste! Presiona Q-Salir o C-Jugar de nuevo", rojo)
            mostrar_puntos(largo_serpiente - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_cambio == 0:
                    x1_cambio = -tamano_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_RIGHT and x1_cambio == 0:
                    x1_cambio = tamano_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_UP and y1_cambio == 0:
                    y1_cambio = -tamano_bloque
                    x1_cambio = 0
                elif event.key == pygame.K_DOWN and y1_cambio == 0:
                    y1_cambio = tamano_bloque
                    x1_cambio = 0

        # Bordes infinitos
        if x1 >= ancho_pantalla:
            x1 = 0
        elif x1 < 0:
            x1 = ancho_pantalla - tamano_bloque
        if y1 >= alto_pantalla:
            y1 = 0
        elif y1 < 0:
            y1 = alto_pantalla - tamano_bloque

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, color_comida, [
                         comida_x, comida_y, tamano_bloque, tamano_bloque])

        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_serpiente.append(cabeza_serpiente)

        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        for x in lista_serpiente[:-1]:
            if x == cabeza_serpiente:
                game_close = True

        dibujar_serpiente(tamano_bloque, lista_serpiente, color_serpiente)
        mostrar_puntos(largo_serpiente - 1)

        pygame.display.update()

        # Si la serpiente come la comida
        if x1 == comida_x and y1 == comida_y:
            # Cambiar color de la serpiente al color de la comida actual
            color_serpiente = color_comida

            # Generar nueva posición y color para la comida
            comida_x = round(random.randrange(
                0, ancho_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque
            comida_y = round(random.randrange(
                0, alto_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque
            color_comida = random.choice(colores_comida)

            largo_serpiente += 1

        reloj.tick(velocidad_serpiente)

    pygame.quit()
    quit()


juego()
