import pygame.font
from lives import Live
from pygame.sprite import Group
'''Вывод очков'''
class Scores():
    '''инициализируем'''
    def __init__(self, screen, stats):
        '''инициализируем экран'''
        super(Scores, self).__init__()
        self.screen = screen
        '''Получаем графический объект экрана в качестве прямоугольника'''
        self.screen_rect = screen.get_rect()
        '''инициализируем stats'''
        self.stats = stats
        '''Настраиваем цвет шрифта'''
        self.text_color1 = (68, 22, 6)
        self.text_color2 = (27, 94, 31)
        self.text_color = (67, 160, 71)
        '''Настраиваем шрифт'''
        self.font = pygame.font.Font('OutlinePixel7.ttf', 36)
        self.font2 = pygame.font.Font('OutlinePixel7.ttf', 36)
        '''Вызов метода отрисовки шрифта'''
        self.image_score()
        '''Вывод рекорда'''
        self.image_high_score()
        self.weapon_image(stats, screen)
    '''преобразовывает текст счета в графическое изображение'''
    def image_score(self):
        '''рендерим(render) шрифт(font) как строку(str) (Очки, ???, цвет шрифта, цвет фона)'''
        self.score_txt = self.font.render(str(self.stats.score), True, self.text_color)
        '''Получаем графический объект счетчика очков'''
        self.score_txt_rect = self.score_txt.get_rect()
        '''Отрисовываем его на экране'''

        self.score_img = pygame.image.load('image/scull.png')
        self.score_img_rect = self.score_img.get_rect()

        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.bottom = self.screen_rect.bottom - 10
        self.score_txt_rect.right = self.score_img_rect.left - 10
        self.score_txt_rect.centery = self.score_img_rect.centery
    '''Преобразование теста рекорда в граф. изображение'''
    def image_high_score(self):
        '''рендерим(render) шрифт(font) как строку(str) (Очки, ???, цвет шрифта, цвет фона)'''
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color)
        self.high_score_txt = self.font.render('HS:', True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_txt_rect = self.high_score_txt.get_rect()
        self.high_score_txt_rect.left = self.screen_rect.left + 20
        self.high_score_txt_rect.bottom = self.screen_rect.bottom - 15
        self.high_score_rect.left = self.high_score_txt_rect.right + 10
        self.high_score_rect.centery = self.high_score_txt_rect.centery
    '''Game_Over'''


    '''Вывод счета на экран'''
    def show_score(self):
        self.screen.blit(self.score_txt, self.score_txt_rect)
        self.screen.blit(self.score_img, self.score_img_rect)
        '''вывод рекорда'''
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.high_score_txt, self.high_score_txt_rect)

    def new_level(self, stats):
        pygame.display.flip()
        stats.level += 1
        '''рендерим(render) шрифт(font) как строку(str) (Очки, ???, цвет шрифта, цвет фона)'''
        self.newlevel = self.font.render('ДРАКА', True, self.text_color, (0, 0, 0))
        self.numlevel = self.font.render(str(stats.level), True, self.text_color, (0, 0, 0))
        '''Получаем графический объект счетчика рекорда'''
        self.new_level_rect = self.newlevel.get_rect()
        self.num_level_rect = self.numlevel.get_rect()
        '''Отрисовываем на экране'''
        self.new_level_rect.center = self.screen_rect.center
        self.num_level_rect.centerx = self.screen_rect.centerx
        self.num_level_rect.centery = self.screen_rect.centery - 60
        self.screen.blit(self.newlevel, self.new_level_rect)
        self.screen.blit(self.numlevel, self.num_level_rect)

    def weapon_image(self, stats, screen):
        self.screen = screen
        if stats.pistol:
            self.weapon_img = pygame.image.load('image/pistol.png')
        elif stats.two_pistols:
            self.weapon_img = pygame.image.load('image/two_pistols.png')
        elif stats.machingun:
            self.weapon_img = pygame.image.load('image/machingun.png')
        elif stats.shotgun:
            self.weapon_img = pygame.image.load('image/shotgun.png')
        elif stats.rifle:
            self.weapon_img = pygame.image.load('image/rifle.png')
        elif stats.bazooka:
            self.weapon_img = pygame.image.load('image/bazooka.png')
        else:
            self.weapon_img = pygame.image.load('image/orc.png')
        self.weapon_img_rect = self.weapon_img.get_rect()
        self.weapon_img_rect.centerx = self.screen_rect.left + 335
        self.weapon_img_rect.centery = self.screen_rect.bottom - 35

    def weapon_image_draw(self):
        self.screen.blit(self.weapon_img, self.weapon_img_rect)


