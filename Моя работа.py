import pygame

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = input().split()
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Крест')


    def draw(screen):
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), width=5)


    draw(screen)
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
