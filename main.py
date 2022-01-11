import pygame
import math
import sys
import os
from random import randint
import csv
import sounds
from subprocess import Popen, run, call


schetchik_ochkov_dlya_pokupki_bashen = 0
randomazer = randint(0, 4)
provershit = 10
schitatel = 0
schetchik_kolichestva_dorozhek = 0
schetchik_kolichestva_stenok = 0
schetchik_kolichestva_serdec = 3
bul_pos = []
tow = 0
naprovlenie = 0
global c
c = 0
liv = False
pole_zipper = list(zip())
nomer_polya = 0
nomer_pole_csv = open('csv_data/pole_nomer.csv', encoding='utf8').read()
nomer_path_csv = open('csv_data/path_nomer.csv', encoding='utf8').read()
nomer_wall_csv = open('csv_data/wall_nomer.csv', encoding='utf8').read()
nomer_fon_csv = open('csv_data/background_nomer.csv', encoding='utf8').read()
nomer_wall = int(nomer_wall_csv)
nomer_path = int(nomer_path_csv)
nomer_fon = int(nomer_fon_csv)
samo_pole_csv = open('csv_data/pole.csv', encoding='utf8')
pole_colour = csv.reader(samo_pole_csv, delimiter=';', quotechar='"')
for i in pole_colour:
    pole_zipper.append(i)
nomer_polya = int(nomer_pole_csv)
perviy_pervogo = int(pole_zipper[int(nomer_pole_csv)][0].replace('(', '').replace(')', '').split(',')[0])
vtoroy_pervogo = int(pole_zipper[int(nomer_pole_csv)][0].replace('(', '').replace(')', '').split(',')[1])
tretiy_pervogo = int(pole_zipper[int(nomer_pole_csv)][0].replace('(', '').replace(')', '').split(',')[2])
perviy_vtorogo = int(pole_zipper[int(nomer_pole_csv)][1].replace('(', '').replace(')', '').split(',')[0])
vtoroy_vtorogo = int(pole_zipper[int(nomer_pole_csv)][1].replace('(', '').replace(')', '').split(',')[1])
tretiy_vtorogo = int(pole_zipper[int(nomer_pole_csv)][1].replace('(', '').replace(')', '').split(',')[2])
samo_pole_csv.close()

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
path2_image = load_image('path2.jpg')
path_image = load_image('path.png')
path3_image = load_image('path3.jpg')
path4_image = load_image('path4.png')
wall_image = load_image('wall.png')
wall2_image = load_image('wall2.png')
wall3_image = load_image('wall3.png')
wall4_image = load_image('wall4.png')
phon_igri_image = load_image('phOn_igri.png')
rotated_wall_image = load_image('rotated_wall.png')
rotated_wall2_image = load_image('rotated_wall2.png')
rotated_wall3_image = load_image('rotated_wall3.png')
rotated_wall4_image = load_image('rotated_wall4.png')
celoe_serdce_image = load_image('celoe_serdechko.png')
pustoe_serdce_image = load_image('pustoe_serdechko.png')
valuta_image = load_image('valuta.png')
bullet_image = load_image("bullet.png")
fon_1 = load_image('smenniy_fon1.jpg')
fon_2 = load_image('smenniy_fon2.jpg')
fon_3 = load_image('smenniy_fon3.jpg')
fon_4 = load_image('smenniy_fon4.jpg')
fon_5 = load_image('smenniy_fon5.jpg')
fon_6 = load_image('smenniy_fon6.jpg')
fon_7 = load_image('smenniy_fon7.jpg')
fon_8 = load_image('smenniy_fon8.jpg')
fon_9 = load_image('smenniy_fon9.jpg')
fon_10 = load_image('smenniy_fon10.jpg')
fon_black = load_image('smenniy_fon_black.jpg')
fon_red = load_image('smenniy_fon_red.jpg')
fon_white = load_image('smenniy_fon_white.jpg')
fon_pink = load_image('smenniy_fon_pink.jpg')


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
        self.speed = 150

        self.c = 0

    def update(self, *args):
        global naprovlenie, liv
        self.x = self.rect.left
        self.y = self.rect.top
        if self.x == 10 and self.y > 10:
            self.rect = self.rect.move(0, -self.speed / args[0])
            naprovlenie = 0
        elif (self.x >= 10) and (self.x <= 530) and (self.y <= 10):
            if self.c == 0:
                self.image = pygame.transform.rotate(self.image, 270)
                self.c = 1
                naprovlenie = 1
            self.rect = self.rect.move(self.speed / args[0], 0)
        elif (self.x >= 530 and self.y >= 9) and self.y <= 800:
            if self.c == 1:
                self.image = pygame.transform.rotate(self.image_copy, 180)
                self.c = 2
                naprovlenie = 2
            self.rect = self.rect.move(0, self.speed / args[0])
        else:
            self.end()

    def end(self):
        global liv
        liv = False
        self.kill()
        player.health -= 1

    def killed(self):
        global liv
        liv = False
        self.kill()
        player.points += 1

        # звук
        sounds.z_enemy()
        sounds.play()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, n):
        super().__init__(bullets)
        self.radius = radius
        self.image = bullet_image
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.napr = n

    def update(self):
        if self.napr == 0:
            self.rect.move_ip(-5, 0)
        if self.napr == 1:
            self.rect.move_ip(0, -5)
        if self.napr == 2:
            self.rect.move_ip(5, 0)
        if pygame.sprite.spritecollideany(self, enemy_group):
            pygame.sprite.spritecollide(self, enemy_group, bullets)
            self.kill()
        # if not screen.contains(self.rect):
            # self.kill()



class Tower(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, left, top):
        super().__init__(tower_group, all_sprites)
        global tow, naprovlenie
        tow += 1
        self.image = tower_image
        self.rect = self.image.get_rect().move(
            tower_width * pos_x + left, tower_height * pos_y + top)
        Ball(10, tower_width * pos_x + left + 25, tower_height * pos_y + top + 25, naprovlenie)
        bul_pos.append([tower_width * pos_x + left + 25, tower_height * pos_y + top + 25])


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
        if nomer_fon == 0:
            screen.blit(fon_1, (0, 500))
        if nomer_fon == 1:
            screen.blit(fon_2, (0, 500))
        if nomer_fon == 2:
            screen.blit(fon_3, (0, 500))
        if nomer_fon == 3:
            screen.blit(fon_4, (0, 500))
        if nomer_fon == 4:
            screen.blit(fon_5, (0, 500))
        if nomer_fon == 5:
            screen.blit(fon_6, (0, 500))
        if nomer_fon == 6:
            screen.blit(fon_7, (0, 500))
        if nomer_fon == 7:
            screen.blit(fon_8, (0, 500))
        if nomer_fon == 8:
            screen.blit(fon_9, (0, 500))
        if nomer_fon == 9:
            screen.blit(fon_10, (0, 500))
        if nomer_fon == 10:
            screen.blit(fon_black, (0, 500))
        if nomer_fon == 11:
            screen.blit(fon_white, (0, 500))
        if nomer_fon == 12:
            screen.blit(fon_red, (0, 500))
        if nomer_fon == 13:
            screen.blit(fon_pink, (0, 500))
        screen.blit(phon_igri_image, (0, 580))
        screen.blit(valuta_image, (510, 595))
        if nomer_path == 0:
            for z in range(7):
                screen.blit(path_image, (0, schetchik_kolichestva_dorozhek))
                screen.blit(path_image, (522, schetchik_kolichestva_dorozhek))
                screen.blit(path_image, (schetchik_kolichestva_dorozhek, 0))
                schetchik_kolichestva_dorozhek += 78
        if nomer_path == 1:
            for z in range(7):
                screen.blit(path2_image, (0, schetchik_kolichestva_dorozhek))
                screen.blit(path2_image, (522, schetchik_kolichestva_dorozhek))
                screen.blit(path2_image, (schetchik_kolichestva_dorozhek, 0))
                schetchik_kolichestva_dorozhek += 78
        if nomer_path == 2:
            for z in range(7):
                screen.blit(path3_image, (0, schetchik_kolichestva_dorozhek))
                screen.blit(path3_image, (522, schetchik_kolichestva_dorozhek))
                screen.blit(path3_image, (schetchik_kolichestva_dorozhek, 0))
                schetchik_kolichestva_dorozhek += 78
        if nomer_path == 3:
            for z in range(7):
                screen.blit(path4_image, (0, schetchik_kolichestva_dorozhek))
                screen.blit(path4_image, (522, schetchik_kolichestva_dorozhek))
                screen.blit(path4_image, (schetchik_kolichestva_dorozhek, 0))
                schetchik_kolichestva_dorozhek += 78
        if nomer_wall == 0:
            for z in range(11):
                screen.blit(wall_image, (schetchik_kolichestva_stenok, 77))
                screen.blit(rotated_wall_image, (77, schetchik_kolichestva_stenok))
                screen.blit(rotated_wall_image, (501, schetchik_kolichestva_stenok))
                screen.blit(wall_image, (schetchik_kolichestva_stenok, 501))
                schetchik_kolichestva_stenok += 37
        if nomer_wall == 1:
            for z in range(11):
                screen.blit(wall2_image, (schetchik_kolichestva_stenok, 77))
                screen.blit(rotated_wall2_image, (77, schetchik_kolichestva_stenok))
                screen.blit(rotated_wall2_image, (501, schetchik_kolichestva_stenok))
                screen.blit(wall2_image, (schetchik_kolichestva_stenok, 501))
                schetchik_kolichestva_stenok += 37
        if nomer_wall == 2:
            for z in range(11):
                screen.blit(wall3_image, (schetchik_kolichestva_stenok, 77))
                screen.blit(rotated_wall3_image, (77, schetchik_kolichestva_stenok))
                screen.blit(rotated_wall3_image, (501, schetchik_kolichestva_stenok))
                screen.blit(wall3_image, (schetchik_kolichestva_stenok, 501))
                schetchik_kolichestva_stenok += 37
        if nomer_wall == 3:
            for z in range(11):
                screen.blit(wall4_image, (schetchik_kolichestva_stenok, 77))
                screen.blit(rotated_wall4_image, (77, schetchik_kolichestva_stenok))
                screen.blit(rotated_wall4_image, (501, schetchik_kolichestva_stenok))
                screen.blit(wall4_image, (schetchik_kolichestva_stenok, 501))
                schetchik_kolichestva_stenok += 37

        if not provershit:
            pygame.draw.rect(screen, pygame.Color(105, 105, 105), (250, 500, 100, 60))
        if provershit:
            pygame.draw.rect(screen, pygame.Color(128, 128, 128), (250, 500, 100, 60))

        fontObj = pygame.font.Font(None, 60)
        textSurfaceObj = fontObj.render(str(schetchik_ochkov_dlya_pokupki_bashen), True, (255, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (300, 525)
        screen.blit(textSurfaceObj, textRectObj)

        for y in range(self.height):
            for x in range(self.width):
                schitatel += 1

                pygame.draw.rect(screen, w, (x * cs + self.left, y * cs + self.top, cs + 1, cs + 1), 0)

                if schitatel % 2 == 0:
                    pygame.draw.rect(screen, pygame.Color(perviy_pervogo, vtoroy_pervogo, tretiy_pervogo),
                                     (x * cs + self.left + 1, y * cs + self.top + 1, cs - 1, cs - 1), 0)
                else:
                    pygame.draw.rect(screen, pygame.Color(perviy_vtorogo, vtoroy_vtorogo, tretiy_vtorogo),
                                     (x * cs + self.left + 1, y * cs + self.top + 1, cs - 1, cs - 1))

                if self.board[y][x] == 1:
                    Tower(x, y, self.left, self.top)
                    self.board[y][x] += 1

        fontObj = pygame.font.Font(None, 60)
        textSurfaceObj = fontObj.render(str(schetchik_ochkov_dlya_pokupki_bashen), True, (255, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (300, 525)
        screen.blit(textSurfaceObj, textRectObj)

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
pygame.display.set_caption('Tower defence')

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
    if c % 50 == 0 and bool(enemy_group):
        # здесь можно поменять скорострельность башенки
        # 100 => 5 секунд, значит 50 примерно равно 2.5, а 25 это 1.25 сек.
        for q in range(tow):
            for n in range(len(bul_pos)):
                Ball(10, bul_pos[n][0], bul_pos[n][1], naprovlenie)

    if player.health <= 0:
        pygame.display.quit()
        call(['python', 'game_over.py'])



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