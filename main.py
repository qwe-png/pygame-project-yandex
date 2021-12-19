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
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), 1)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('(' + str((int(event.pos[0]) - int(self.left)) // self.cell_size) + ', ' + str((int(event.pos[1]) - int(self.top)) // self.cell_size) + ')' if not ((int(event.pos[0]) - int(self.left)) // self.cell_size) < 0 and not ((int(event.pos[0]) - int(self.left)) // self.cell_size) >= self.width and not ((int(event.pos[1]) - int(self.top)) // self.cell_size) < 0 and not ((int(event.pos[1]) - int(self.top)) // self.cell_size) >= self.height else None)

def main():
    pygame.init()
    size = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инициализация игры')
    board = Board(5, 7)
    board.set_view(100, 100, 30)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()