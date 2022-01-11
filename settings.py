import pygame
import os
import sys
import csv
from subprocess import Popen, run, call

f = open('csv_data/sounds.txt', encoding='utf8').readlines()

a = ["bullet0.mp3", "bullet1.mp3", "bullet2.mp3"]
b = ["tower0.mp3", "tower1.mp3", "tower2.mp3"]
c = ["enemy0.mp3", "enemy1.mp3", "enemy2.mp3"]

ia = a.index(f[0].strip().split("/")[1])
ib = b.index(f[1].strip().split("/")[1])
ic = c.index(f[2].strip().split("/")[1])

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


pygame.init()
width = 417
height = 500
size = width, height
screen = pygame.display.set_mode(size)

running = True
scorost = 60
fps = 60
right = True

fon = load_image('fon_sett.png')
clock = pygame.time.Clock()

font = pygame.font.Font(None, 21)
text1 = font.render(f"Нажмите чтобы воспроизвести звук: {ia}", True, (100, 255, 100))
text2 = font.render(f"Нажмите чтобы воспроизвести звук: {ib}", True, (100, 255, 100))
text3 = font.render(f"Нажмите чтобы воспроизвести звук: {ic}", True, (100, 255, 100))


while running:
    screen.blit(fon, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 327 < int(event.pos[0]) < 405 and 50 < int(event.pos[1]) < 95:
                if ia < 2:
                    ia += 1
                else:
                    ia = 0
                print(ia)
            elif 327 < int(event.pos[0]) < 405 and 140 < int(event.pos[1]) < 180:
                if ib < 2:
                    ib += 1
                else:
                    ib = 0
                print(ib)
            elif 327 < int(event.pos[0]) < 405 and 232 < int(event.pos[1]) < 268:
                if ic < 2:
                    ic += 1
                else:
                    ic = 0
                print(ic)
            elif 222 < int(event.pos[0]) < 405 and 400 < int(event.pos[1]) < 480:
                open('csv_data/sounds.txt', 'w').close()
                f = open('csv_data/sounds.txt', 'w')
                for i in [a[ia], b[ib], c[ic]]:
                    print(i)
                    f.write("z_data/" + i + '\n')
                f.close()
                running = False
                pygame.display.quit()
                call(['python', 'main_menu.py'])
                terminate()
            elif 30 < int(event.pos[0]) < 315 and 50 < int(event.pos[1]) < 95:
                pygame.mixer.music.load(f"z_data/{a[ia]}")
            elif 30 < int(event.pos[0]) < 315 and 140 < int(event.pos[1]) < 180:
                pygame.mixer.music.load(f"z_data/{b[ib]}")
            elif 30 < int(event.pos[0]) < 315 and 232 < int(event.pos[1]) < 268:
                pygame.mixer.music.load(f"z_data/{c[ic]}")
                pygame.mixer.music.play()

    text1 = font.render(f"Нажмите чтобы воспроизвести звук: {ia}", True, (100, 255, 100))
    text2 = font.render(f"Нажмите чтобы воспроизвести звук: {ib}", True, (100, 255, 100))
    text3 = font.render(f"Нажмите чтобы воспроизвести звук: {ic}", True, (100, 255, 100))
    screen.blit(text1, (30 + 6, 50 + 6))
    screen.blit(text2, (30 + 6, 140 + 6))
    screen.blit(text3, (30 + 6, 232 + 6))

    clock.tick(fps)
    pygame.display.flip()
