import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 屏幕刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_sprite, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_sprite)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class BackGround(GameSprite):
    def __init__(self, is_alt=False):

        # 1.调用父类方法实现精灵背景的创建
        super().__init__("./images/background.png")
        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类的方法
        super().update()

        # 2.判断是否移出屏幕，如果移出屏幕，则将图像移到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):

        # 1.调用父类方法，创建敌机精灵，指定敌机的图片
        super().__init__("./images/enemy1.png")
        # 2.随机指定敌机的初始飞行速度
        self.speed = random.randint(1, 3)
        # 3.随机指定敌机的初始出现位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1. 调用父类方法，保持垂直向下的飞机
        super().update()
        # 2. 判断敌机是否飞出屏幕，如果飞出，要从精灵组里删除
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组中删除")
            # kill()可以将敌机从所有精灵组中删除
            self.kill()

    def __del__(self):
        # print("敌机嘎了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):

        # 1.调用父类方法，设置images&speed
        super().__init__("./images/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 3.创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向上移动
        self.rect.x += self.speed

        # 判断英雄左右移动的位置
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")
        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置子弹的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3.将子弹精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 调用父类方法，绘制子弹图片，并且设置初始速度
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 调用父类方法，让子弹垂直飞行
        super().update()
        # 判断子弹是否飞出屏幕上方
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹发射了...")