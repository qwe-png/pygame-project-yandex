import pygame
import random

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

class Path(Board):
    import pygame
    import random

    class LOL(AssertionError):
        pass

    if __name__ == '__main__':
        try:

            # инициализация Pygame:
            pygame.init()
            pygame.display.set_caption('Дичь')
            # размеры окна:
            size = width, height = 300, 200
            # screen — холст, на котором нужно рисовать:
            screen = pygame.display.set_mode(size)
            screen.fill(pygame.Color('white'))
            s = 0
            w = 0
            g = 0
            u = 0
            r = 0
            m = 0
            provershik = 0
            for i in range(300):
                w = 30
                provershik += 1
                if u == 1:
                    s -= 15
                u = 0
                if provershik % 11 == 0:
                    provershik = 0
                    w = 15
                    g += 17
                    u = 1
                    s = 0
                    r += 1
                    m += 1
                    if r % 2 == 0:
                        s -= 16
                screen.fill(pygame.Color('red'), (s, g, w, 15))
                s += 32
                if u % 2 == 1:
                    screen.fill(pygame.Color('red'), (0, g, w, 15))
            # формирование кадра:
            # команды рисования на холсте
            # ...
            # ...
            # смена (отрисовка) кадра:
            pygame.display.flip()
            # ожидание закрытия окна:

            while pygame.event.wait().type != pygame.QUIT:
                pass
            # завершение работы:
            pygame.quit()
        except ValueError:
            print('Неправильный формат ввода')
        except LOL:
            print('Число n не кратно числу a')
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
#коментарий`