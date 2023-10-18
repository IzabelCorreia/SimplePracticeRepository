# COFIGURAÇÕES INICIAIS 
import random
import pygame

pygame.init()
pygame.display.set_caption("Snake Game")
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

tamQuad = 10

def gerarFood():
    foodX = round(random.randrange(0, largura - tamQuad)/20.0)*20.0
    foodY = round(random.randrange(0, altura - tamQuad)/20.0)*20.0
    return foodX, foodY


def drawFood(tamanho, FoodX, FoodY):
    pygame.draw.rect(tela, red, [FoodX, FoodY, tamanho, tamanho])


def drawSnake(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, white, [pixel[0], pixel[1], tamanho, tamanho])


def drawPoints(points):
    font = pygame.font.SysFont("Helvetiva", 25)
    text = font.render(f"Pontos: {points}", True, green)
    tela.blit(text, [1,1])

def selctVel(tecla):
    if tecla == pygame.K_DOWN:
        veloX = 0
        veloY = tamQuad
    if tecla == pygame.K_UP:
        veloX = 0
        veloY = -tamQuad
    if tecla == pygame.K_RIGHT:
        veloX = tamQuad
        veloY = 0
    if tecla == pygame.K_LEFT:
        veloX = -tamQuad
        veloY = 0 
    return veloX, veloY
# CRIAR LOOP
def rodaGame():

    x = largura / 2
    y = altura / 2

    veloX = 0
    veloY = 0

    tamSnake = 1
    pixels = []

    FoodX, FoodY  = gerarFood()

    running = True
    while running:
        tela.fill(black)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            elif evento.type == pygame.KEYDOWN:
                veloX, veloY = selctVel(evento.key)
        
        drawFood(tamQuad, FoodX, FoodY)

        x += veloX
        y += veloY 

        pixels.append([x, y])
        if len(pixels) > tamSnake:
            del pixels[0]
        # se bateu nela mesma
        for pixel in pixels[-1]:
            if pixel == [x, y]:
                running = True


        drawSnake(tamQuad, pixels)       
        drawPoints(tamSnake - 1)

        pygame.display.update()
        
        # cria nova comida 
        if x == FoodX and y == FoodY:
            tamSnake += 1
            FoodX, FoodY = gerarFood()

        clock.tick(10)
rodaGame()