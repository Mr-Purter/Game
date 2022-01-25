import pygame
import sys
import random
from pygame.locals import *

okno_shirina = 1000  # Ширина окна
okno_visota = 500    # Высота окна
svet_title = (225, 42, 31) # Цвет шрифта
svet_bg = (255, 255, 255)   # Цвет заднего фона
FPS = 60
mx_vrag_razmer = 50        # max размер врага
skor_wasd = 5              # скорость птицы (стрелочками)
mn_vrag_razmer = 20        # min размер врага
vrag_skor_mn = 1           # min скорость врага
vrag_skor_mx = 1           # max скорость врага
chastota_vrag = 12         # частота спавна врагов
mx_ochkov = 0



def key():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                return



def tekts_ris(text, font, surface, x, y):
    text = font.render(text, 1, svet_title)
    textrect = text.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text, textrect)


def stolk(igrok, vrag):
    for i in vrag:
        if igrok.colliderect(i['rect']):
            return True
    return False



                                             #создание окна
pygame.init()
okno_razm = pygame.display.set_mode((okno_shirina, okno_visota))
pygame.display.set_caption('Птица без крыла')
pygame.mouse.set_visible(False)

time = pygame.time.Clock()


shrift = pygame.font.SysFont('Arial', 48)    #настройка шрифта

                                             #настройка звука
pygame.mixer.music.load('laxity-crosswords-by-seraphic-music.mp3')
sn_gm_fn = pygame.mixer.Sound('zvuki-quotkonets-igryiquot-game-over-sounds-30249.wav')


igrok_pick = pygame.image.load('pngegg ).png')
vrag_pick = pygame.image.load('Орёл.png')  # настройка картинок
igrok_rect = igrok_pick.get_rect()

                                             #начальный экран
tekts_ris('Добро пожаловать в игру "Птица без крыла"', shrift, okno_razm, (okno_shirina / 3) - 220, (okno_visota / 3) - 150)
tekts_ris('Единственное правило:', shrift, okno_razm, (okno_shirina / 3) - 25, (okno_visota / 3) - 100)
tekts_ris('держитесь на расстоянии 5 см от орлов', shrift, okno_razm, (okno_shirina / 3) - 175, (okno_visota / 3) - 50)
tekts_ris('Нажмите "Enter" для начала игры', shrift, okno_razm, (okno_shirina / 3) - 120, (okno_visota / 3) + 100)
tekts_ris('Удачи!!', shrift, okno_razm, (okno_shirina / 3) + 100, (okno_visota / 3) + 175)
pygame.display.update()
key()




while True:
    # Настройки окна
    vrag = []
    ochki = 0
    igrok_rect.topleft = (okno_shirina / 2, okno_visota - 50)
    mv_l = mv_r = mv_u = mv_d = False
    chet_vrag_new = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:
        ochki += 1 # зачисление очков

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    mv_r = False
                    mv_l = True
                if event.key == K_RIGHT:
                    mv_l = False
                    mv_r = True
                if event.key == K_UP:
                    mv_d = False
                    mv_u = True
                if event.key == K_DOWN:
                    mv_u = False
                    mv_d = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    exit()

                if event.key == K_LEFT:
                    mv_l = False
                if event.key == K_RIGHT:
                    mv_r = False
                if event.key == K_UP:
                    mv_u = False
                if event.key == K_DOWN:
                    mv_d = False




                                        #движения героя мышкой
            if event.type == MOUSEMOTION:
                igrok_rect.move_ip(event.pos[0] - igrok_rect.centerx, event.pos[1] - igrok_rect.centery)

                                         #спавн орлов
        if key:
            chet_vrag_new += 1
        if chet_vrag_new == chastota_vrag:
            chet_vrag_new = 0
            vrag_sz = random.randint(mn_vrag_razmer, mx_vrag_razmer)
            vrag_new = {'rect': pygame.Rect(random.randint(0, okno_shirina - vrag_sz), 0 - vrag_sz, vrag_sz, vrag_sz),
                        'speed': random.randint(vrag_skor_mn, vrag_skor_mx),
                        'surface':pygame.transform.scale(vrag_pick, (vrag_sz, vrag_sz)),
                        }

            vrag.append(vrag_new)

        # движение стрелочками
        if mv_l and igrok_rect.left > 0:
            igrok_rect.move_ip(-1 * skor_wasd, 0)
        if mv_r and igrok_rect.right < okno_shirina:
            igrok_rect.move_ip(skor_wasd, 0)
        if mv_u and igrok_rect.top > 0:
            igrok_rect.move_ip(0, -1 * skor_wasd)
        if mv_d and igrok_rect.bottom < okno_visota:
            igrok_rect.move_ip(0, skor_wasd)


        pygame.mouse.set_pos(igrok_rect.centerx, igrok_rect.centery)

                                  #движение орлов
        for k in vrag[:]:
            if k['rect'].top > okno_visota:
                vrag.remove(k)

        for k in vrag:
            if key:
                k['rect'].move_ip(0, k['speed'])
            elif key:
                k['rect'].move_ip(0, -5)
            elif key:
                k['rect'].move_ip(0, 1)





        okno_razm.fill(svet_bg)                 #заливка заднего фона


                                           #Очки
        tekts_ris('Очки: %s' % (ochki), shrift, okno_razm, 400, 0)
        tekts_ris('Макс.очков: %s' % (mx_ochkov), shrift, okno_razm, 10, 0)


        okno_razm.blit(igrok_pick, igrok_rect)\

                                     #Орлы
        for k in vrag:
            okno_razm.blit(k['surface'], k['rect'])

        pygame.display.update()

                            # Столкновение орла и птички
        if stolk(igrok_rect, vrag):
            if ochki > mx_ochkov:
                mx_ochkov = ochki
            break

        time.tick(FPS)

                               #Настройка музыки
    pygame.mixer.music.stop()
    sn_gm_fn.play()
                               #Экран проигрыша
    tekts_ris('ВЫ ПРОИГРАЛИ!!!', shrift, okno_razm, (okno_shirina / 3), (okno_visota / 3))
    tekts_ris('Нажмите ENTER для перезапуска', shrift, okno_razm, (okno_shirina / 3.5) - 80, (okno_visota / 3) + 50)
    pygame.display.update()
    key()
    sn_gm_fn.stop()

def exit():
        pygame.quit()
        sys.exit()