import pygame, controls, bullet, enemy

'''импортируем класс Gun из Gun.py'''
from orc import Orc
from stats import Stats
from scores import Scores
from menu import Menu
from enemy import Enemy
from pygame.sprite import Group
from lives import Live
from bullet import *

clock = pygame.time.Clock()
def run():
    clock.tick(10)
    '''Инициализируем игру'''
    pygame.init()
    """FPS"""

    '''Графическая область'''
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    '''Заголовок графической области'''
    pygame.display.set_caption('ORCZ!!')
    pygame.display.set_icon(pygame.image.load("image/select.png"))
    '''Цвет задника (R, G, B)'''
    bg_screen = (0,0,0)
    '''Создаем объект пушки на экране(screen)'''
    orc = Orc(screen)
    '''Создаем контейнер пришельцев'''
    enemys = Group()
    '''Создание контейнера Пули'''
    pbg = Group()
    ebg = Group()
    plg = Group()
    boxes = Group()
    expl = Group()
    expl_anim = Group()
    '''Вызов Функции создания армии'''
    '''Создаем экземпляр stats класса Stats'''
    stats = Stats()
    '''Создаем объект Счета на экране'''
    sc = Scores(screen, stats)
    menu = Menu(screen)
    enemy_c = Enemy(screen, enemys)
    live = Live(screen, stats)
    TPB = Two_Pistol_Bullet(screen, orc, pbg)
    MB = Machinegun_Bullet(screen, orc)
    SHB = Shotgun_Bullet(screen, orc)
    RB = Rifle_Bullet(screen, orc)
    BB = Bazooka_Bullet(screen, orc)
    ex = Explosion(screen)
    '''выводим счет'''
    pygame.mixer.music.load('music/Menu.mp3')
    pygame.mixer.music.play()
    '''Бесконечный цикл обработки всех событий в игре'''
    while True:
        """FPS"""

        '''Вызываем функцию event из controls.py'''
        #controls.music(stats, menu)
        #controls.guns(stats)
        controls.events(screen, orc, stats, bg_screen, sc, menu, pbg, enemys, ebg, plg, live, MB, SHB, RB, TPB, BB)
        '''Проверяем колличество жизней'''
        if stats.menu_menu:
            controls.menu_screen(menu)
        elif stats.difficulty_menu:
            controls.difficulty_menu_screen(menu)
        elif stats.run_game:
            controls.difficulty(menu, orc, enemy, enemys, plg)
            '''Вызываем функцию update_gun из orc.py'''
            orc.update_orc()
            '''Вызываем функцию update из bullet.py'''
            pbg.update(screen, orc, pbg)
            ebg.update(screen, Enemy, ebg, enemys)
            boxes.update(screen, Enemy)
            expl.update(screen, expl)
            expl_anim.update(screen, expl_anim)
            '''Вызываем функцию update_screen из controls.py'''
            controls.update_screen(screen, orc, enemys, pbg, ebg, sc, menu, live, plg, stats, boxes, expl, expl_anim, Enemy)
            '''Стрельба врагов'''
            enemy.Enemy_fire(enemys, ebg, screen, orc, menu)
            enemy_c.draw_HP(screen)
            controls.lootbox_use(stats, orc, boxes, pbg, enemys, live, plg, screen, ebg, menu, expl)

            TPB.fire(screen, orc, pbg)
            MB.fire(screen, orc, pbg)
            SHB.fire(screen, orc, pbg)
            RB.fire(screen, orc, pbg)
            BB.fire(screen, orc, pbg)
            '''Вызываем функцию удаления пули(del_bullet) из bullet для группы bullets'''
            bullet.player_bullet_update(enemys, orc, pbg, ebg, stats, sc, controls, screen, enemy, menu, Enemy, plg, live, boxes, expl, expl_anim)
            bullet.explosion(expl, screen, stats, sc, ebg, enemys, Enemy)
            '''Вызывает update из aliens.py'''
            controls.update_enemys(stats, orc, enemys, pbg, ebg, screen, enemy, menu, plg, live, expl, boxes)
            controls.new_army(enemys, pbg, screen, enemy, bg_screen, sc, stats, ebg, menu, MB, plg, live, boxes, expl)
        elif stats.pause:
            controls.pause_screen(menu)
        else:
            controls.game_over_screen(sc, menu)

run()
