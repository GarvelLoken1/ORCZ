import pygame
from pygame.sprite import Sprite
class Orc(pygame.sprite.Sprite):
    '''метод инициализации (screen - графику)'''
    def __init__(self, screen):
        super(Orc, self).__init__()
        '''инициализация пушки'''
        self.screen = screen
        '''Загрузка изображение'''
        self.image = pygame.image.load('image/orc.png')
        '''Получаем графический объекст пушки в качестве прямоугольника(rect - rectangle)'''
        self.rect = self.image.get_rect()
        '''Получаем графический объекст экрана в качестве прямоугольника'''
        self.screen_rect = self.screen.get_rect()
        '''Координаты пушки по Иксу(centerx(посередине)) накладываем на координаты экрана'''
        self.rect.centerx = self.screen_rect.centerx
        '''Координаты по Игрику(bottom (низ)) накладываем на координаты экрана'''
        self.rect.bottom = self.screen_rect.bottom - 72
        '''Преобразование целых чисел в вещественные (float(десятичные))'''
        self.centre = float(self.rect.centerx)
        '''Передвижение вправо (По умолчанию = False)'''
        self.mright = False
        '''Передвижение влево (По умолчанию = False)'''
        self.mleft = False
    '''Выводим на экран'''
    def orc_draw(self):
        '''Отрисовывание(blit) пушки(self.image) по заданым параметрам (self.rect)'''
        self.screen.blit(self.image, self.rect)

    '''Обновление позиции пушки'''
    def update_orc(self):
        '''Если передвижение вправо (self.mrite) TRUE(по умолчани) и правй пиксель пушки (self.rect.right) не привышает правый пиксель экрана(self.screen_rect.right)'''
        if self.mright and self.rect.right < self.screen_rect.right:
            self.centre += 1
        '''Для Лева'''
        if self.mleft and self.rect.left > self.screen_rect.left:
            self.centre -= 1
        '''Приправниваем координаты пушки по Иксу к Преобразованию целых чисел в вещественные (float(десятичные)'''
        self.rect.centerx = self.centre
