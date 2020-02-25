import pygame
win_h=500
win_w=1000
window=pygame.display.set_mode((win_w,win_h))
run=True
clock=pygame.time.Clock()
ball_x=200
ball_y=200
speed_x=2
speed_y=2
ball_r=50
rect_x=0
rect_y=0
rect_w=30
rect_h=150
while run:
    clock.tick(30)
    window.fill((255,0,63))
    keys=pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_g:
                speed_y+=10
    if keys[pygame.K_s] and not(rect_y+rect_h>=win_h):
        rect_y+=20
    if keys[pygame.K_w] and not(rect_y<=0):
        rect_y-=20

    pygame.draw.circle(window,(100,2,2),(ball_x,ball_y),ball_r)
    pygame.draw.rect(window,(140,30,20),(rect_x,rect_y,rect_w,rect_h))
    ball_x+=speed_x
    ball_y+=speed_y
    if ball_x + ball_r >= win_w or ball_x-ball_r<=0:
        speed_x*=-1
    if ball_y + ball_r >= win_h or ball_y-ball_r<=0:
        speed_y*=-1

    pygame.display.update()
