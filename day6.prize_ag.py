from tkinter import RIGHT
from turtle import width
import pygame as pg
import pymunk
import pymunk.pygame_util   
import math
import random

from source import L10, L12, L16, L5, L6, L7, L8, L9 , L11, L13, L14, L15 ,L16,L17,L18, R5, R6, R7 , R8, R9, R10, R11, R12 ,a , Length ,R13, R14, R15 ,R16,R17,R18

pg.init()

WIDTH = 1000
HEIGHT = 1000
speed = 1500
# 떨어지는 공의 개수 
ball_number  = 500
thickness = 9


#공이 떨어지는 깔대기 만들기(설계)
k = 10
b = 100
c = 17
d = 30

L1, L2, L3, L4 = (k, -100), (k, b), (WIDTH/2 - c, 200), (WIDTH/2 - c , 200+d)
R1, R2, R3, R4 = (WIDTH-k, -100), (WIDTH-k,b), (WIDTH/2 +c, 200), (WIDTH/2 + c, 200+d)
leftLine = [L1, L2, L3, L4]
rightLine = [R1, R2, R3, R4]

LEFTLINE = [L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18]
RIGHTLINE = [R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18]

def makeoutline(space):
    for i in range(14):
        leftfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        leftfunnelShape = pymunk.Segment(leftfunnelBody, LEFTLINE[i],LEFTLINE[i+1], thickness)
        leftfunnelShape.elasticity = 0

        space.add(leftfunnelBody, leftfunnelShape)
        rightfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        rightfunnelShape = pymunk.Segment(rightfunnelBody, RIGHTLINE[i],RIGHTLINE[i+1], thickness)
        rightfunnelShape.elasticity = 0

        space.add(rightfunnelBody, rightfunnelShape)   




def makeFunnel(space):
    for i in range(3):
        leftfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        leftfunnelShape = pymunk.Segment(leftfunnelBody, leftLine[i],leftLine[i+1], thickness)
        space.add(leftfunnelBody, leftfunnelShape)
        rightfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        rightfunnelShape = pymunk.Segment(rightfunnelBody, rightLine[i],rightLine[i+1], thickness)
        space.add(rightfunnelBody, rightfunnelShape)

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

# 윤상은이 만든거 
def createBall_prize(space, position):
    radius = 4
    ballBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    ballBody.position = position
    ballShape = pymunk.Circle(ballBody, radius)
    # ballShape.mass = 100
    ballShape.color = random_color()
    ballShape.elasticity = 0.2
    ballShape.friction = 0.2
    space.add(ballBody, ballShape)

    return ballShape

geori =35
FFH = 200+d+geori
pushvalue = a/2*Length
floorheight = Length/2

h= a*Length/2+c
i= 3*Length/2+a*c

P1 = [WIDTH/2 ,FFH]
P2= (WIDTH/2-h,FFH + i)
P3= (WIDTH/2+h,FFH + i)

P4= (WIDTH/2-2*h,FFH + 2*i)
P5= (WIDTH/2,FFH + 2*i)
P6= (WIDTH/2+2*h,FFH + 2*i)

P7= (WIDTH/2-3*h,FFH + 3*i)
P8= (WIDTH/2-h,FFH + 3*i)
P9= (WIDTH/2+h,FFH + 3*i)
P10= (WIDTH/2+3*h,FFH + 3*i)
P11 = [WIDTH/2-4*h ,FFH+4*i]
P12= (WIDTH/2-2*h,FFH+4*i)
P13= (WIDTH/2,FFH+4*i)
P14= (WIDTH/2+2*h,FFH+4*i)
P15= (WIDTH/2+4*h,FFH+4*i)

P16= (WIDTH/2-5*h,FFH+5*i)
P17= (WIDTH/2-3*h,FFH+5*i)
P18= (WIDTH/2-h,FFH + 5*i)
P19= (WIDTH/2+h,FFH + 5*i)
P20= (WIDTH/2+3*h,FFH +5*i)
P21= (WIDTH/2+5*h,FFH +5*i)
P22= (WIDTH/2-6*h,FFH+6*i)
P23= (WIDTH/2-4*h,FFH+6*i)
P24= (WIDTH/2-2*h,FFH +6*i)
P25= (WIDTH/2,FFH +6*i)
P26= (WIDTH/2+2*h,FFH +6*i)
P27= (WIDTH/2+4*h,FFH +6*i)
P28= (WIDTH/2+6*h,FFH +6*i)


P = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10,P11, P12, P13, P14, P15, P16, P17, P18, P19, P20 ,P21, P22, P23, P24, P25, P26, P27, P28]


def RH1(space, point): # position 은 리스트를 받는다. 
    P11=[1, 2]  
    P11[0] = point[0]-pushvalue
    P11[1] = point[1]+floorheight

    P12=[1, 2]  
    P12[0] = point[0]+pushvalue
    P12[1] = P11[1]

    P13=[1, 2]  
    P13[0] = P11[0]
    P13[1] = point[1]+floorheight+Length

    P14=[1, 2] 
    P14[0] = P12[0]
    P14[1] = P13[1]

    P15=[1, 2] 
    P15[0] = point[0] 
    P15[1] = P13[1]+floorheight

    leftwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    leftwayShape = pymunk.Segment(leftwayBody,point,P11,thickness)
    space.add(leftwayBody, leftwayShape)

    lleftwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    lleftwayShape = pymunk.Segment(lleftwayBody,P11,P13, thickness)
    space.add(lleftwayBody, lleftwayShape)

    llleftwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    llleftwayShape = pymunk.Segment(llleftwayBody,P13,P15, thickness)
    space.add(llleftwayBody, llleftwayShape)

    rightwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    rightwayShape = pymunk.Segment(rightwayBody,point,P12,thickness)
    space.add(rightwayBody, rightwayShape)

    rrightwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    rrightwayShape = pymunk.Segment(rrightwayBody,P12,P14, thickness)
    space.add(rrightwayBody, rrightwayShape)

    rrrightwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    rrrightwayShape = pymunk.Segment(rrrightwayBody,P14,P15, thickness)
    space.add(rrrightwayBody, rrrightwayShape)
    


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

    makeoutline(realSpace)
    for i in range(28):
        RH1(realSpace,P[i])

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