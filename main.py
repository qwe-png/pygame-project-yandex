import pygame
import math
import sys
import os
from random import randint

from pygame.locals import *




schetchik_ochkov_dlya_pokupki_bashen = 0

randomazer = randint(0, 4)

provershit = 10

schitatel = 0

schetchik_kolichestva_dorozhek = 0

schetchik_kolichestva_stenok = 0


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


all_sprites = pygame.sprite.Group()

tower_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()

tower_image = load_image('tower.png')
tower_width = tower_height = 80

enemy_image = load_image("enemy.png")

path_image = load_image('path.png')

wall_image = load_image('wall.png')

rotated_wall_image = load_image('rotated_wall.png')


class Player:
    def __init__(self):
        self.health = 10
        self.points = 0

    def draw(self):
        font = pygame.font.Font(None, 30)

        text = font.render(f"Жизни: {str(self.health)}", True, (100, 255, 100))
        text_x = width - text.get_width() - 10
        text_y = 10

        screen.blit(text, (text_x, text_y))

        text2 = font.render(f"Очки:{str(self.points)}", True, (100, 255, 100))
        text_x2 = width - text2.get_width() - 10
        text_y2 = text2.get_height() + 10

        screen.blit(text2, (text_x2, text_y2))
#

# TODO нужно доделать класс ENEMY, понять, почему враг не рисуется
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(enemy_group, all_sprites)
        self.x = 0
        self.y = 0
        self.image = enemy_image

        self.rect = self.image.get_rect().move(self.x, self.y)

        self.level = 0
        self.health = 0
        self.speed = 2

    def update(self, *args):
        if self.x == 10 and self.y > 10:
            self.y -= self.speed / args[0]

            self.rect = self.rect.move(self.x, self.y)


        elif self.x == 10 and self.y <= 10:
            self.x += self.speed / args[0]

            self.rect = self.rect.move(self.x, self.y)


        elif self. x >= 590 and self.y <= 10:
            self.y += self.speed / args[0]

            self.rect = self.rect.move(self.x, self.y)


        else:
            self.die()

    def die(self):
        self.kill()


class Tower(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, left, top):
        super().__init__(tower_group, all_sprites)

        self.image = tower_image


        self.rect = self.image.get_rect().move(
            tower_width * pos_x + left, tower_height * pos_y + top)

        print(pos_x)


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
        schitatel = 0
        schetchik_kolichestva_dorozhek = 0
        schetchik_kolichestva_stenok = 77
        w = pygame.Color(202, 228, 255)
        cs = self.cell_size

        for y in range(self.height):
            for x in range(self.width):
                schitatel += 1

                schetchik_kolichestva_dorozhek = 0

                schetchik_kolichestva_stenok = 77

                pygame.draw.rect(screen, w, (x * cs + self.left, y * cs + self.top, cs + 1, cs + 1), 0)


                if schitatel % 2 == 0:


                    pygame.draw.rect(screen, pygame.Color(105, 105, 255),
                                     (x * cs + self.left + 1, y * cs + self.top + 1, cs - 1, cs - 1), 0)


                else:
                    pygame.draw.rect(screen, pygame.Color(155, 105, 205), (x * cs + self.left + 1, y * cs + self.top + 1, cs - 1, cs - 1), 0)
#№

                for z in range(7):
                    screen.blit(path_image, (0, schetchik_kolichestva_dorozhek))

                    screen.blit(path_image, (522, schetchik_kolichestva_dorozhek))

                    screen.blit(path_image, (schetchik_kolichestva_dorozhek, 0))

                    schetchik_kolichestva_dorozhek += 78
                for z in range(11):


                    screen.blit(wall_image, (schetchik_kolichestva_stenok, 77))

                    screen.blit(rotated_wall_image, (77, schetchik_kolichestva_stenok))

                    screen.blit(rotated_wall_image, (501, schetchik_kolichestva_stenok))

                    screen.blit(wall_image, (schetchik_kolichestva_stenok, 501))

                    schetchik_kolichestva_stenok += 37


                if not provershit:
                    pygame.draw.rect(screen, pygame.Color(105, 128, 155), (250, 501, 100, 50))


                if provershit:
                    pygame.draw.rect(screen, pygame.Color(128, 178, 128), (250, 501, 100, 50))


                fontObj = pygame.font.Font(None, 60)

                textSurfaceObj = fontObj.render(str(schetchik_ochkov_dlya_pokupki_bashen), True, (255, 0, 255))

                textRectObj = textSurfaceObj.get_rect()

                textRectObj.center = (300, 525)

                screen.blit(textSurfaceObj, textRectObj)


                if self.board[y][x] >= 1:

                    Tower(x, y, self.left, self.top)

        tower_group.draw(screen)


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
        if cell_coords != None:
            self.board[list(cell_coords)[1]][list(cell_coords)[0]] += 1
            print(self.board[list(cell_coords)[1]][list(cell_coords)[0]])


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


pygame.init()
pygame.display.set_caption('Игра')

size = width, height = 600, 800
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("black"))

x, y = 5, 5
board = Board(x, y)
board.set_view(100, 100, 80)

fps = 60
clock = pygame.time.Clock()
player = Player()
while True:
    screen.fill(pygame.Color("black"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            if provershit:
                schetchik_ochkov_dlya_pokupki_bashen += 10
                print('asd')

        if event.type == pygame.MOUSEMOTION:
            if 250 <= int(event.pos[0]) <= 350 and 500 <= int(event.pos[1]) <= 550:
                provershit = True
            else:
                provershit = False
    board.render(screen)
    enemy_group.draw(screen)
    player.draw()
    # enemy_group.update(event, fps)
    pygame.display.flip()
