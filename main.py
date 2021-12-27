import pygame
import math
import sys
import os

def terminate():
    #выход
    pygame.quit()
    sys.exit()


def surface(image, colorkey=None):
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


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
                pygame.draw.rect(screen, w, (x * cs + self.left, y * cs + self.top, cs, cs), 0)
                pygame.draw.rect(screen, pygame.Color(0, 0, 0), (x * cs + self.left + 1, y * cs + self.top + 1, cs - 1, cs - 1), 1)

        pygame.draw.rect(screen, (255, 255, 255), (0, 550, 600, 300), 0)


    def get_cell(self, mouse_pos):
        x = math.ceil((mouse_pos[0] - self.left) / self.cell_size) - 1
        y = math.ceil((mouse_pos[1] - self.top) / self.cell_size) - 1
        try:
            if x >= 0 and y >= 0:
                check = self.board[y][x]
                return x, y
            else:
                return None
        except IndexError:
            return None


    def on_click(self, cell_coords):
        print(cell_coords)


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


pygame.init()
pygame.display.set_caption('Игра')

size = width, height = 600, 800
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("orange"))

x, y = 5, 5
board = Board(x, y)
board.set_view(100, 100, 80)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    screen.fill(pygame.Color("orange"))
    board.render(screen)
    pygame.display.flip()
