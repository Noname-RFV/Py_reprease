import pygame, random
from ctypes import *

print(windll.user32.GetSystemMetrics(0))
print(windll.user32.GetSystemMetrics(1))
# Инициализация PyGame
pygame.init()

# Настройки окна
# Использовать настраиваемое разрешение (0) или запустить во весь экран (1)
mode = 0
if mode:
    window_w = windll.user32.GetSystemMetrics(0)
    window_h = windll.user32.GetSystemMetrics(1)
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    window_w = 400
    window_h = 150
    window = pygame.display.set_mode((window_w, window_h), pygame.RESIZABLE)
pygame.display.set_caption("Pong by Freereod")
clock = pygame.time.Clock()


# Настройки шарика
class ball:
    def __init__(self, x, y, radius, colour, speed_x, speed_y, change):
        self.x = x  # Координата Х
        self.y = y  # Координата У
        self.radius = radius  # Радиус
        self.colour = colour  # Цвет в модели RGB
        self.speed_x = float(speed_x)  # Скорость по Х
        self.speed_y = float(speed_y)  # Скорость по У
        self.change = change  # Коэффициент ускорения

    # Проверка вылета за границу
    def check_range(self):
        if self.x + self.speed_x > window_w - self.radius - 5:
            self.speed_x *= -1 * self.change
        if self.x + self.speed_x < 0 + self.radius + 5:
            self.speed_x *= -1 * self.change
        if self.y + self.speed_y < 0 + self.radius + 5:
            self.speed_y *= -1 * self.change
        if self.y + self.speed_y > window_h - self.radius - 5:
            self.speed_y *= -1 * self.change

    # Отрисовка шарика
    def drawBall(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)
        self.x = round(self.x + self.speed_x)
        self.y = round(self.y + self.speed_y)
        self.check_range()

    def spawnBall(self, w, h):
        self.x = w // 2
        self.y = h // 2
        self.speed_x = random.randint(-20, 20)
        self.speed_y = random.randint(-20, 20)


run = True

bl = ball(window_w // 2, window_h // 2, 10, (255, 0, 0), random.randint(-20, 20), random.randint(-20, 20), 1)
gamer_ball = ball(30, 30, 10, (0, 255, 100), 0, 0, 1)
# Основной цикл программы
while run:
    clock.tick(30)
    # Проверяем нажатые клавиши
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Отработка движения мыши
        if event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            gamer_ball.x = mouse[0]
            gamer_ball.y = mouse[1]
    if keys[pygame.K_SPACE]:
        bl.spawnBall(window_w, window_h)  # Спавн шарика
    if keys[pygame.K_ESCAPE]:
        run = False  # Выход
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (100, 0, 255), (0, 0, 5, window_h))
    pygame.draw.rect(window, (100, 0, 255), (0, 0, window_w, 5))
    pygame.draw.rect(window, (100, 0, 255), (window_w, window_h, -5, -window_h))
    pygame.draw.rect(window, (100, 0, 255), (window_w, window_h, -window_w, -5))
    bl.drawBall(window)
    gamer_ball.drawBall(window)
    pygame.display.update()