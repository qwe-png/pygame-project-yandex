import pygame
import math
import sys
import os
from random import randint
import csv
import sounds
from time import sleep
from subprocess import Popen, run, call

pygame.font.init()
schetchik_ochkov_dlya_pokupki_bashen = 10
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
slozhnost = open('csv_data/slozhnost.csv', encoding='utf8').read()

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
pont = pygame.font.SysFont('Comic Sans MS', 30)
ubito_vragov1 = pont.render('Убито Врагов: 15', True, (255, 0, 0))
zarabotano_deneg1 = pont.render('Заработано денег: 210', True, (0, 255, 255))
ubito_vragov2 = pont.render('Убито Врагов: 33', True, (255, 0, 0))
zarabotano_deneg2 = pont.render('Заработано денег: 600', True, (0, 255, 255))





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

price = 10
all_sprites = pygame.sprite.Group()
tower_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
boss = pygame.sprite.Group()
bullets = pygame.sprite.Group()

tower_width = tower_height = 80
tower_image = load_image('tower.png')
tower_image2 = load_image('tower_2.png')
enemy_image = load_image("enemy.png")
enemy2_image = load_image('enemy2.png')
enemy3_image = load_image('enemy3.png')
enemy4_image = load_image('enemy4.png')
enemy5_image = load_image('enemy5.png')
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
black_image = load_image('fon.jpg')
fon_black = load_image('smenniy_fon_black.jpg')
fon_red = load_image('smenniy_fon_red.jpg')
fon_white = load_image('smenniy_fon_white.jpg')
fon_pink = load_image('smenniy_fon_pink.jpg')
mesto_spavna_image = load_image('mesto_spavna.png')
image_sprite_boss_napravo = [pygame.image.load("data/boss_napravo1.png"),
                             pygame.image.load("data/boss_napravo2.png"),
                             pygame.image.load("data/boss_napravo3.png"),
                             pygame.image.load("data/boss_napravo4.png")]
image_sprite_boss_nazad = [pygame.image.load("data/boss_nazad1.png"),
                           pygame.image.load("data/boss_nazad2.png"),
                           pygame.image.load("data/boss_nazad3.png"),
                           pygame.image.load("data/boss_nazad4.png")]
image_sprite_boss_vpered = [pygame.image.load("data/boss_tuda1.png"),
                            pygame.image.load("data/boss_tuda2.png"),
                            pygame.image.load("data/boss_tuda3.png"),
                            pygame.image.load("data/boss_tuda4.png")]
pobeda_image = load_image('pobeda.png')
stage_1_complete_image = load_image('stage_1_complete.png')
stage_2_complete_image = load_image('stage_2_complete.png')
continue_sprite = load_image('continue.png')
menu_viigrisha_image = load_image('menu_viigrisha.png')



class Player:
    def __init__(self):
        if slozhnost == '0':
            self.health = 3
        elif slozhnost == '1':
            self.health = 1
        self.points = 100

    def draw(self):
        font = pygame.font.Font(None, 30)

        text = font.render(f"Жизни: {str(self.health)}", True, (100, 255, 100))
        text_x = width - text.get_width() - 10
        text_y = 10

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


vsego_deneg = 100


class Enemy5(pygame.sprite.Sprite):
    def __init__(self):
        global schetchik_kolichestva_serdec, liv
        super().__init__(enemy_group, all_sprites)
        self.image = enemy5_image
        self.image_copy = enemy5_image
        self.x = 10
        self.y = 498
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(
            self.x, self.y)
        liv = True
        self.level = 0
        self.health = 8
        self.speed = 220

        self.c = 0

    def update(self, *args):
        global naprovlenie, liv
        self.x = self.rect.left
        self.y = self.rect.top
        if self.health <= 0:
            self.killed()
        if self.x == 10 and self.y > 10:
            self.rect = self.rect.move(0, -self.speed / args[0])
        elif (self.x >= 10) and (self.x <= 530) and (self.y <= 10):
            if self.c == 0:
                self.image = pygame.transform.rotate(self.image, 270)
                self.c = 1
            self.rect = self.rect.move(self.speed / args[0], 0)
        elif (self.x >= 530 and self.y >= 9) and self.y <= 700:
            if self.c == 1:
                self.image = pygame.transform.rotate(self.image_copy, 180)
                self.c = 2
            self.rect = self.rect.move(0, self.speed / args[0])
        else:
            self.end()

    def end(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.health -= 1
        player.points += 25
        vsego_deneg += 25

        sounds.enemy_end()
        sounds.play()

    def killed(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.points += 25
        vsego_deneg += 25

        # звук
        sounds.z_enemy()
        sounds.play()


class Enemy4(pygame.sprite.Sprite):
    def __init__(self):
        global schetchik_kolichestva_serdec, liv
        super().__init__(enemy_group, all_sprites)
        self.image = enemy4_image
        self.image_copy = enemy4_image
        self.x = 10
        self.y = 498
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(
            self.x, self.y)
        liv = True
        self.level = 0
        self.health = 16
        self.speed = 110

        self.c = 0

    def update(self, *args):
        global naprovlenie, liv
        self.x = self.rect.left
        self.y = self.rect.top
        if self.health <= 0:
            self.killed()
        if self.x == 10 and self.y > 10:
            self.rect = self.rect.move(0, -self.speed / args[0])
        elif (self.x >= 10) and (self.x <= 530) and (self.y <= 10):
            if self.c == 0:
                self.image = pygame.transform.rotate(self.image, 270)
                self.c = 1
            self.rect = self.rect.move(self.speed / args[0], 0)
        elif (self.x >= 530 and self.y >= 9) and self.y <= 700:
            if self.c == 1:
                self.image = pygame.transform.rotate(self.image_copy, 180)
                self.c = 2
            self.rect = self.rect.move(0, self.speed / args[0])
        else:
            self.end()

    def end(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.health -= 1
        player.points += 30
        vsego_deneg += 30

        sounds.enemy_end()
        sounds.play()

    def killed(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.points += 30
        vsego_deneg += 30

        # звук
        sounds.z_enemy()
        sounds.play()


class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        global schetchik_kolichestva_serdec, liv
        super().__init__(enemy_group, all_sprites)
        self.image = enemy3_image
        self.image_copy = enemy3_image
        self.x = 10
        self.y = 498
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(
            self.x, self.y)
        liv = True
        self.level = 0
        self.health = 5
        self.speed = 180

        self.c = 0

    def update(self, *args):
        global naprovlenie, liv
        self.x = self.rect.left
        self.y = self.rect.top
        if self.health <= 0:
            self.killed()
        if self.x == 10 and self.y > 10:
            self.rect = self.rect.move(0, -self.speed / args[0])
        elif (self.x >= 10) and (self.x <= 530) and (self.y <= 10):
            if self.c == 0:
                self.image = pygame.transform.rotate(self.image, 270)
                self.c = 1
            self.rect = self.rect.move(self.speed / args[0], 0)
        elif (self.x >= 530 and self.y >= 9) and self.y <= 700:
            if self.c == 1:
                self.image = pygame.transform.rotate(self.image_copy, 180)
                self.c = 2
            self.rect = self.rect.move(0, self.speed / args[0])
        else:
            self.end()

    def end(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.health -= 1
        player.points += 15
        vsego_deneg += 15

        sounds.enemy_end()
        sounds.play()

    def killed(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.points += 15
        vsego_deneg += 15

        # звук
        sounds.z_enemy()
        sounds.play()


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        global schetchik_kolichestva_serdec, liv
        super().__init__(enemy_group, all_sprites)
        self.image = enemy2_image
        self.image_copy = enemy2_image
        self.x = 10
        self.y = 498
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(
            self.x, self.y)
        liv = True
        self.level = 0
        self.health = 5
        self.speed = 200

        self.c = 0

    def update(self, *args):
        global naprovlenie, liv
        self.x = self.rect.left
        self.y = self.rect.top
        if self.health <= 0:
            self.killed()
        if self.x == 10 and self.y > 10:
            self.rect = self.rect.move(0, -self.speed / args[0])
        elif (self.x >= 10) and (self.x <= 530) and (self.y <= 10):
            if self.c == 0:
                self.image = pygame.transform.rotate(self.image, 270)
                self.c = 1
            self.rect = self.rect.move(self.speed / args[0], 0)
        elif (self.x >= 530 and self.y >= 9) and self.y <= 700:
            if self.c == 1:
                self.image = pygame.transform.rotate(self.image_copy, 180)
                self.c = 2
            self.rect = self.rect.move(0, self.speed / args[0])
        else:
            self.end()

    def end(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.health -= 1
        player.points += 10
        vsego_deneg += 10

        sounds.enemy_end()
        sounds.play()

    def killed(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.points += 10
        vsego_deneg += 10

        # звук
        sounds.z_enemy()
        sounds.play()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        global schetchik_kolichestva_serdec, liv
        super().__init__(enemy_group, all_sprites)
        self.image = enemy_image
        self.image_copy = enemy_image
        self.x = 10
        self.y = 498
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(
            self.x, self.y)
        liv = True
        self.level = 0
        self.health = 2
        self.speed = 140

        self.c = 0

    def update(self, *args):
        global naprovlenie, liv
        self.x = self.rect.left
        self.y = self.rect.top
        if self.health <= 0:
            self.killed()
        if self.x == 10 and self.y > 10:
            self.rect = self.rect.move(0, -self.speed / args[0])
        elif (self.x >= 10) and (self.x <= 530) and (self.y <= 10):
            if self.c == 0:
                self.image = pygame.transform.rotate(self.image, 270)
                self.c = 1
            self.rect = self.rect.move(self.speed / args[0], 0)
        elif (self.x >= 530 and self.y >= 9) and self.y <= 700:
            if self.c == 1:
                self.image = pygame.transform.rotate(self.image_copy, 180)
                self.c = 2
            self.rect = self.rect.move(0, self.speed / args[0])
        else:
            self.end()

    def end(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.health -= 1
        player.points += 5
        vsego_deneg += 5

        sounds.enemy_end()
        sounds.play()

    def killed(self):
        global liv, vsego_deneg
        liv = False
        self.kill()
        player.points += 5
        vsego_deneg += 5

        # звук
        sounds.z_enemy()
        sounds.play()

boss_health = 0
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        global schetchik_kolichestva_serdec, liv, provershit_naprav_bossa, boss_health
        super().__init__(boss, enemy_group, all_sprites)
        self.an = 0
        self.image = image_sprite_boss_vpered[0]
        self.image_copy = image_sprite_boss_vpered[0]
        self.x = 10
        self.y = 498
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(
            self.x, self.y)
        liv = True
        self.level = 0
        self.health = 40
        hp = pont.render(str(self.health), False, (0, 255, 255))
        screen.blit(hp, (0, 400))
        self.speed = 60
        self.cena = 0

        self.c = 0

    def update(self, *args):
        global naprovlenie, liv, boss_health
        self.x = self.rect.left
        self.y = self.rect.top
        if self.health <= 0:
            self.killed()
        if self.an < 10:
            self.cena = 0
        elif 10 < self.an < 20:
            self.cena = 1
        elif 20 < self.an < 30:
            self.cena = 2
        elif 30 < self.an < 40:
            self.cena = 3
        if self.an == 45:
            self.an = 0
            cena = 0
        if self.c == 0:
            self.image = image_sprite_boss_vpered[self.cena]
            self.image_copy = image_sprite_boss_vpered[self.cena]
        if self.c == 1:
            self.image = image_sprite_boss_napravo[self.cena]
            self.image_copy = image_sprite_boss_napravo[self.cena]
        if self.c == 2:
            self.image = image_sprite_boss_nazad[self.cena]
            self.image_copy = image_sprite_boss_nazad[self.cena]
        if self.x == 10 and self.y > 10:
            self.rect = self.rect.move(0, -self.speed / args[0])
        elif (self.x >= 10) and (self.x <= 530) and (self.y <= 10):
            if self.c == 0:
                self.image = pygame.transform.rotate(self.image, 270)
                self.c = 1
            self.rect = self.rect.move(self.speed / args[0], 0)
        elif (self.x >= 530 and self.y >= 9) and self.y <= 700:
            if self.c == 1:
                self.image = pygame.transform.rotate(self.image_copy, 180)
                self.c = 2
            self.rect = self.rect.move(0, self.speed / args[0])
        else:
            self.end()
        self.an += 1
        #if boss_move_x == 0 and boss_move_y > 0:
        # #    boss_move_x = 0
        # #    boss_move_y -= 0.4
        #    provershit_naprav_bossa = 0
        # #elif 522 > boss_move_x >= 0 and boss_move_y <= 0:
        # #    boss_move_x += 0.4
        #     boss_move_y = 0
        #     provershit_naprav_bossa = 1
        # elif 522 <= boss_move_x and 522 > boss_move_y >= 0:
        #     boss_move_x = 522
        #     boss_move_y += 0.4
        #     provershit_naprav_bossa = 2
        boss_health = str(self.health)

    def end(self):
        global liv, vsego_deneg, boss_health
        liv = False
        self.kill()
        player.health -= 3
        player.points += 5
        vsego_deneg += 5

        sounds.enemy_end()
        sounds.play()
        boss_health = str(self.health)

    def killed(self):
        global liv, vsego_deneg, boss_health
        liv = False
        self.kill()
        player.points += 5
        vsego_deneg += 5

        # звук
        sounds.z_enemy()
        sounds.play()
        boss_health = str(self.health)



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
            for s in pygame.sprite.spritecollide(self, enemy_group, dokill=False):
                s.health -= 1

            self.kill()
        if self.rect.left == 0:
            self.kill()
        if self.rect.top == 0:
            self.kill()
        # if not screen.contains(self.rect):
            # self.kill()

proverka_na_prisutstvie_bashni = list(zip())

class Tower(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, left, top):
        global proverka_na_prisutstvie_bashni
        super().__init__(tower_group, all_sprites)
        global tow, naprovlenie
        self.povor1 = True
        self.povor2 = True
        tow += 1
        self.image = tower_image
        self.rect = self.image.get_rect().move(
            tower_width * pos_x + left, tower_height * pos_y + top)
        # Ball(10, tower_width * pos_x + left + 25, tower_height * pos_y + top + 25, naprovlenie)
        bul_pos.append([tower_width * pos_x + left + 25, tower_height * pos_y + top + 25])
        sounds.z_tower()
        sounds.play()

    def povorot1(self, deg):
        if self.povor1 and self.povor2:
            self.image = pygame.transform.rotate(self.image, deg)
            self.povor1 = False

    def povorot2(self, deg):
        if self.povor2:
            self.image = pygame.transform.rotate(tower_image, deg)
            self.povor2 = False

    def sbros(self):
        self.image = tower_image
        self.povor1 = True
        self.povor2 = True

class Tower_up(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, left, top):
        global proverka_na_prisutstvie_bashni
        super().__init__(tower_group, all_sprites)
        global tow, naprovlenie
        self.povor1 = True
        self.povor2 = True
        tow += 1
        self.image = tower_image2
        self.rect = self.image.get_rect().move(
            tower_width * pos_x + left, tower_height * pos_y + top)
        # Ball(10, tower_width * pos_x + left + 25, tower_height * pos_y + top + 25, naprovlenie)
        bul_pos.append([tower_width * pos_x + left + 25, tower_height * pos_y + top + 25])
        sounds.z_tower()
        sounds.play()

    def povorot1(self, deg):
        if self.povor1 and self.povor2:
            self.image = pygame.transform.rotate(self.image, deg)
            self.povor1 = False

    def povorot2(self, deg):
        if self.povor2:
            self.image = pygame.transform.rotate(tower_image2, deg)
            self.povor2 = False

    def sbros(self):
        self.image = tower_image2
        self.povor1 = True
        self.povor2 = True

stoimost = 0
provershit_naprav_bossa = 0
prozrachnost = 0
prozrachnost2 = 0
xan = 0
class Board:
    # создание поля
    def __init__(self, width, height):
        self.schetchik_ochkov_dlya_pokupki_bashen = 10
        self.price = 10
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.chckr = {}
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
        #if slozhnost == '1':
            # if provershit_naprav_bossa == 0:
                 #screen.blit(image_sprite_boss_vpered[cena], (boss_move_x, boss_move_y))
            # elif provershit_naprav_bossa == 1:
            #     screen.blit(image_sprite_boss_napravo[cena], (boss_move_x, boss_move_y))
            # elif provershit_naprav_bossa == 2:
            #     screen.blit(image_sprite_boss_nazad[cena], (boss_move_x, boss_move_y))

        shrift = pygame.font.Font(None, 60)
        nanesenniy_shrift = shrift.render(str(self.schetchik_ochkov_dlya_pokupki_bashen), True, (255, 0, 0))
        endsrift = nanesenniy_shrift.get_rect()
        endsrift.center = (300, 525)
        screen.blit(nanesenniy_shrift, endsrift)

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


                if player.points >= self.price:
                    pygame.draw.rect(screen, pygame.Color(210, 210, 0), (250, 500, 100, 60))
                else:
                    pygame.draw.rect(screen, pygame.Color(100, 100, 100), (250, 500, 100, 60))

                if self.board[y][x] == 1:
                    print(1)
                    self.chckr[f"{y}{x}"] = Tower(x, y, self.left, self.top)
                    self.board[y][x] += 1

                if self.board[y][x] == 3:
                    print(2)
                    self.chckr[f"{y}{x}"].kill()
                    self.chckr[f"{y}{x}"] = Tower_up(x, y, self.left, self.top)
                    self.board[y][x] += 1
        shrift = pygame.font.Font(None, 60)
        nanesenniy_shrift = shrift.render(str(self.schetchik_ochkov_dlya_pokupki_bashen), True, (255, 0, 0))
        endsrift = nanesenniy_shrift.get_rect()
        endsrift.center = (300, 525)
        screen.blit(nanesenniy_shrift, endsrift)
        if slozhnost == '1':
            pygame.draw.rect(screen, pygame.Color(33, 50, 63), (0, 650, 100, 60))
            boss_health_nadpis = pont.render(str(boss_health), True, (0, 255, 255))
            screen.blit(boss_health_nadpis, (0, 650))
            screen.blit(celoe_serdce_image, (38, 670))

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
        if cell_coords != None and player.points >= self.price and self.board[list(cell_coords)[1]][list(cell_coords)[0]] < 3:
            # print(proverka_na_prisutstvie_bashni)
            self.board[list(cell_coords)[1]][list(cell_coords)[0]] += 1
            self.schetchik_ochkov_dlya_pokupki_bashen += 10
            player.points -= self.price
            self.price += 10


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

player = Player()
velocity = 12
boss_move_x = 0
boss_move_y = 498
cena = 0
schetchik_vragov_pervoy_volni = 0
schetchik_vragov_vtoroy_volni = 0
provershit_konca_pervoy_volni = False
provershit_konca_vtoroy_volni = False
provershit_nachala_vtoroy_volni = False
bool_2wawe = True
bol_chst = True
pobeda_provershit = False
prizrachnost = 0
while True:
    for en in enemy_group:
        if en.c == 1 and naprovlenie == 0:
            naprovlenie = 1
        if en.c == 2:
            naprovlenie = 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            # print(event.pos)
            print(event.pos)
            if provershit_konca_pervoy_volni and 436 < int(event.pos[0]) <= 600 and 0 <= int(event.pos[1]) < 51:
                provershit_konca_pervoy_volni = False
                provershit_nachala_vtoroy_volni = True
            if provershit_konca_vtoroy_volni and 210 < int(event.pos[0]) <= 246 and 403 <= int(event.pos[1]) < 437:
                pygame.display.quit()
                call(['python', 'main_menu.py'])
                terminate()
            if provershit_konca_vtoroy_volni and 271 < int(event.pos[0]) <= 324 and 397 <= int(event.pos[1]) < 443:
                pygame.display.quit()
                open('csv_data/slozhnost.csv', 'w').write('1')
                call(['python', 'main.py'])
                terminate()
            if provershit_konca_vtoroy_volni and 348 < int(event.pos[0]) <= 388 and 397 <= int(event.pos[1]) < 443:
                pygame.display.quit()
                call(['python', 'main.py'])
                terminate()
            if pobeda_provershit and 126 < int(event.pos[0]) <= 236 and 378 <= int(event.pos[1]) < 430:
                pygame.display.quit()
                call(['python', 'main_menu.py'])
                terminate()
            if pobeda_provershit and 254 < int(event.pos[0]) <= 356 and 372 <= int(event.pos[1]) < 429:
                pygame.display.quit()
                call(['python', 'main.py'])
                terminate()
            if pobeda_provershit and 441 < int(event.pos[0]) <= 473 and 197 <= int(event.pos[1]) < 226:
                pygame.display.quit()
                call(['python', 'map.py'])
                terminate()

        if event.type == pygame.MOUSEMOTION:
            if 250 <= int(event.pos[0]) <= 350 and 500 <= int(event.pos[1]) <= 550:
                provershit = True
            else:
                provershit = False
        screen.fill(pygame.Color("black"))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                call(['python', 'map.py'])
                terminate()
    potracheno_deneg = pont.render(f'Потрачено денег: {vsego_deneg - player.points}', True, (0, 255, 255))
    board.render(screen)
    if slozhnost == '0':
        if not schetchik_vragov_pervoy_volni > 425:
            schetchik_vragov_pervoy_volni += 1

        if schetchik_vragov_pervoy_volni % 45 == 0 and schetchik_vragov_pervoy_volni:
            Enemy()
        if schetchik_vragov_pervoy_volni % 75 == 0:
            Enemy2()
        if schetchik_vragov_pervoy_volni % 250 == 0:
            Enemy3()
        if vsego_deneg == 210 and not provershit_nachala_vtoroy_volni:
            provershit_konca_pervoy_volni = True
        if vsego_deneg == 600:
            provershit_konca_vtoroy_volni = True
        if vsego_deneg > 210: provershit_konca_pervoy_volni = False
        if provershit_konca_pervoy_volni:
            naprovlenie = 0

            if not prozrachnost > 255:
                prozrachnost += 1
                stage_1_complete_image.set_alpha(prozrachnost)
                continue_sprite.set_alpha(prozrachnost)
                black_image.set_alpha(prozrachnost)
                ubito_vragov1.set_alpha(prozrachnost)
                zarabotano_deneg1.set_alpha(prozrachnost)
                potracheno_deneg.set_alpha(prozrachnost)
        if provershit_konca_vtoroy_volni:
            naprovlenie = 0
            if not prozrachnost2 > 255:
                prozrachnost2 += 1
                stage_2_complete_image.set_alpha(prozrachnost2)
                menu_viigrisha_image.set_alpha(prozrachnost2)
                black_image.set_alpha(prozrachnost2)
                potracheno_deneg.set_alpha(prozrachnost2)
                ubito_vragov2.set_alpha(prozrachnost2)
                zarabotano_deneg2.set_alpha(prozrachnost2)

    if pobeda_provershit:
        if not prizrachnost > 255:
            prizrachnost += 1
            pobeda_image.set_alpha(prizrachnost)
    xan += 1
    if stoimost == 0:
        if slozhnost == '1':
            stoimost += 1
            if stoimost == 1:
                Boss()
    if xan % 50 == 0 and not pobeda_provershit and slozhnost == '1':
        player.points += 15
        vsego_deneg += 15
    if int(boss_health) - 0 <= 0 and xan > 5 and slozhnost == '1':
        pobeda_provershit = True
    else:
        pobeda_provershit = False




    c += 1
    # здесь можно поменять скорострельность башенки
    # 100 => 5 секунд, значит 50 примерно равно 2.5, а 25 это 1.25 сек.
    # for n in range(len(bul_pos)):
    #     Ball(10, bul_pos[n][0], bul_pos[n][1], naprovlenie)
    #     sounds.z_bullet()
    #     sounds.play()
    for y in range(5):
        for x in range(5):
            if board.board[y][x] == 2:
                if c % 50 == 0 and bool(enemy_group):
                    Ball(10, x * board.cell_size + board.left, y * board.cell_size + board.top, naprovlenie)
                    sounds.z_bullet()
                    sounds.play()
            if board.board[y][x] == 4:
                if c % 25 == 0 and bool(enemy_group):
                    Ball(10, x * board.cell_size + board.left, y * board.cell_size + board.top, naprovlenie)
                    sounds.z_bullet()
                    sounds.play()
            if naprovlenie == 1:
                if f"{y}{x}" in board.chckr.keys():
                    board.chckr[f"{y}{x}"].povorot1(270)
            if naprovlenie == 2:
                if f"{y}{x}" in board.chckr.keys():
                    board.chckr[f"{y}{x}"].povorot2(180)

    if player.health <= 0:
        pygame.display.quit()
        call(['python', 'game_over.py'])
        terminate()


    # отрисовка
    tower_group.draw(screen)
    enemy_group.draw(screen)
    player.draw()
    bullets.draw(screen)
    boss.draw(screen)


    if provershit_nachala_vtoroy_volni:
        # naprovlenie = 0
        if bol_chst:
            for i in tower_group:
                i.sbros()
            bol_chst = False
        if bool_2wawe:
            naprovlenie = 0
            bool_2wawe = False
        if schetchik_vragov_vtoroy_volni < 900:
            schetchik_vragov_vtoroy_volni += 1
            if schetchik_vragov_vtoroy_volni % 50 == 0 and schetchik_vragov_vtoroy_volni <= 451:
                Enemy3()
            if schetchik_vragov_vtoroy_volni % 110 == 0 and schetchik_vragov_vtoroy_volni > 230:
                Enemy4()
            if schetchik_vragov_vtoroy_volni % 200 == 0 and schetchik_vragov_vtoroy_volni > 399:
                Enemy5()
    screen.blit(mesto_spavna_image, (-20, 515))

    if provershit_konca_pervoy_volni:
        screen.blit(black_image, (0, -400))
        screen.blit(stage_1_complete_image, (0, 150))
        screen.blit(ubito_vragov1, (0, 0))
        screen.blit(zarabotano_deneg1, (0, 30))
        screen.blit(potracheno_deneg, (0, 60))
        screen.blit(continue_sprite, (420, -20))
    if provershit_konca_vtoroy_volni:
        screen.blit(black_image, (0, -400))
        screen.blit(ubito_vragov2, (0, 0))
        screen.blit(zarabotano_deneg2, (0, 30))
        screen.blit(potracheno_deneg, (0, 60))
        screen.blit(stage_2_complete_image, (0, 150))
        screen.blit(menu_viigrisha_image, (165, 379))
    if pobeda_provershit is True:
        pobeda_image.set_alpha(prizrachnost)
        screen.blit(pobeda_image, (109, 180))
    # обновление
    bullets.update()
    enemy_group.update(fps)

    clock.tick(fps)
    pygame.display.flip()
