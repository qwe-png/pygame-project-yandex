import pygame
import os
import sys
from subprocess import Popen, run, call

pygame.init()
width = 900
height = 697
size = width, height
screen = pygame.display.set_mode(size)

def terminate():
    # выход
    pygame.quit()
    sys.exit()

def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

running = True
scorost = 60
fps = 60
right = True
provershit = open('csv_data/background_nomer.csv', encoding='utf8').read()
provershit = int(provershit)
clock = pygame.time.Clock()
proverka_monotonnosti = False
odnotonnost_text_image = load_image('odnotonie_tona_text.png')
mnogotonnost_text_image = load_image('mnogotonnie_tona_text.png')
kruzhok = load_image('smena_tonnosti.png')
phon_image = load_image('background.png')
fon1_image = load_image('big_fon1.png')
fon2_image = load_image('big_fon2.png')
fon3_image = load_image('big_fon3.png')
fon4_image = load_image('big_fon4.png')
fon5_image = load_image('big_fon5.png')
fon6_image = load_image('big_fon6.png')
fon7_image = load_image('big_fon7.png')
fon8_image = load_image('big_fon8.png')
fon9_image = load_image('big_fon9.png')
fon10_image = load_image('big_fon10.png')
black_fon = load_image('big_fon_black.png')
white_fon = load_image('big_fon_white.png')
pink_fon = load_image('big_fon_pink.png')
red_fon = load_image('big_fon_red.png')
accept_btn = load_image('accept_btn.png')
strelka = load_image('strelka.png')
nazad_v_menu = False
while running:
    screen.fill('white')
    screen.blit(phon_image, (0, 0))
    screen.blit(accept_btn, (145, 580))
    screen.blit(strelka, (800, 280))
    if not proverka_monotonnosti:
        screen.blit(odnotonnost_text_image, (500, 20))
    else:
        screen.blit(mnogotonnost_text_image, (500, 20))
    screen.blit(kruzhok, (470, 37))
    if not provershit:
        screen.blit(fon1_image, (10, 225))
    if provershit == 1:
        screen.blit(fon2_image, (10, 225))
    if provershit == 2:
        screen.blit(fon3_image, (10, 225))
    if provershit == 3:
        screen.blit(fon4_image, (10, 225))
    if provershit == 4:
        screen.blit(fon5_image, (10, 225))
    if provershit == 5:
        screen.blit(fon6_image, (10, 225))
    if provershit == 6:
        screen.blit(fon7_image, (10, 225))
    if provershit == 7:
        screen.blit(fon8_image, (10, 225))
    if provershit == 8:
        screen.blit(fon9_image, (10, 225))
    if provershit == 9:
        screen.blit(fon10_image, (10, 225))
    if provershit == 10:
        screen.blit(black_fon, (10, 225))
    if provershit == 11:
        screen.blit(white_fon, (10, 225))
    if provershit == 12:
        screen.blit(red_fon, (10, 225))
    if provershit == 13:
        screen.blit(pink_fon, (10, 225))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if 815 < int(event.pos[0]) < 879 and 286 < int(event.pos[1]) < 316:
                if provershit == 9:
                    provershit = 0
                elif provershit == 13:
                    provershit = 10
                else:
                    provershit = int(provershit) + 1 - 1 + 1
            if 469 < int(event.pos[0]) < 524 and 33 < int(event.pos[1]) < 82:
                if not proverka_monotonnosti:
                    provershit = 10
                    proverka_monotonnosti = True
                else:
                    provershit = open('csv_data/background_nomer.csv', encoding='utf8').read()
                    provershit = int(provershit)
                    proverka_monotonnosti = False
            if 144 < int(event.pos[0]) < 561 and 580 < int(event.pos[1]) < 654:
                open('csv_data/background_nomer.csv', 'w').write(str(provershit))
                running = False
                pygame.display.quit()
                call(['python', 'store.py'])
                terminate()


    clock.tick(fps)
    pygame.display.flip()
