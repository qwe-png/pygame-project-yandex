import pygame
import math
import sys
import os
from random import randint

schetchik_ochkov_dlya_pokupki_bashen = 0
randomazer = randint(0, 4)
provershit = 10
schitatel = 0
schetchik_kolichestva_dorozhek = 0
schetchik_kolichestva_stenok = 0
schetchik_kolichestva_serdec = 3
bul_pos = []
tow = 0
global c
c = 0
liv = False


def terminate():
    # выход
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["НАЖМИТЕ ЛКМ ЧТОБЫ НАЧАТЬ"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)






def end_screen():
    intro_text = ["НАЖМИТЕ ПКМ, ЧТОБЫ НАЧАТЬ ЗАНОВО"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)


def surface(image, colorkey=None):
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_image(name):
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
bullets = pygame.sprite.Group()

tower_width = tower_height = 80
tower_image = load_image('tower.png')
enemy_image = load_image("enemy.png")
path_image = load_image('path.png')
wall_image = load_image('wall.png')
phon_igri_image = load_image('phOn_igri.png')
rotated_wall_image = load_image('rotated_wall.png')
celoe_serdce_image = load_image('celoe_serdechko.png')
pustoe_serdce_image = load_image('pustoe_serdechko.png')
valuta_image = load_image('valuta.png')
bullet_image = load_image("bullet.png")


class Player:
    def __init__(self):
        self.health = 3
        self.points = 10

    def draw(self):
        font = pygame.font.Font(None, 30)

        text = font.render(f"Жизни: {str(self.health)}", True, (100, 255, 100))
        text_x = width - text.get_width() - 10
        text_y = 10
        screen.blit(text, (text_x, text_y))

        text2 = font.render(f"Очки:{str(self.points)}", True, (100, 255, 100))
        fontObj = pygame.font.Font(None, 50)
        textSurfaceObj = fontObj.render(str(self.points), True, (0, 255, 255))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (365, 613)
        screen.blit(textSurfaceObj, textRectObj)

        if self.health == 3:
            screen.blit(celoe_serdce_image, (84, 600))
            screen.blit(celoe_serdce_image, (107, 600))
            screen.blit(celoe_serdce_image, (130, 600))
        if self.health == 2:
            screen.blit(celoe_serdce_image, (84, 600))
            screen.blit(celoe_serdce_image, (107, 600))
            screen.blit(pustoe_serdce_image, (130, 600))
        if self.health == 1:
            screen.blit(celoe_serdce_image, (84, 600))
            screen.blit(pustoe_serdce_image, (107, 600))
            screen.blit(pustoe_serdce_image, (130, 600))
        if self.health == 0:
            screen.blit(pustoe_serdce_image, (84, 600))
            screen.blit(pustoe_serdce_image, (107, 600))
            screen.blit(pustoe_serdce_image, (130, 600))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        global schetchik_kolichestva_serdec, liv
        super().__init__(enemy_group, all_sprites)
        self.image = enemy_image
        self.image_copy = enemy_image
        self.x = 10
        self.y = 720
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(
            self.x, self.y)
        liv = True
        self.level = 0
        self.health = 0
        self.speed = 200

        self.c = 0

    def update(self, *args):
        self.x = self.rect.left
        self.y = self.rect.top
        if self.x == 10 and self.y > 10:
            self.rect = self.rect.move(0, -self.speed / args[0])
        elif (self.x >= 10) and (self.x <= 530) and (self.y <= 10):
            if self.c == 0:
                self.image = pygame.transform.rotate(self.image, 270)
                self.c = 1
            self.rect = self.rect.move(self.speed / args[0], 0)
        elif (self.x >= 530 and self.y >= 9) and self.y <= 800:
            if self.c == 1:
                self.image = pygame.transform.rotate(self.image_copy, 180)
                self.c = 2
            self.rect = self.rect.move(0, self.speed / args[0])
        else:
            self.end()

    def end(self):
        global liv
        self.kill()
        liv = False
        player.health -= 1

    def killed(self):
        global liv
        self.kill()
        liv = False
        player.points += 1


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(bullets)
        self.radius = radius
        self.image = bullet_image
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = -5
        self.vy = 0

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, enemy_group):
            pygame.sprite.spritecollide(self, enemy_group, bullets)
            self.dis()
            Enemy().killed()

    def dis(self):
        self.kill()



class Tower(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, left, top):
        super().__init__(tower_group, all_sprites)
        global tow
        tow += 1
        print(tow)
        self.image = tower_image
        self.rect = self.image.get_rect().move(
            tower_width * pos_x + left, tower_height * pos_y + top)
        Ball(10, tower_width * pos_x + left + 25, tower_height * pos_y + top + 25)
        bul_pos.append([tower_width * pos_x + left + 25, tower_height * pos_y + top + 25])
        print(bul_pos)


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
        w = pygame.Color(255, 255, 255)
        cs = self.cell_size
        screen.blit(phon_igri_image, (0, 580))
        screen.blit(valuta_image, (510, 595))
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
                    pygame.draw.rect(screen, pygame.Color(155, 105, 205),
                                     (x * cs + self.left + 1, y * cs + self.top + 1, cs - 1, cs - 1))

                if not provershit:
                    pygame.draw.rect(screen, pygame.Color(105, 105, 105), (250, 500, 100, 60))
                if provershit:
                    pygame.draw.rect(screen, pygame.Color(128, 128, 128), (250, 500, 100, 60))
                fontObj = pygame.font.Font(None, 60)
                textSurfaceObj = fontObj.render(str(schetchik_ochkov_dlya_pokupki_bashen), True, (255, 0, 0))
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (300, 525)
                screen.blit(textSurfaceObj, textRectObj)

                if self.board[y][x] == 1:
                    Tower(x, y, self.left, self.top)
                    self.board[y][x] += 1

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

size = width, height = 600, 700
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("black"))

x, y = 5, 5
board = Board(x, y)
board.set_view(100, 100, 80)

fps = 60
clock = pygame.time.Clock()

start_screen()
player = Player()

while True:
    screen.fill(pygame.Color("black"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            Enemy()
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

    # проверки
    c += 1
    if c % 50 == 0 and (liv is True):
        # здесь можно поменять скорострельность башенки
        # 100 => 5 секунд, значит 50 примерно равно 2.5, а 25 это 1.25 сек.
        for q in range(tow):
            for n in range(len(bul_pos)):
                Ball(10, bul_pos[n][0], bul_pos[n][1])

    if player.health <= 0:
        exec(open("game_over.py").read())

    # отрисовка
    tower_group.draw(screen)
    enemy_group.draw(screen)
    player.draw()
    bullets.draw(screen)

    # обновление
    bullets.update()
    enemy_group.update(fps)

    clock.tick(fps)
    pygame.display.flip()
