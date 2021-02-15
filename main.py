import pygame
from random import choice

W, H = 10, 20
TILE = 34
GAME_RES = W * TILE, H * TILE
FPS = 60

pygame.init()
sc = pygame.display.set_mode(GAME_RES)
game_sc = pygame.Surface(GAME_RES)
clock = pygame.time.Clock()
rotate = False

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)

figure = choice(figures)
t, t1 = 0, 40

while True:
    sc.blit(game_sc, (0, 0))
    game_sc.fill(pygame.Color("black"))
    px = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate = True
            elif event.key == pygame.K_LEFT:
                px = -1
            elif event.key == pygame.K_RIGHT:
                px = 1
            elif event.key == pygame.K_DOWN:
                t1 = 20

    for i in range(4):
        figure[i].x += px
    t += 1
    if t > t1:
        t = 0
        for i in range(4):
            figure[i].y += 1
    center = figure[0]
    if rotate:
        if not figure == figures[1]:
            for i in range(4):
                x = figure[i].y - center.y
                y = figure[i].x - center.x
                figure[i].x = center.x - x
                figure[i].y = center.y + y
        rotate = False

    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_sc, "white", figure_rect)
    pygame.display.flip()
    clock.tick(FPS)

