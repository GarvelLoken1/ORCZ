import pygame
from pygame.sprite import Group

class Live(pygame.sprite.Sprite):
    def __init__(self, screen, stats):
        super(Live, self).__init__()
        self.screen = screen
        self.stats = stats
        self.image = pygame.image.load('image/orc.png')
        self.font = pygame.font.Font('OutlinePixel7.ttf', 36)
        self.text_color = (67, 160, 71)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        self.live_update(stats)


    def lives_group(self, plg, screen, stats):
        for lives_number in range(stats.live):
            Lives = Live(screen, stats)
            Lives.rect.x = Lives.rect.centerx - 2 * Lives.rect.width + (lives_number * (Lives.rect.width + 20)) - 65
            Lives.rect.bottom = self.screen_rect.bottom - 10
            plg.add(Lives)

    def live_update(self, stats):
        self.txt = self.font.render(str(stats.live), True, self.text_color)
        self.rect_txt = self.txt.get_rect()
        self.rect.centerx = self.screen_rect.centerx - 10
        self.rect.bottom = self.screen_rect.bottom - 10
        self.rect_txt.centerx = self.rect.centerx - 50
        self.rect_txt.bottom = self.screen_rect.bottom - 15

    def live_draw(self, plg, stats):
        #self.screen.blit(self.image, self.rect)
        if stats.live <= 3:
            plg.draw(self.screen)
        else:
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.txt, self.rect_txt)




