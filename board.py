import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.values = [[None] * width for _ in range(height)]
        self.left = 10
        self.top = 20
        self.cell_size = 34

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        if self.left <= mouse_pos[0] <= self.width * self.cell_size and \
                self.top <= mouse_pos[1] <= self.height * self.cell_size:
            x = mouse_pos[0]
            y = mouse_pos[1]
            i = (x - self.left) // self.cell_size
            j = (y - self.top) // self.cell_size
            return i, j
        return None

    def render(self, screen):
        pygame.draw.rect(screen, 'white',
                         (self.left, self.top, self.width * self.cell_size, self.height * self.cell_size), 1)

        for i in range(self.width):
            for j in range(self.height):
                x = self.left + i * self.cell_size
                y = self.top + j * self.cell_size
                pygame.draw.rect(screen, 'grey',
                                 (x, y, self.cell_size, self.cell_size), 1)

        for j in range(self.width):
            for i in range(self.height):
                x = self.left + j * self.cell_size + 1
                y = self.top + i * self.cell_size + 1
                if self.values[i][j] is not None:
                    pygame.draw.rect(screen, self.values[i][j],
                                     (x, y, self.cell_size - 2, self.cell_size - 2), 0)


def change_value(board, cell):
    i, j = cell
    board.values[j][i] += 1
    board.values[j][i] %= 2


def change_line(board, cell):
    i, j = cell
    board.values[j][i] += 1
    board.values[j][i] %= 2
    for k in range(board.width):
        board.values[j][k] += 1
        board.values[j][k] %= 2
    for l in range(board.height):
        board.values[l][i] += 1
        board.values[l][i] %= 2


size = width, height = 500, 642
screen = pygame.display.set_mode(size)
board = Board(10, 20)
board.set_view(0, 0, 32)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
