import pygame
import random
import math


pygame.init()
shoot_sound = pygame.mixer.Sound('music/Shoot.wav')
class Pistol_Bullet(pygame.sprite.Sprite):
    '''Метод инициализации (графика(screen), пушка(gun)'''
    def __init__(self, screen, orc):
        super(Pistol_Bullet, self).__init__()
        '''инициализация пули'''
        self.screen = screen
        '''создание спрайта пули'''
        self.bullet_img = pygame.image.load('image/bullet.png')
        self.rect = self.bullet_img.get_rect()
        '''скорость'''
        self.speed = 1
        '''место появления по оси ИКС'''
        self.rect.centerx = orc.rect.centerx
        '''место появления по оси Игрик'''
        self.rect.top = orc.rect.top
        '''Преобразование целых чисел в вещественные (float(десятичные)'''
        self.y = float(self.rect.y)

    def update(self, screen, orc, pbg):
        '''перемещение пули вверх'''

        self.y -= self.speed
        '''обносление позиции пули'''
        self.rect.y = self.y

    def draw_player_bullet(self):
        '''Рисуем пулю на экране'''
        self.screen.blit(self.bullet_img, self.rect)

class Two_Pistol_Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, orc, pbg):
        super(Two_Pistol_Bullet, self).__init__()
        self.screen = screen
        self.bullet_img = pygame.image.load('image/bullet.png')
        self.rect = self.bullet_img.get_rect()
        self.speed = 1
        self.rect.top = orc.rect.top
        if len(pbg) % 2 == 0:
            self.rect.centerx = orc.rect.left
        else:
            self.rect.centerx = orc.rect.right
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.TPB_fire_time = False
    def update(self, screen, orc, pbg):
        self.y -= self.speed
        self.rect.y = self.y
    def fire(self, screen, orc, pbg):
        if self.TPB_fire_time:
            for i in range(2):
                TPB = Two_Pistol_Bullet(screen, orc, pbg)
                pbg.add(TPB)
            shoot_sound.play()
            self.TPB_fire_time = False
    def draw_player_bullet(self):
        '''Рисуем пулю на экране'''
        self.screen.blit(self.bullet_img, self.rect)

class Machinegun_Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, orc):
        super(Machinegun_Bullet, self).__init__()
        self.screen = screen
        self.bullet_img = pygame.image.load('image/bullet1.png')
        self.rect = self.bullet_img.get_rect()
        self.speed = 1.5
        self.angel = random.uniform(-0.1, 0.1)
        self.bullet_img = pygame.transform.rotate(self.bullet_img, math.atan(self.angel / 1) * 180 / 3.14)
        self.rect.centerx = orc.rect.centerx
        self.rect.top = orc.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.MB_time = 0
        self.MB_fire_time = False

    def update(self, screen, orc, pbg):
        self.y -= self.speed
        self.rect.y = self.y
        self.x -= self.angel
        self.rect.x = self.x

    def fire(self, screen, orc, pbg):
        if self.MB_fire_time:
            self.MB_time += 10
            if self.MB_time % 300 == 0:
                MB = Machinegun_Bullet(screen, orc)
                pbg.add(MB)
                shoot_sound.play()
            if self.MB_time >= 1200:
                self.MB_time = 0
                self.MB_fire_time = False

    def draw_player_bullet(self):
        '''Рисуем пулю на экране'''
        self.screen.blit(self.bullet_img, self.rect)

class Shotgun_Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, orc):
        super(Shotgun_Bullet, self).__init__()
        self.screen = screen
        self.bullet_img = pygame.image.load('image/bullet2.png')
        self.rect = self.bullet_img.get_rect()
        self.speed = 0.7
        self.angel = random.uniform(-0.4, 0.4)
        self.bullet_img = pygame.transform.rotate(self.bullet_img, math.atan(self.angel/1)*180/3.14)
        self.rect.centerx = orc.rect.centerx
        self.rect.top = orc.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.SHB_time = 0
        self.SHB_fire_time = False
        self.SHB_load = True

    def update(self, screen, orc, pbg):
        self.y -= self.speed
        self.rect.y = self.y
        self.x -= self.angel
        self.rect.x = self.x

    def fire(self, screen, orc, pbg):
        if self.SHB_load:
            if self.SHB_fire_time:
                for i in range(5):
                    SHB = Shotgun_Bullet(screen, orc)
                    shoot_sound.play()
                    shoot_sound.set_volume(0.5)
                    pbg.add(SHB)
                    self.SHB_fire_time = False
                    self.SHB_load = False
        if self.SHB_load == False:
            self.SHB_time += 1
            if self.SHB_time == 300:
                self.SHB_time = 0
                self.SHB_load = True

    def draw_player_bullet(self):
        '''Рисуем пулю на экране'''
        self.screen.blit(self.bullet_img, self.rect)

class Rifle_Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, orc):
        super(Rifle_Bullet, self).__init__()
        self.screen = screen
        self.bullet_img = pygame.image.load('image/bullet3.png')
        self.rect = self.bullet_img.get_rect()
        self.speed = 4
        self.rect.centerx = orc.rect.centerx
        self.rect.top = orc.rect.top
        self.y = float(self.rect.y)
        self.RB_time = 0
        self.RB_fire_time = False
        self.RB_load = True

    def update(self, screen, orc, pbg):
        self.y -= self.speed
        self.rect.y = self.y
    def fire(self, screen, orc, pbg):
        if self.RB_load:
            if self.RB_fire_time:
                RB = Rifle_Bullet(screen, orc)
                shoot_sound.play()
                shoot_sound.set_volume(0.5)
                pbg.add(RB)
                self.RB_fire_time = False
                self.RB_load = False
        if self.RB_load == False:
            self.RB_time += 1
            if self.RB_time == 200:
                self.RB_time = 0
                self.RB_load = True

    def draw_player_bullet(self):
        self.screen.blit(self.bullet_img, self.rect)

class Bazooka_Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, orc):
        super(Bazooka_Bullet, self).__init__()
        self.screen = screen
        self.bullet_img = pygame.image.load('image/bullet5.png')
        self.rect = self.bullet_img.get_rect()
        self.speed = 0.5
        self.rect.centerx = orc.rect.centerx
        self.rect.top = orc.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.move_time = 1
        self.BB_time = 0
        self.BB_fire_time = False
        self.BB_load = True
    def update(self, screen, orc, pbg):
        self.y -= self.speed
        self.rect.y = self.y
        if self.move_time >= 0:
            self.move_time += 1
            self.x += self.speed
            self.rect.x = self.x
            if self.move_time == 50:
                self.move_time = -1
        if self.move_time <= 0:
            self.move_time -= 1
            self.x -= self.speed
            self.rect.x = self.x
            if self.move_time == -50:
                self.move_time = 1
    def fire(self, screen, orc, pbg):
        if self.BB_load:
            if self.BB_fire_time:
                BB = Bazooka_Bullet(screen, orc)
                shoot_sound.play()
                shoot_sound.set_volume(0.5)
                pbg.add(BB)
                self.BB_fire_time = False
                self.BB_load = False
        if self.BB_load == False:
            self.BB_time += 1
            if self.BB_time == 500:
                self.BB_time = 0
                self.BB_load = True
    def draw_player_bullet(self):
        self.screen.blit(self.bullet_img, self.rect)


'''Лутбоксы'''
class Lootbox(pygame.sprite.Sprite):
    def __init__(self, screen, enemys):
        super(Lootbox, self).__init__()
        self.screen = screen
        self.i = ('image/machingun_box.png',
                  'image/shotgun_box.png',
                  'image/pistol_box.png',
                  'image/rifle_box.png',
                  'image/live_box.png',
                  'image/bazooka_box.png',
                  'image/random_box.png',
                  'image/death_box.png')
        self.a = random.choice(self.i)
        self.lootbox_img = pygame.image.load(self.a)
        self.rect = self.lootbox_img.get_rect()
        self.speed = 0.5
        self.MB_time = 1
        for Enemy in enemys:
            self.rect.centerx = Enemy.rect.centerx
            self.rect.centery = Enemy.rect.centery
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self, screen, Enemy):
        self.y += self.speed
        self.rect.y = self.y
        if self.MB_time >= 0:
            self.MB_time += 1
            self.x += self.speed
            self.rect.x = self.x
            if self.MB_time == 300:
                self.MB_time = -1
        if self.MB_time <= 0:
            self.MB_time -= 1
            self.x -= self.speed
            self.rect.x = self.x
            if self.MB_time == -300:
                self.MB_time = 1

    def draw_lootbox(self):
        self.screen.blit(self.lootbox_img, self.rect)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Explosion, self).__init__()
        self.screen = screen
        self.explosion_img = pygame.image.load('image/explosion3.png')
        self.rect = self.explosion_img.get_rect()
        self.explosion = False

class Explosion_Anim(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Explosion_Anim, self).__init__()
        self.screen = screen
        self.explosion_anim = pygame.image.load('image/explosion3.png')
        self.rect_anim = self.explosion_anim.get_rect()
        self.time = 0
        self.explosion_anim_act = False

    def draw_explosion_anim(self):
        if self.explosion_anim_act:
            self.time += 1
            if self.time % 20 == 0:
                self.explosion_anim = pygame.transform.rotate(self.explosion_anim, 90)
            if self.time == 100:
                self.kill()
        self.screen.blit(self.explosion_anim, self.rect_anim)

class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, Enemy):
        super(Enemy_Bullet, self).__init__()
        self.screen = screen
        self.bullet_img = pygame.image.load('image/bullet.png')
        self.rect = self.bullet_img.get_rect()
        self.speed = 1
        self.angel = random.uniform(-0.3, 0.3)
        self.bullet_img = pygame.transform.rotate(self.bullet_img, math.atan(-self.angel / 1) * 180 / 3.14)
        self.bullet_img = pygame.transform.flip(self.bullet_img, True, True)
        self.rect.centerx = Enemy.rect.centerx
        self.rect.centery = Enemy.rect.centery
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    def update(self, screen, Enemy, ebg, enemys):
        self.y += self.speed
        self.rect.y = self.y
        self.x -= self.angel
        self.rect.x = self.x
    def draw_enemy_bullet(self):
        self.screen.blit(self.bullet_img, self.rect)


'''Управление пулями'''
def player_bullet_update(enemys, orc, pbg, ebg, stats, sc, controls, screen, enemy, menu, Enemy, plg, live, boxes, expl, expl_anim):
    death = pygame.mixer.Sound('music/Explosion.wav')
    explosion = Explosion(screen)
    explosion_anim = Explosion_Anim(screen)
    for new_player_bullet in pbg.copy():
        '''Если пуля нижнем пикселем вышла за экран'''
        if new_player_bullet.rect.bottom <= 0:
             '''удаляем пулю'''
             new_player_bullet.remove(pbg)
    for new_enemy_bullet in ebg.copy():
        if new_enemy_bullet.rect.bottom >= 650:
            new_enemy_bullet.remove(ebg)
    '''Создаем коллизию груп bullets и enemys с удалением пули(True) и пришельца(True). Создается словрь с ключем Bullet и значение Enemy'''
    if stats.rifle:
        pbg_enemys_collide = pygame.sprite.groupcollide(pbg, enemys, False, False)
    else:
        pbg_enemys_collide = pygame.sprite.groupcollide(pbg, enemys, True, False)
    '''Взрыв пули'''
    if not stats.bazooka:
        pygame.sprite.groupcollide(pbg, ebg, True, True)
    #if pygame.sprite.spritecollideany(orc, expl):
    #    controls.orc_kill(stats, orc, enemys, pbg, ebg, screen, enemy, menu, plg, live, expl, boxes)
    #if pygame.sprite.spritecollideany(orc, ebg):
    #    controls.orc_kill(stats, orc, enemys, pbg, ebg, screen, enemy, menu, plg, live, expl, boxes)
    '''коллизия пуль и врагов'''
    if pbg_enemys_collide:
        death.play()
        death.set_volume(0.3)
        '''Для группы enemys в нашем словаре collision по значениям (values)'''
        for enemys in pbg_enemys_collide.values():
            '''вычет жизней'''
            for Enemy in enemys:
                if not stats.bazooka:
                    Enemy.live -= 1
                    Enemy.damage = True
                    Enemy.update(enemys, stats, screen, ebg, orc,menu)
                    if Enemy.live <= 0:
                        Enemy.kill()
                        '''Добавляем к очкам +1 умноженную на длинну уничтоженного списка (lin) пришельцев(enemys)'''
                        stats.score += 1 * len(enemys)
                        '''лутбоксы'''
                        lootbox = Lootbox(screen, enemys)
                        i = random.randint(0, 100)
                        '''шанс лутбокса'''
                        if i > 10:
                            boxes.add(lootbox)
            '''урон от базуки'''
            if stats.bazooka:

                for Enemy in enemys:
                    explosion.rect.centerx = Enemy.rect.centerx
                    explosion.rect.centery = Enemy.rect.centery
                    explosion_anim.rect_anim.centerx = Enemy.rect.centerx
                    explosion_anim.rect_anim.centery = Enemy.rect.centery

                expl_anim.add(explosion_anim)
                expl.add(explosion)

                explosion.explosion = True
                explosion_anim.explosion_anim_act = True
                #print(explosion.explosion)
            sc.image_score()
            '''Вызываем проверку рекорда'''
            controls.check_high_score(stats, sc)
            pygame.display.update()
            #for Enemy in enemys:
            #    enemys.remove(Enemy)
            #    Enemy.image = pygame.image.load('image/scull.png')
            #    Enemy.screen.blit(Enemy.image, Enemy.rect)
                #pygame.display.update()
            #    Enemy.death = True
    if stats.bazooka:
        bullet_bullet_collide = pygame.sprite.groupcollide(pbg, ebg, True, True)
        if bullet_bullet_collide:
            death.play()
            death.set_volume(0.3)
            for ebg in bullet_bullet_collide.values():
                for bullet in ebg:
                    explosion.rect.centerx = bullet.rect.centerx
                    explosion.rect.centery = bullet.rect.centery
                    explosion_anim.rect_anim.centerx = bullet.rect.centerx
                    explosion_anim.rect_anim.centery = bullet.rect.centery
                expl_anim.add(explosion_anim)
                expl.add(explosion)
                explosion.explosion = True

'''взрыв'''
def explosion(expl, screen, stats, sc, ebg, enemys, Enemy):
    expl_enemy_collide = pygame.sprite.groupcollide(expl, enemys, True, False)
    for enemys in expl_enemy_collide.values():
        '''вычет жизней'''
        for enemy in enemys:
            enemy.live -= 1
            Enemy.damage = True
            print('жизни врага', enemy.live)
            if enemy.live <= 0:
                stats.score += 1 * (len(enemys)//2)
                enemy.kill()
        sc.image_score()
    pygame.sprite.groupcollide(expl, ebg, False, True)


