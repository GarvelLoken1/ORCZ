import pygame
import random
from bullet import *

images = [pygame.image.load('image/human.png'), pygame.image.load('image/human2.png'),
          pygame.image.load('image/human3.png'), pygame.image.load('image/human4.png'),
          pygame.image.load('image/human5.png'), pygame.image.load('image/human6.png')]
'''Создаем класс одного пришельца'''
class Enemy(pygame.sprite.Sprite):
    '''Метод инициализации (графика(screen)'''
    def __init__(self, screen, enemys):
        '''инициализируем и задаем начальную позицию'''
        super(Enemy, self).__init__()
        '''инициализация пришлельца'''
        self.screen = screen
        self.death = False
        '''Загрузка изображение'''
        #if self.death:
            #self.image = pygame.image.load('image/scull.png')
        #else:
        self.image = random.choice(images)
        '''Получаем графический объект пришельца в качестве прямоугольника(rect - rectangle)'''
        self.rect = self.image.get_rect()
        '''Получаем графический объекст экрана в качестве прямоугольника'''
        self.screen_rect = self.screen.get_rect()
        '''Координаты пришельца по Иксу отслеживаем по ширине (width)'''
        self.rect.x = self.rect.width
        '''Координаты пришельца по Иксу отслеживаем по высоте (height)'''
        self.rect.y = self.rect.height
        '''Преобразование целых чисел в вещественные (float(десятичные))'''
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #self.death_time = 0
        self.damage_time = 0
        self.fire_time = 0
        self.fire = False
        self.diff_easy = False
        self.diff_norm = False
        self.diff_hard = False
        self.damage = False
        self.live = 2
        self.cur_live = 2
        self.healthbar(screen)
    '''полоска жизней'''
    def healthbar(self, screen):
        self.a = 50
        self.b = self.a * (self.live / self.cur_live)
        self.HP = pygame.Rect(self.rect.left, self.rect.bottom + 2, self.b, 4)
        self.HP_back = pygame.Rect(self.rect.left - 2, self.rect.bottom, self.a + 4, 8)
        pygame.draw.rect(screen, (0, 0, 0), self.HP_back, 2)
        pygame.draw.rect(screen, (76, 175, 79), self.HP)

    '''вывод пришельца на экран'''
    def draw_HP(self, screen):
        '''Отрисовывание(blit) пушки(self.image) по заданым параметрам (self.rect)'''
        #self.screen.blit(self.image, self.rect)

    '''перемещение пришельцев'''

    def update(self, enemys, stats, screen, ebg, orc, menu):
        if self.diff_easy:
            self.y += (stats.level / 200)
            self.rect.y = self.y
        elif self.diff_norm:
            self.y += (stats.level / 175)
            self.rect.y = self.y
        elif self.diff_hard:
            self.y += (stats.level / 150)
            self.rect.y = self.y
        if self.screen_rect.centery - 500 < self.rect.y < self.screen_rect.centery - 400 \
                or self.screen_rect.centery - 300 < self.rect.y < self.screen_rect.centery - 200 \
                or self.screen_rect.centery - 100 < self.rect.y < self.screen_rect.centery - 0 \
                or self.screen_rect.centery - (- 100) > self.rect.y > self.screen_rect.centery - (- 200):
            self.x -= 0.1
            self.rect.x = self.x
            if self.rect.right == self.screen_rect.left:
                self.rect.left = self.screen_rect.right
                self.x = self.rect.x
        if self.screen_rect.centery - 400 < self.rect.y < self.screen_rect.centery - 300 \
                or self.screen_rect.centery - 200 < self.rect.y < self.screen_rect.centery - 100 \
                or self.screen_rect.centery - 0 < self.rect.y < self.screen_rect.centery - (- 100) \
                or self.screen_rect.centery - (- 200) < self.rect.y < self.screen_rect.centery - (- 300):
            self.x += 0.1
            self.rect.x = self.x
            if self.rect.left == self.screen_rect.right:
                self.rect.right = self.screen_rect.left
                self.x = self.rect.x
        #if self.damage:
        #    if self.damage_time >= 0:
        #        self.damage_time += 1
        #        if self.damage_time == 1:
        #            self.image = pygame.transform.rotozoom(self.image, 45, 1)
        #        elif self.damage_time == 100:
        #            print(self.damage_time)
        #            self.damage_time = 0
        #            self.damage = False
        #            self.image = pygame.transform.rotozoom(self.image, -45, 1)







'''Создаем армию пришельцев'''
def create_army(screen, enemys, menu):
    '''Создаем одного пришельца на основе класса Enemy'''
    enemy = Enemy(screen, enemys)
    if menu.dif_easy:
        a = 7
    elif menu.dif_norm:
        a = 6
    elif menu.dif_hard:
        a = 5
    '''Создаем ширину на основе класса Enemy'''
    enemy_width = enemy.rect.width
    '''Создаем высоту на основе класса Enemy'''
    enemy_height = enemy.rect.height - 20
    '''Расчет колличества пришельцев в одном ряду по Иксу'''
    numbers_enemy_x = int(((1280 - 2 * enemy_width) / enemy_width) / 2)
    '''Расчет колличества пришельцев в одном столбце по Игрику'''
    numbers_enemy_y = int(((720 - 2 * enemy_height) / enemy_height) / 2)
    '''создаем цикл, который создает ряды пришельцев'''
    for enemys_number_by_pillar in range(numbers_enemy_y - a):
        '''Создаем цикл, который создает столбы пришельцев'''
        for enemys_number_by_row in range(numbers_enemy_x + 2):
            '''Создаем одного пришельца на основе класса Enemy'''
            enemy = Enemy(screen, enemys)
            '''Распределяем их по ряду исходя из колличества'''
            enemy.x = 2 * enemy_width * enemys_number_by_row
            '''Распределяем по столбцам исходя из колличества'''
            enemy.y = 0.5 * enemy_height + 2 * enemy_height * enemys_number_by_pillar
            ''''''
            enemy.rect.y = enemy.y
            enemy.rect.x = enemy.x
            '''Добавляем в группу enemys'''
            enemys.add(enemy)

'''Атака врагов'''
def Enemy_fire(enemys, ebg, screen, orc, menu):
    for Enemy in enemys:
        if Enemy.rect.centerx == orc.rect.centerx:
            if menu.dif_easy:
                i = [True, False, False, False, False]
            if menu.dif_norm:
                i = [True, False, False, False]
            if menu.dif_hard:
                i = [True, False, False]
            Enemy.fire = random.choice(i)
        if Enemy.fire:
            Enemy.fire_time += 1
            if Enemy.fire_time == random.randint(50, 100):
                new_enemy_bullet = Enemy_Bullet(screen, Enemy)
                ebg.add(new_enemy_bullet)
                Enemy.fire_time = 0
                Enemy.fire = False