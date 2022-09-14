import pygame as pg
import pymunk
import pymunk.pygame_util   
import math
import random

from source import LEFTLINE, RIGHTLINE, root3, Length ,c, P, pushvalue, floorheight, h

pg.init()

#중요변수들!
CAPTION = "Comma ND"
ICON = pg.image.load("ICON.png")

#size of window
WIDTH = 1000
HEIGHT = 1000


# number of dropped balls 
ball_number  = 500

# thickness of walls
thickness = 8

# initial value of the gravity
GRAVITY = 2500

#공이 떨어지는 깔대기 구축을 위한 변수 설정
k = 10
b = 100

d = 30

L1, L2, L3, L4 = (k, -100), (k, b), (WIDTH/2 - c, 200), (WIDTH/2 - c , 200+d)
R1, R2, R3, R4 = (WIDTH-k, -100), (WIDTH-k,b), (WIDTH/2 +c, 200), (WIDTH/2 + c, 200+d)
leftLine = [L1, L2, L3, L4]
rightLine = [R1, R2, R3, R4]

# function for make wall
# 외곽 뼈대 구축
def makeoutLine(space):
    for i in range(14):
        leftfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        leftfunnelShape = pymunk.Segment(leftfunnelBody, LEFTLINE[i],LEFTLINE[i+1], thickness)
        leftfunnelShape.elasticity = 0

        space.add(leftfunnelBody, leftfunnelShape)
        rightfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        rightfunnelShape = pymunk.Segment(rightfunnelBody, RIGHTLINE[i],RIGHTLINE[i+1], thickness)
        rightfunnelShape.elasticity = 0

        space.add(rightfunnelBody, rightfunnelShape)   
# 상단부 깔때기 구축
def makeFunnel(space):
    for i in range(3):
        leftfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        leftfunnelShape = pymunk.Segment(leftfunnelBody, leftLine[i],leftLine[i+1], thickness)
        space.add(leftfunnelBody, leftfunnelShape)
        rightfunnelBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        rightfunnelShape = pymunk.Segment(rightfunnelBody, rightLine[i],rightLine[i+1], thickness)
        space.add(rightfunnelBody, rightfunnelShape)

#create main window and set icon
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(CAPTION)
pg.display.set_icon(ICON)


def draw(space, window, drawoption):
    window.fill("black")
    space.debug_draw(drawoption)
    pg.display.update()

# 새로운 공을 생성할 때마다 공의 색깔을 임의의 색깔로 설정하기
def random_color(): 
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    opa=random.randint(0,100)
    return (red,green,blue,opa) #red,green,blue,opa(불투명도) 를 random으로 뽑아내고 밑에 createBall 함수에서 호출

# 공의 position을 랜덤으로 정하기
def random_postion(): 
    x=random.randint(500,950)
    # x=random.randint(L1(0)+40,R1(1)-40)
    y=random.randint(-100,100)
    return(x,y)

# 공 구축하기
def createBall(space, position):
    radius = 5
    ballBody = pymunk.Body()
    ballBody.position = position
    ballShape = pymunk.Circle(ballBody, radius)
    ballShape.mass = 100
    ballShape.color = random_color()
    ballShape.elasticity = 0.2
    ballShape.friction = 0.2
    space.add(ballBody, ballShape)

    return ballShape

# 정육각형 모양의 구조물 설치를 위한 좌표 설정! 시작점은 이미 source.py의 리스트 P로 저장되어있다. 
def regularHexagon(space, point): 
    HexPoint1=[1, 2]  
    HexPoint1[0] = point[0]-pushvalue
    HexPoint1[1] = point[1]+floorheight

    HexPoint2=[1, 2]  
    HexPoint2[0] = point[0]+pushvalue
    HexPoint2[1] = HexPoint1[1]

    HexPoint3=[1, 2]  
    HexPoint3[0] = HexPoint1[0]
    HexPoint3[1] = point[1]+floorheight+Length

    HexPoint4=[1, 2] 
    HexPoint4[0] = HexPoint2[0]
    HexPoint4[1] = HexPoint3[1]

    HexPoint5=[1, 2] 
    HexPoint5[0] = point[0] 
    HexPoint5[1] = HexPoint3[1]+floorheight

    leftwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    leftwayShape = pymunk.Segment(leftwayBody,point,HexPoint1,thickness)
    space.add(leftwayBody, leftwayShape)

    lleftwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    lleftwayShape = pymunk.Segment(lleftwayBody,HexPoint1,HexPoint3, thickness)
    space.add(lleftwayBody, lleftwayShape)

    llleftwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    llleftwayShape = pymunk.Segment(llleftwayBody,HexPoint3,HexPoint5, thickness)
    space.add(llleftwayBody, llleftwayShape)

    rightwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    rightwayShape = pymunk.Segment(rightwayBody,point,HexPoint2,thickness)
    space.add(rightwayBody, rightwayShape)

    rrightwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    rrightwayShape = pymunk.Segment(rrightwayBody,HexPoint2,HexPoint4, thickness)
    space.add(rrightwayBody, rrightwayShape)

    rrrightwayBody = pymunk.Body(body_type=pymunk.Body.STATIC)
    rrrightwayShape = pymunk.Segment(rrrightwayBody,HexPoint4,HexPoint5, thickness)
    space.add(rrrightwayBody, rrrightwayShape)
    

# 공이 흘러가는 파이프 세우기 
n = 7
piperadius = thickness

# 공이 흐르는 파이프(레일) 구축
def createPipe(space):
    for i in range(15):
            Rpoint1 = (WIDTH/2+i*2*h, P[25][1]+2*Length+20)
            Rpoint2 = (WIDTH/2+i*2*h,HEIGHT)
            RcontainerBody = pymunk.Body(body_type=pymunk.Body.STATIC)
            RcontainerShape = pymunk.Segment(RcontainerBody, Rpoint1,Rpoint2, piperadius)
            space.add(RcontainerBody, RcontainerShape)

            Lpoint1 = (WIDTH/2-(i+1)*2*h, P[25][1]+2*Length+20)
            Lpoint2 = (WIDTH/2-(i+1)*2*h,HEIGHT)
            LcontainerBody = pymunk.Body(body_type=pymunk.Body.STATIC)
            LcontainerShape = pymunk.Segment(LcontainerBody, Lpoint1,Lpoint2, piperadius)
            space.add(LcontainerBody, LcontainerShape)

# 공이 담길 벽(바구니) 구축
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

# main loop
def run(window, width, height):
    run = True
    clock = pg.time.Clock()
    fps = 60
    deltaTime = 1/fps
    realSpace = pymunk.Space()
    realSpace.gravity = (0, GRAVITY)  

    for i in range(ball_number):
        realBall=createBall(realSpace,random_postion()) #realSpace에 공 만들기    
    createWall(realSpace)
    makeFunnel(realSpace)
    createPipe(realSpace)
    makeoutLine(realSpace)
    for i in range(28):
        regularHexagon(realSpace,P[i+1])

    drawOptions = pymunk.pygame_util.DrawOptions(window)

    #For our team, print our name at console
    print("\nDigital Galton Board - Comma 2022 Summer project\nBy Jaejun Kim, Sangeun Youn, Yujin Jeong\n")


    while run:
        #종료조건 확인
        for nowEvent in pg.event.get():
            if nowEvent.type == pg.QUIT:
                run = False
                break
            # 실험을 위한 클릭시 클릭 좌표에 새로운 구슬을 생성하는 기능
            # if nowEvent.type == pg.MOUSEBUTTONDOWN:
            #     if nowEvent.button == 1:
            #         createBall(realSpace, pg.mouse.get_pos())
        draw(realSpace, window, drawOptions)
        realSpace.step(deltaTime)
        clock.tick(fps)
        
    pg.quit()

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)