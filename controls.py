import random
import time

import pygame
import sys

import bullet
from bullet import *
import enemy

pygame.init()
lvlmusic = ['music/lvl1.mp3', 'music/lvl2.mp3']
shoot_sound = pygame.mixer.Sound('music/Shoot.wav')
nextlvl = pygame.mixer.music.load('music/Nextlvl.mp3')
dash = pygame.mixer.Sound('music/Dash.wav')
select = pygame.mixer.Sound('music/Select.wav')
start = pygame.mixer.Sound('music/Start.wav')
take = pygame.mixer.Sound('music/Lootbox.wav')
broke = pygame.mixer.Sound('music/Broke.wav')
'''Обработка событий по файлу orc.py'''
def events(screen, orc, stats, bg_screen, sc, menu, pbg, enemys, ebg, plg, live, MB, SHB, RB, TPB, BB):
    '''Перебираем все события пользователя'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
            screen = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F12:
                if stats.fullscreen:
                    screen = pygame.display.set_mode((1280, 720))
                    stats.fullscreen = False
                    time.sleep(3)
                else:
                    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
                    stats.fullscreen = True
                    time.sleep(3)
        if stats.menu_menu:
            '''Кнопка старт'''
            if menu.menu_start:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start.play()
                        stats.menu_menu = False
                        screen.fill(bg_screen)
                        live.lives_group(plg, screen, stats)
                        sc.new_level(stats)
                        sc.show_score()
                        live.live_draw(plg, stats)
                        sc.weapon_image_draw()
                        pygame.display.flip()
                        '''конечный экран'''
                        time.sleep(2)
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load(random.choice(lvlmusic))
                        pygame.mixer.music.play(-1)
                        stats.run_game = True

                        enemy.create_army(screen, enemys, menu)
                    if event.key == pygame.K_DOWN:
                        select.play()
                        menu.menu_start = False
                        menu.bg_menu_draw()
                        menu.menu_difficulty = True
                    if event.key == pygame.K_UP:
                        select.play()
                        menu.menu_start = False
                        menu.bg_menu_draw()
                        menu.menu_exit = True
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                '''Кнопка сложности'''
            elif menu.menu_difficulty:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        shoot_sound.play()
                        stats.menu_menu = False
                        menu.bg_menu_draw()
                        pygame.display.flip()
                        stats.difficulty_menu = True
                    if event.key == pygame.K_DOWN:
                        select.play()
                        menu.menu_difficulty = False
                        menu.bg_menu_draw()
                        menu.menu_exit = True
                    if event.key == pygame.K_UP:
                        select.play()
                        menu.menu_difficulty = False
                        menu.bg_menu_draw()
                        menu.menu_start = True
                '''Кнопка выход'''
            elif menu.menu_exit:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        sys.exit()
                    if event.key == pygame.K_DOWN:
                        select.play()
                        menu.menu_exit = False
                        menu.bg_menu_draw()
                        menu.menu_start = True
                    if event.key == pygame.K_UP:
                        select.play()
                        menu.menu_exit = False
                        menu.bg_menu_draw()
                        menu.menu_difficulty = True
        elif stats.difficulty_menu:
            '''Кнопка бойз'''
            if menu.dif_easy:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        shoot_sound.play()
                        menu.dif_easy = True
                        stats.difficulty_menu = False
                        menu.bg_menu_draw()
                        pygame.display.flip()
                        stats.menu_menu = True
                    if event.key == pygame.K_DOWN:
                        select.play()
                        menu.dif_easy = False
                        menu.bg_menu_draw()
                        menu.dif_norm = True
                    if event.key == pygame.K_UP:
                        select.play()
                        menu.dif_easy = False
                        menu.bg_menu_draw()
                        menu.dif_hard = True
                        '''Ноба'''
            elif menu.dif_norm:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        shoot_sound.play()
                        menu.dif_norm = True
                        stats.difficulty_menu = False
                        menu.bg_menu_draw()
                        pygame.display.flip()
                        stats.menu_menu = True
                    if event.key == pygame.K_DOWN:
                        select.play()
                        menu.dif_norm = False
                        menu.bg_menu_draw()
                        menu.dif_hard = True
                    if event.key == pygame.K_UP:
                        select.play()
                        menu.dif_norm = False
                        menu.bg_menu_draw()
                        menu.dif_easy = True
                        '''Варбосс'''
            elif menu.dif_hard:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        shoot_sound.play()
                        menu.dif_hard = True
                        stats.difficulty_menu = False
                        menu.bg_menu_draw()
                        pygame.display.flip()
                        stats.menu_menu = True
                    if event.key == pygame.K_DOWN:
                        select.play()
                        menu.dif_hard = False
                        menu.bg_menu_draw()
                        menu.dif_easy = True
                    if event.key == pygame.K_UP:
                        select.play()
                        menu.dif_hard = False
                        menu.bg_menu_draw()
                        menu.dif_norm = True
        elif stats.run_game:
            '''Событие - выход'''
                #'''''''''Клавиша нажата'''
            if event.type == pygame.KEYDOWN:
                '''клавиша ВПРАВО'''
                if event.key == pygame.K_RIGHT:
                    orc.mright = True
                '''ЛЕВО'''
                if event.key == pygame.K_LEFT:
                    orc.mleft = True
                '''ПРОБЕЛ'''
                if event.key == pygame.K_SPACE:
                    if stats.pistol:
                        shoot_sound.play()
                        pb = Pistol_Bullet(screen, orc)
                        pbg.add(pb)
                    if stats.two_pistols:
                        TPB.TPB_fire_time = True
                    if stats.machingun:
                        MB.MB_fire_time = True
                    if stats.shotgun:
                        SHB.SHB_fire_time = True
                    if stats.rifle:
                        RB.RB_fire_time = True
                    if stats.bazooka:
                        BB.BB_fire_time = True
                if event.key == pygame.K_ESCAPE:
                    stats.pause = True
                    pygame.mixer.music.load('music/Pause.mp3')
                    pygame.mixer.music.play()
                    stats.run_game = False
                if event.key == pygame.K_1:
                    stats.pistol = True
                    stats.two_pistols = False
                    stats.machingun = False
                    stats.shotgun = False
                    stats.rifle = False
                    stats.bazooka = False
                if event.key == pygame.K_2:
                    stats.pistol = False
                    stats.two_pistols = True
                    stats.machingun = False
                    stats.shotgun = False
                    stats.rifle = False
                    stats.bazooka = False
                if event.key == pygame.K_3:
                    stats.machingun = True
                    stats.pistol = False
                    stats.two_pistols = False
                    stats.shotgun = False
                    stats.rifle = False
                    stats.bazooka = False
                if event.key == pygame.K_4:
                    stats.shotgun = True
                    stats.pistol = False
                    stats.two_pistols = False
                    stats.machingun = False
                    stats.rifle = False
                    stats.bazooka = False
                if event.key == pygame.K_5:
                    stats.two_pistols = False
                    stats.shotgun = False
                    stats.pistol = False
                    stats.machingun = False
                    stats.rifle = True
                    stats.bazooka = False
                if event.key == pygame.K_6:
                    stats.pistol = False
                    stats.two_pistols = False
                    stats.machingun = False
                    stats.shotgun = False
                    stats.rifle = False
                    stats.bazooka = True

                '''Клавиша Отжата'''
            elif event.type == pygame.KEYUP:
                '''ПРАВО'''
                if event.key == pygame.K_RIGHT:
                    orc.mright = False
                '''ЛЕВО'''
                if event.key == pygame.K_LEFT:
                    orc.mleft = False
            '''Пауза'''
        elif stats.pause:
            if menu.pause_btg:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        stats.pause_btg = False
                        pygame.display.flip()
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load(random.choice(lvlmusic))
                        pygame.mixer.music.play(0)
                        stats.run_game = True
                    if event.key == pygame.K_DOWN:
                        menu.pause_btg = False
                        menu.bg_menu_draw()
                        menu.pause_btm = True
                    if event.key == pygame.K_UP:
                        menu.pause_btg = False
                        menu.bg_menu_draw()
                        menu.pause_btm = True
            elif menu.pause_btm:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        stats.pause_btg = False
                        enemys.empty()
                        ebg.empty()
                        pbg.empty()
                        stats.reset_stats()
                        pygame.display.flip()
                        stats.menu_menu = True
                    if event.key == pygame.K_DOWN:
                        menu.pause_btg = True
                        menu.bg_menu_draw()
                        menu.pause_btm = False
                    if event.key == pygame.K_UP:
                        menu.pause_btg = True
                        menu.bg_menu_draw()
                        menu.pause_btm = False
            '''Геймовер'''
        elif stats.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    stats.game_over = False
                    menu.bg_menu_draw()
                    enemys.empty()
                    ebg.empty()
                    pbg.empty()
                    stats.reset_stats()
                    sc.image_score()
                    live.lives_group(plg, screen, stats)
                    stats.menu_menu = True
                    pygame.display.flip()
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

'''Обновление экрана'''
def update_screen(screen, orc, enemys, pbg, ebg, sc, menu, live, plg, stats, boxes, expl, expl_anim, Enemy):
    '''фоновый цвет'''
    enemy_c = Enemy(screen,enemys)
    menu.bg_lvl_draw()
    '''Отрисовываем пули'''
    for new_player_bullet in pbg.sprites():
        new_player_bullet.draw_player_bullet()
    for new_enemy_bullet in ebg.sprites():
        new_enemy_bullet.draw_enemy_bullet()
    for new_box in boxes.sprites():
        new_box.draw_lootbox()
    '''отрисовка жизней врага'''
    for HB in enemys.sprites():
        HB.healthbar(screen)
    '''ОРК'''
    orc.orc_draw()
    '''Отрисовываем пришельца с помощью функции def draw() из класса enemys'''
    enemys.draw(screen)
    '''Отрисовка взрывов'''
    for new_expl_anim in expl_anim.sprites():
        new_expl_anim.draw_explosion_anim()
    """Жизни"""
    live.live_draw(plg, stats)
    '''выводим счет'''
    sc.show_score()
    sc.weapon_image(stats, screen)
    sc.weapon_image_draw()
    '''конечный экран'''
    pygame.display.flip()

'''Обновление группы enemys'''
def update_enemys(stats, orc, enemys, pbg, ebg, screen, enemy, menu, plg, live, expl, boxes):
    enemys.update(enemys, stats, screen, ebg, orc, menu)
    '''Коллизия между пушкой и группой enemys'''
    if pygame.sprite.spritecollideany(orc, enemys):
        print(pygame.sprite.spritecollideany(orc, enemys))
        orc_kill(stats, orc, enemys, pbg, ebg, screen, enemy, menu, plg, live, expl, boxes)
    screen_rect = screen.get_rect()
    '''Пишем условия для пришельца (Enemy) в группе enemys'''
    for Enemy in enemys.sprites():
        if Enemy.rect.bottom >= screen_rect.bottom - 70:
            orc_kill(stats, orc, enemys, pbg, ebg, screen, enemy, menu, plg, live, expl, boxes)
            break

'''Столкновение орка и армии'''
def orc_kill(stats, orc, enemys, pbg, ebg, screen, enemy, menu, plg, live, expl, boxes):
    dash.play()
    '''Проверяем колличество жизней'''
    if stats.live > 1:
        '''отнятие жизни'''
        stats.live -= 1
        '''перезагружаем армию'''
        enemys.empty()
        enemy.create_army(screen, enemys, menu)
        plg.empty()
        live.lives_group(plg, screen, stats)
        live.live_update(stats)
        '''перезагружаем пули'''
        ebg.empty()
        pbg.empty()
        expl.empty()
        boxes.empty()
        '''Создаем пушку заново'''
        orc.orc_draw()
        '''вызываем задержку'''
        time.sleep(1)
        print(stats.live)
        print(len(plg))
    else:
        stats.live -= 1
        stats.run_game = False
        stats.game_over = True
        pbg.empty()
        ebg.empty()

'''Создание новой армии при уничтожении'''
def new_army(enemys, pbg, screen, enemy, bg_screen, sc, stats, ebg, menu, MB, plg, live, boxes, expl):
    if len(enemys) == 0:
        pygame.mixer.music.pause()
        #nextlvl.play()
        screen.fill(bg_screen)
        sc.new_level(stats)
        '''выводим счет'''
        sc.show_score()
        live.live_draw(plg, stats)
        '''конечный экран'''
        pygame.display.flip()
        time.sleep(3)
        '''очищаем группу с пулями'''
        pbg.empty()
        MB.fire_time = False
        ebg.empty()
        boxes.empty()
        expl.empty()
        '''Создаем армию'''
        enemy.create_army(screen, enemys, menu)
        pygame.mixer.music.play()


'''Проверка рекорда'''
def check_high_score(stats, sc):
    '''Если нынешник очки больше рекорда'''
    if stats.score > stats.high_score:
        '''Заменяем рекорд ныншними очками'''
        stats.high_score = stats.score
        '''Обновляем рекорд'''
        sc.image_high_score()
        '''перезаписываем файл с сохранением'''
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))

def game_over_screen(sc, menu):
    menu.bg_menu_draw()
    menu.game_over_show()
    '''выводим счет'''
    sc.show_score()
    '''конечный экран'''
    pygame.display.flip()

def menu_screen(menu):
    menu.bg_menu_draw()
    menu.draw_menu()
    pygame.display.flip()
def difficulty_menu_screen(menu):
    menu.draw_difficulty()
    pygame.display.flip()
def pause_screen(menu):
    menu.bg_menu_draw()
    menu.draw_pause()
    pygame.display.flip()
def difficulty(menu, orc, enemy, enemys, plg):
    if menu.dif_easy:
        for enemy in enemys:
            enemy.diff_easy = True
            enemy.diff_norm = False
            enemy.diff_hard = False
        enemy.a = 5
    if menu.dif_norm:
        orc.image = pygame.image.load('image/noba.png')
        for live in plg:
            live.image = pygame.image.load('image/noba.png')
        for enemy in enemys:
            enemy.diff_easy = False
            enemy.diff_norm = True
            enemy.diff_hard = False
        enemy.a = 5
    if menu.dif_hard:
        orc.image = pygame.image.load('image/warboss.png')
        for live in plg:
            live.image = pygame.image.load('image/warboss.png')
        for enemy in enemys:
            enemy.diff_easy = False
            enemy.diff_norm = False
            enemy.diff_hard = True
            #print(enemy.diff_hard)
        enemy.a = 4

def guns(stats):
    if stats.pistol:
        stats.machingun = False
        stats.shotgun = False
        stats.rifle = False
    if stats.machingun:
        stats.pistol = False
        stats.shotgun = False
        stats.rifle = False
    if stats.shotgun:
        stats.pistol = False
        stats.machingun = False
        stats.rifle = False
    if stats.rifle:
        stats.pistol = False
        stats.machingun = False
        stats.shotgun = False

def lootbox_use(stats, orc, boxes, pbg, enemys, live, plg, screen, ebg, menu, expl):

    for mbox in boxes.copy():
        if stats.rifle:
            pygame.sprite.groupcollide(pbg, boxes, False, False)
        elif mbox.a == 'image/death_box.png':
            pygame.sprite.groupcollide(pbg, boxes, True, False)
        else:
            if pygame.sprite.groupcollide(pbg, boxes, False, True):
                broke.play()

        if mbox.rect.bottom >= 650:
            mbox.remove(boxes)
        if pygame.sprite.spritecollideany(orc, boxes):
            take.play()
            take.set_volume(2)
            if mbox.a == 'image/live_box.png':
                stats.live += 1
                live.lives_group(plg, screen, stats)
                live.live_update(stats)
                pygame.display.update()
                print(stats.live)
            elif mbox.a == 'image/pistol_box.png':
                if stats.pistol:
                    stats.machingun = False
                    stats.shotgun = False
                    stats.pistol = False
                    stats.two_pistols = True
                    stats.rifle = False
                    stats.bazooka = False
                else:
                    stats.machingun = False
                    stats.shotgun = False
                    stats.pistol = True
                    stats.two_pistols = False
                    stats.rifle = False
                    stats.bazooka = False
            elif mbox.a == 'image/machingun_box.png':
                stats.machingun = True
                stats.shotgun = False
                stats.pistol = False
                stats.two_pistols = False
                stats.rifle = False
                stats.bazooka = False
            elif mbox.a == 'image/shotgun_box.png':
                stats.machingun = False
                stats.shotgun = True
                stats.pistol = False
                stats.two_pistols = False
                stats.rifle = False
                stats.bazooka = False
            elif mbox.a == 'image/rifle_box.png':
                stats.pistol = False
                stats.machingun = False
                stats.shotgun = False
                stats.two_pistols = False
                stats.rifle = True
                stats.bazooka = False
            elif mbox.a == 'image/bazooka_box.png':
                stats.machingun = False
                stats.shotgun = False
                stats.pistol = False
                stats.two_pistols = False
                stats.rifle = False
                stats.bazooka = True
            elif mbox.a == 'image/random_box.png':
                L = Lootbox(screen, enemys)
                mbox.a = L.a
                return
            elif mbox.a == 'image/death_box.png':
                orc_kill(stats, orc, enemys, pbg, ebg, screen, enemy, menu, plg, live, expl, boxes)
            mbox.kill()


#def music(stats, menu):
    #playlist = []
    #playlist.append('music/Menu.mp3')
    #playlist.append('music/Contra_Contravirt_OC_ReMix.ogv')
    #playlist.append('music/Pause.mp3')
    #if stats.menu_menu:
    #    pygame.mixer.music.stop()
    #pygame.mixer.music.load(playlist.pop())
    #    music = 'music/Menu.mp3'
    #    print(stats.menu_menu)
    #elif stats.run_game:
    #    pygame.mixer.music.rewind()
        #pygame.mixer.music.load(playlist.pop())
    #    music = 'music/Contra_Contravirt_OC_ReMix.ogv'
    #    print(stats.run_game)
    #elif stats.pause:
    #    pygame.mixer.music.rewind()
        #pygame.mixer.music.load(playlist.pop())
     #   music = 'music/Pause.mp3'
     #   print(stats.pause)
    #pygame.mixer.music.load(music)
    #pygame.mixer.music.play(-1)