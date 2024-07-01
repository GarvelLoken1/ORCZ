import pygame
'''Начальное меню'''
class Menu(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Menu, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.select = pygame.image.load('image/select.png')
        self.select_rect_start = self.select.get_rect()
        self.select_rect_dif = self.select.get_rect()
        self.select_rect_exit = self.select.get_rect()
        self.select_rect_easy = self.select.get_rect()
        self.select_rect_norm = self.select.get_rect()
        self.select_rect_hard = self.select.get_rect()
        self.select_back_to_game = self.select.get_rect()
        self.select_back_to_menu = self.select.get_rect()
        self.font = pygame.font.Font('OutlinePixel7.ttf', 50)#, bold=True, italic=False)
        self.font2 = pygame.font.Font('OutlinePixel7.ttf', 32)#, bold=True, italic=False)
        self.text_color = (68, 22, 6)
        self.color = 76, 175, 79
        self.menu_start = True
        self.menu_difficulty = False
        self.menu_exit = False
        self.dif_easy = True
        self.dif_norm = False
        self.dif_hard = False
        self.pause_btg = True
        self.pause_btm = False
        self.start()
        self.difficulty()
        self.exit()
        self.easy()
        self.norm()
        self.hard()
        self.back_to_game()
        self.back_to_menu()
        self.bg_lvl()
        self.bg_menu()
        self.game_over()
    '''Кнопка Старт'''
    def start(self):
        self.start_txt = self.font.render('ПАГНАЛИ!!!', True, self.text_color)
        self.start_txt_rect = self.start_txt.get_rect()

        self.start_txt_rect.center = self.screen_rect.center
        self.select_rect_start.right = self.start_txt_rect.left - 20
        self.select_rect_start.centery = self.start_txt_rect.centery
    '''Сложность'''
    def difficulty(self):
        self.difficulty_txt = self.font.render('СЛОЖНАСТЬ', True, self.text_color)
        self.difficulty_txt_rect = self.difficulty_txt.get_rect()
        self.difficulty_txt_rect.centerx = self.screen_rect.centerx
        self.difficulty_txt_rect.centery = self.screen_rect.centery + 82
        self.select_rect_dif.right = self.difficulty_txt_rect.left - 20
        self.select_rect_dif.centery = self.difficulty_txt_rect.centery
    '''Кнопка выход'''
    def exit(self):
        self.exit_txt = self.font.render('СВАЛИТЬ', True, self.text_color)
        self.exit_txt_rect = self.exit_txt.get_rect()
        self.exit_txt_rect.centerx = self.screen_rect.centerx
        self.exit_txt_rect.centery = self.screen_rect.centery + 164
        self.select_rect_exit.right = self.exit_txt_rect.left - 20
        self.select_rect_exit.centery = self.exit_txt_rect.centery

    '''Сложности'''

    '''Легкая'''
    def easy(self):
        self.easy_txt = self.font.render('БОЙЗ', True, self.text_color)
        self.easy_txt_rect = self.easy_txt.get_rect()
        self.easy_txt_rect.center = self.screen_rect.center
        self.select_rect_easy.right = self.easy_txt_rect.left - 20
        self.select_rect_easy.centery = self.easy_txt_rect.centery
    '''Норм'''
    def norm(self):
        self.norm_txt = self.font.render('НОБА', True, self.text_color)
        self.norm_txt_rect = self.norm_txt.get_rect()
        self.norm_txt_rect.centerx = self.screen_rect.centerx
        self.norm_txt_rect.centery = self.screen_rect.centery + 82
        self.select_rect_norm.right = self.norm_txt_rect.left - 20
        self.select_rect_norm.centery = self.norm_txt_rect.centery
    '''Сложно'''
    def hard(self):
        self.hard_txt = self.font.render('ВАРБОЗ', True, self.text_color)
        self.hard_txt_rect = self.hard_txt.get_rect()
        self.hard_txt_rect.centerx = self.screen_rect.centerx
        self.hard_txt_rect.centery = self.screen_rect.centery + 164
        self.select_rect_hard.right = self.hard_txt_rect.left - 20
        self.select_rect_hard.centery = self.hard_txt_rect.centery

        '''Пауза'''
    def back_to_game(self):
        self.back_to_game_txt = self.font.render('ПРОДОЛЖИТЬ ДАКУ', True, self.text_color)
        self.back_to_game_txt_rect = self.back_to_game_txt.get_rect()
        self.back_to_game_txt_rect.center = self.screen_rect.center
        self.select_back_to_game.right = self.back_to_game_txt_rect.left - 20
        self.select_back_to_game.centery = self.back_to_game_txt_rect.centery

    def back_to_menu(self):
        self.back_to_menu_txt = self.font.render('В МЕНЮ', True, self.text_color)
        self.back_to_menu_txt_rect = self.back_to_menu_txt.get_rect()
        self.back_to_menu_txt_rect.centerx = self.screen_rect.centerx
        self.back_to_menu_txt_rect.centery = self.screen_rect.centery + 82
        self.select_back_to_menu.right = self.back_to_menu_txt_rect.left - 20
        self.select_back_to_menu.centery = self.back_to_menu_txt_rect.centery


        '''Отрисовка сложностей'''
    def draw_difficulty(self):
        if self.dif_easy:
            self.screen.blit(self.easy_txt, self.easy_txt_rect)
            self.screen.blit(self.norm_txt, self.norm_txt_rect)
            self.screen.blit(self.hard_txt, self.hard_txt_rect)
            self.screen.blit(self.select, self.select_rect_easy)
        if self.dif_norm:
            self.screen.blit(self.easy_txt, self.easy_txt_rect)
            self.screen.blit(self.norm_txt, self.norm_txt_rect)
            self.screen.blit(self.hard_txt, self.hard_txt_rect)
            self.screen.blit(self.select, self.select_rect_norm)
        if self.dif_hard:
            self.screen.blit(self.easy_txt, self.easy_txt_rect)
            self.screen.blit(self.norm_txt, self.norm_txt_rect)
            self.screen.blit(self.hard_txt, self.hard_txt_rect)
            self.screen.blit(self.select, self.select_rect_hard)
        '''Отрисовка меню'''
    def draw_menu(self):
        if self.menu_start:
            self.screen.blit(self.start_txt, self.start_txt_rect)
            self.screen.blit(self.difficulty_txt, self.difficulty_txt_rect)
            self.screen.blit(self.exit_txt, self.exit_txt_rect)
            self.screen.blit(self.select, self.select_rect_start)
        if self.menu_difficulty:
            self.screen.blit(self.start_txt, self.start_txt_rect)
            self.screen.blit(self.difficulty_txt, self.difficulty_txt_rect)
            self.screen.blit(self.exit_txt, self.exit_txt_rect)
            self.screen.blit(self.select, self.select_rect_dif)
        if self.menu_exit:
            self.screen.blit(self.start_txt, self.start_txt_rect)
            self.screen.blit(self.difficulty_txt, self.difficulty_txt_rect)
            self.screen.blit(self.exit_txt, self.exit_txt_rect)
            self.screen.blit(self.select, self.select_rect_exit)

        '''Отрисовка паузы'''
    def draw_pause(self):
        if self.pause_btg:
            self.screen.blit(self.back_to_game_txt, self.back_to_game_txt_rect)
            self.screen.blit(self.back_to_menu_txt, self.back_to_menu_txt_rect)
            self.screen.blit(self.select, self.select_back_to_game)
        if self.pause_btm:
            self.screen.blit(self.back_to_game_txt, self.back_to_game_txt_rect)
            self.screen.blit(self.back_to_menu_txt, self.back_to_menu_txt_rect)
            self.screen.blit(self.select, self.select_back_to_menu)

    def game_over(self):
        '''рендерим(render) шрифт(font) как строку(str) (Очки, ???, цвет шрифта, цвет фона)'''
        self.gameover = self.font.render('ТИБЯ НАСТУКАЛИ!', True, self.text_color)
        self.restart = self.font2.render('ЖМИ "Enter" ШОБЫ ИЩО ИЛИ "ESC" ШОБЫ БИЖАТЬ', True, self.text_color)
        '''Получаем графический объект счетчика рекорда'''
        self.game_over_rect = self.gameover.get_rect()
        self.restart_rect = self.restart.get_rect()
        '''Отрисовываем на экране'''
        self.restart_rect.centerx = self.screen_rect.centerx
        self.restart_rect.centery = self.screen_rect.centery + 60
        self.game_over_rect.center = self.screen_rect.center

    def game_over_show(self):
        self.screen.blit(self.gameover, self.game_over_rect)
        self.screen.blit(self.restart, self.restart_rect)

    '''Бэкграунд'''
    def bg_lvl(self):
        self.bg_lvl_img = pygame.image.load('image/bg_lvl.jpg')
        self.bg_lvl_rect = self.bg_lvl_img.get_rect()
        self.bg_lvl_rect.center = self.screen_rect.center
        self.plank_img = pygame.image.load('image/plank.png')
        self.plank_rect = self.plank_img.get_rect()
        self.plank_rect.centerx = self.screen_rect.centerx
        self.plank_rect.midbottom = self.screen_rect.midbottom
    def bg_lvl_draw(self):
        self.screen.blit(self.bg_lvl_img, self.bg_lvl_rect)
        self.screen.blit(self.plank_img, self.plank_rect)

    def bg_menu(self):
        self._bg_menu = pygame.image.load('image/bg_menu.png')
        self.bg_menu_rect = self._bg_menu.get_rect()
        self.bg_menu_rect.center = self.screen_rect.center
    def bg_menu_draw(self):
        self.screen.blit(self._bg_menu, self.bg_menu_rect)

