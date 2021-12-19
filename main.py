import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (i * self.cell_size + self.left, j * self.cell_size + self.top, self.cell_size,
                                  self.cell_size), 2)


size = width, height = 800, 400
screen = pygame.display.set_mode(size)
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = list(event.pos)
            asd = width // pos[0]
            print(asd)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
