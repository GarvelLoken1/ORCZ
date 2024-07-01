'''Отслеживание статистики'''
class Stats():
    '''Инициализирует статистику'''
    def __init__(self):
        self.reset_stats()
        '''Проверка жизней'''
        self.run_game = False
        self.game_over = False
        self.menu_menu = True
        self.difficulty_menu = False
        self.pause = False
        self.fullscreen = False
        self.pistol = True
        self.two_pistols = False
        self.machingun = False
        self.shotgun = False
        self.rifle = False
        self.bazooka = False

        '''Открываем текстовый файл highscore.txt в режиме чтения (r) как файл f'''
        with open('highscore.tx', 'r') as f:
            '''считываем строку в текстовом файле и преобразуем в численное'''
            self.high_score = int(f.readline())
    '''статистика, меняющаяся во время игры'''
    def reset_stats(self):
        '''жизни'''
        self.live = 3
        '''очки'''
        self.score = 0
        '''lvl'''
        self.level = 0
