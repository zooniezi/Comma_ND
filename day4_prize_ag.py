from turtle import width
import pygame as pg
import pymunk
import pymunk.pygame_util
import math
import random

pg.init()

WIDTH = 1000
HEIGHT = 800
speed = 3500
# 떨어지는 공의 개수 
ball_number  = 1000

k = 10
b = 100
c = 15
d = 30

L1, L2, L3, L4 = (k, -100), (k, b), (WIDTH/2 - c, 200), (WIDTH/2 - c , 200+d)
R1, R2, R3, R4 = (WIDTH-k, -100), (WIDTH-k,b), (WIDTH/2 +c, 200), (WIDTH/2 + c, 200+d)
leftLine = [L1, L2, L3, L4]
rightLine = [R1, R2, R3, R4]


window = pg.display.set_mode((WIDTH, HEIGHT))

def draw(space, window, drawoption):
    window.fill("black")
    space.debug_draw(drawoption)
    pg.display.update()

def random_color(): #클릭을 할때마다 공의 색깔을 결정하기 위해서
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    opa=random.randint(0,100)
    return (red,green,blue,opa) #이렇게 red,green,blue,opa를 random으로 뽑아내고 밑에 create_ball에서 얘네가 클릭될 때마다 새롭게 찍히고 있는것

def random_postion(): #공의 position을 랜덤으로 정하기
    x=random.randint(50,950)
    # x=random.randint(L1(0)+40,R1(1)-40)
    y=random.randint(-100,100)
    return(x,y)

def createBall(space, position):
    radius = 7
    ballBody = pymunk.Body()
    ballBody.position = position
    ballShape = pymunk.Circle(ballBody, radius)
    ballShape.mass = 100
    ballShape.color = random_color()
    ballShape.elasticity = 0.2
    ballShape.friction = 0.2
    space.add(ballBody, ballShape)

    return ballShape

n = 2             # 봉을 몇 층 세울 것 인가? 
geori = 50        # 떨어지는 공과 제일 위층 파이브 사이의 거리 
FFH = 200 + d + geori      # 1층의 높이 first floor height 
floorheight = 50        # 층과 층 사이의 거리 
pipeDistance = 60       # 한 층에서 봉과 봉 사이의 거리 
pushvalue = pipeDistance/2          # 민값 == 한 층과 다른 층 사이에 얼마나 거리가 있는 지 
piperadius = 9        # 봉의 반지름 
 

def createPipe(space):
    for i in range(15):
        for j in range(n): # pipe 만들기 
            rigthpipeBody=pymunk.Body(body_type=pymunk.Body.STATIC)
            rigthpipeBody.position=(WIDTH/2+i*pipeDistance+j*pushvalue,FFH+j*floorheight)
            rigthpipeShape=pymunk.Circle(rigthpipeBody,piperadius)
            rigthpipeShape.color=(255,0,0,100)
            rigthpipeShape.elasticity = 0.1
            rigthpipeShape.friction = 0.5
            space.add(rigthpipeBody,rigthpipeShape)

            leftpipeBody=pymunk.Body(body_type=pymunk.Body.STATIC)
            leftpipeBody.position=(WIDTH/2-(i+1)*pipeDistance+j*pushvalue,FFH+j*floorheight)
            leftpipeShape=pymunk.Circle(leftpipeBody,piperadius)
            leftpipeShape.color=(255,0,0,100)
            leftpipeShape.elasticity = 0.1
            leftpipeShape.friction = 0.5
            space.add(leftpipeBody,leftpipeShape)
            if j == n-1:   # 공을 받는 통 만들기 
                Rpoint1 = (WIDTH/2+i*pipeDistance+j*pushvalue,FFH+j*floorheight+40)
                Rpoint2 = (WIDTH/2+i*pipeDistance+j*pushvalue,HEIGHT)
                RcontainerBody = pymunk.Body(body_type=pymunk.Body.STATIC)
                RcontainerShape = pymunk.Segment(RcontainerBody, Rpoint1,Rpoint2, 8)
                space.add(RcontainerBody, RcontainerShape)

                Lpoint1 = (WIDTH/2-(i+1)*pipeDistance+j*pushvalue,FFH+j*floorheight+40)
                Lpoint2 = (WIDTH/2-(i+1)*pipeDistance+j*pushvalue,HEIGHT)
                LcontainerBody = pymunk.Body(body_type=pymunk.Body.STATIC)
                LcontainerShape = pymunk.Segment(LcontainerBody, Lpoint1,Lpoint2, 8)
                space.add(LcontainerBody, LcontainerShape)



    

def createWall(space):
    rects = [
        #[(중심x좌표, 중심y좌표), (가로, 세로)]
        #[(중심x좌표, 중심y좌표), (가로, 세로)]
        [(WIDTH/2, HEIGHT),(WIDTH, 40)]
    ]
    for center, size in rects:
        rectBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        rectBody.position = center
        rectShape = pymunk.Poly.create_box(rectBody, size)
        rectShape.elasticity = 0.4
        rectShape.friction = 0.4
        space.add(rectBody, rectShape)
    
def makeFunnel(space):
    for i in range(3):
        leftfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        leftfunnelShape = pymunk.Segment(leftfunnelBody, leftLine[i],leftLine[i+1], 8)
        space.add(leftfunnelBody, leftfunnelShape)
        rightfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        rightfunnelShape = pymunk.Segment(rightfunnelBody, rightLine[i],rightLine[i+1], 8)
        space.add(rightfunnelBody, rightfunnelShape)

# n = 2             # 봉을 몇 층 세울 것 인가? 
# FFH = 200 + d + 50      # 1층의 높이 first floor height 
# floorheight = 50        # 층과 층 사이의 거리 
# pipeDistance = 60       # 한 층에서 봉과 봉 사이의 거리 
# pushvalue = pipeDistance/2          # 민값 == 한 층과 다른 층 사이에 얼마나 거리가 있는 지 
# piperadius = 9        # 봉의 반지름 
 


a = [WIDTH/2 ,FFH]
# a1 = (WIDTH/2-pushvalue,FFH+floorheight)
# a2 = (WIDTH/2+pushvalue,FFH+floorheight)

# 공이 떨어지는 통로를 만들어보자 


def makeway(space, position): # position 은 리스트를 받는다. 
    position1=[1, 2]  # 아무의미 없는 숫자 -- 어짜피 바뀔 숫자다 
    position1[0] = position[0]-pushvalue
    position1[1] = position[1]+floorheight
    position2=[1, 2]  # 아무의미 없는 숫자 -- 어짜피 바뀔 숫자다 
    position2[0] = position[0]+pushvalue
    position2[1] = position[1]+floorheight
    position3=[1, 2]  # 아무의미 없는 숫자 -- 어짜피 바뀔 숫자다 
    position3[0] = position[0]-c
    position3[1] = position[1]-geori
    position4=[1, 2]  # 아무의미 없는 숫자 -- 어짜피 바뀔 숫자다 
    position4[0] = position[0]+c
    position4[1] = position[1]-geori
    position5=[1, 2]  # 아무의미 없는 숫자 -- 어짜피 바뀔 숫자다 

    angle = math.atan(floorheight/pushvalue)

    position5[0] = position1[0]-2*c/(math.sin(angle))
    position5[1] = position1[1]
    position6=[1, 2]  # 아무의미 없는 숫자 -- 어짜피 바뀔 숫자다 
    position6[0] = position2[0]+2*c/(math.sin(angle))
    position6[1] = position2[1]
    position = tuple(position)
    position1 = tuple(position1)
    position2 = tuple(position2)
    position3 = tuple(position3)
    position4 = tuple(position4)
    position5 = tuple(position5)
    position6 = tuple(position6)
    leftwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    leftwayShape = pymunk.Segment(leftwayBody,position ,position1, 8)
    space.add(leftwayBody, leftwayShape)
    rightwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    rightwayShape = pymunk.Segment(rightwayBody, position,position2, 8)
    space.add(rightwayBody, rightwayShape)
    lleftwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    lleftwayShape = pymunk.Segment(lleftwayBody,position3 ,position5, 8)
    space.add(lleftwayBody, lleftwayShape)
    rrightwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    rrightwayShape = pymunk.Segment(rrightwayBody, position4,position6, 8)
    space.add(rrightwayBody, rrightwayShape)
    






#main loop
def run(window, width, height):
    run = True
    clock = pg.time.Clock()
    fps = 60
    deltaTime = 1/fps
    realSpace = pymunk.Space()
    realSpace.gravity = (0, speed)  # 3500 

    for i in range(ball_number):
        realBall=createBall(realSpace,random_postion()) #realSpace에 공 만들기    
    createWall(realSpace)
    makeFunnel(realSpace)
    #createPipe(realSpace)
    makeway(realSpace,a)


    drawOptions = pymunk.pygame_util.DrawOptions(window)

    while run:
        #종료조건 확인
        for nowEvent in pg.event.get():
            if nowEvent.type == pg.QUIT:
                run = False
                break
            # if nowEvent.type == pg.MOUSEBUTTONDOWN:
            #     if nowEvent.button == 1:
            #         createBall(realSpace, pg.mouse.get_pos())
        draw(realSpace, window, drawOptions)
        realSpace.step(deltaTime)
        clock.tick(fps)
        
    pg.quit()

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)

 