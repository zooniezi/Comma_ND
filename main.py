from turtle import width
import pygame as pg
import pymunk
import pymunk.pygame_util
import math

pg.init()

WIDTH = 1000
HEIGHT = 800

window = pg.display.set_mode((WIDTH, HEIGHT))

def draw(space, window, drawoption):
    window.fill("white")
    space.debug_draw(drawoption)
    pg.display.update()

def createBall(space):
    radius = 50
    ballBody = pymunk.Body()
    ballBody.position = (WIDTH/2, HEIGHT/2)
    ballShape = pymunk.Circle(ballBody, radius)
    ballShape.mass = 100
    ballShape.color = (255,0,0,100)
    ballShape.elasticity = 0.9
    ballShape.friction = 0.4
    space.add(ballBody, ballShape)

    return ballShape

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
    realSpace.gravity = (100, 981)

    realBall = createBall(realSpace)
    createWall(realSpace)

    drawOptions = pymunk.pygame_util.DrawOptions(window)

    while run:
        #종료조건 확인
        for nowEvent in pg.event.get():
            if nowEvent.type == pg.QUIT:
                run = False
                break
        draw(realSpace, window, drawOptions)
        realSpace.step(deltaTime)
        clock.tick(fps)
        
    pg.quit()

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)

 