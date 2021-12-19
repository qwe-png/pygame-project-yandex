import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.set_view()

    # настройка внешнего вида
    def set_view(self, left=10, top=10, cell_size=30):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        w = pygame.Color(255, 255, 255)
        cs = self.cell_size
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, w, (x * cs + self.left, y * cs + self.top, cs, cs), 1)

    def get_cell(self, mouse_pos):
        b_w = self.width * self.cell_size
        b_h = self.height * self.cell_size
        if self.left < mouse_pos[0] < self.left + b_w:
            if self.top < mouse_pos[1] < self.top + b_h:
                cell_coords = (mouse_pos[0] - self.top) // self.cell_size + 1, \
                              (mouse_pos[1] - self.left) // self.cell_size + 1
                return cell_coords
        return None

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Игра')

    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color("blue"))
    x, y = 800, 800
    board = Board(x, y)
    board.set_view(300, 300, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
