from cmath import rect
import re
import pygame as pg #pygame을 불러오기 + pg로 줄어서 쓰겠다고 선언
import pymunk
import pymunk.pygame_util
import math
import random

pg.init() #게임이 열림

length = 1000 #내가 만드는 창의 가로 길이
height = 600 #내가 만드는 창의 세로 길이

window=pg.display.set_mode((length,height)) #창의 크기 설정 
#--> pygame안에 있는 display안에 있는 set_mode를 사용하여 창의 크기를 설정하기 그리고 변수로 값을 대입
# 참고로 창의 x축이 오른쪽 y축이 아래로 갈수록 증가하는것이고, 원점은 왼쪽 맨 윗점이 원점

def draw(space,window,draw_option): #draw 함수를 정의하고, 이 함수의 매개변수는 space,window,draw_option이 있음
    window.fill("white") #윈도우 창을 흰색으로 모두 채우겠다는 의미   # 여기서 의미하는 윈도우가 위에 있는 윈도우...?는 아닌거 같은데 음...?
    space.debug_draw(draw_option)
    pg.display.update()

def random_color(): #클릭을 할때마다 공의 색깔을 결정하기 위해서
    red=random.randint(0,256)
    green=random.randint(0,256)
    blue=random.randint(0,256)
    opa=random.randint(0,101)
    return (red,green,blue,opa) #이렇게 red,green,blue,opa를 random으로 뽑아내고 밑에 create_ball에서 얘네가 클릭될 때마다 새롭게 찍히고 있는것

def create_ball(space,position): #create_ball을 찍어내는 기계하고 생각, create_ball이라는 함수를 정의하고 이 함수의 매개변수는 space
    radius=50 #반지름은 50으로 설정
    ball_body=pymunk.Body() #pymunk에 있는 body를 사용
    ball_body.position=position #위치 설정하기, 튜플을 괄호가 필요없음
    ball_shape=pymunk.Circle(ball_body,radius) #모양과 반지름
    ball_shape.mass=100 #질량
    ball_shape.color=random_color() #rgb와 불투명도
    ball_shape.elasticity=0.8 #탄성력
    ball_shape.friction=1.3 #마찰력
    space.add(ball_body,ball_shape) #space라는 매개변수에 ball_body와 ball_shape을 더하라....?????
    return ball_shape #space랑 position 을 넣으면 ball_shape을 뱉어냄: 마술상자라고 생각하기

def create_world(space): #벽 만들기
    rect=[
        [(length/2,height),(length,40)]
        ] #벽의 중심과 크기 결정하기, 리스트 안에 리스트 안에 튜플
    for center,size in rect: 
        rect_body=pymunk.Body(body_type=pymunk.Body.STATIC) #고정시키기
        rect_body.position=center
        rect_shape=pymunk.Poly.create_box(rect_body,size)
        rect_shape.color=(0,100,200,100)
        rect_shape.elasticity=0.5
        rect_shape.friction=1.3
        space.add(rect_body,rect_shape)

#메인 루프
def run(window,length,height): #여기에서의 변수와 위의 변수는 다름
    run = True
    clock=pg.time.Clock()
    fps=60
    delta_time=1/fps #시간 설정하기
    real_space=pymunk.Space()
    real_space.gravity=(50,981) #중력 벡터 설정하기, 1사분면 꺼꾸로라고 생각하기
    real_ball=create_ball(real_space,(length/2,height/2)) #real_space에 공 만들기
    create_wall=create_world(real_space) #real_space에 벽 만들기
   
    draw_options=pymunk.pygame_util.DrawOptions(window)

    while run:
        #종료 조건 확인하기#
        for now_event in pg.event.get(): #pygame안에 event라는 틀이 있다고 생각
            if now_event.type==pg.QUIT: #x표시를 누르면 나가도록 하기
                run=False
                break
            if now_event.type==pg.MOUSEBUTTONDOWN: #마우스가 눌린걸 인식하는 이벤트
                if now_event.button==1:
                    create_ball(real_space,pg.mouse.get_pos())

        draw(real_space,window,draw_options) 
        real_space.step(delta_time) #공간 안에 있는 물건들이 다음순간에 어디있는지 계산하기
        clock.tick(fps)

    pg.quit() #만약에 while문에 오류가 발생해서 while문을 벗어나게 된다면 종료하라는 의미: 좀 더 안정적으로 하기 위함

if __name__=="__main__":
    run(window,length,height) 


