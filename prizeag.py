
import pygame as pg # pg 로 pygame로 표현하겠다. 
import pymunk  # 물리 법칙을 구현하는 친구
import pymunk.pygame_util # . --> 안의  utill 이라는 걸 가져오겠다. 
import math



pg.init() # 함수여서 () 필요 pygame 을 시작한다. 

WIDTH  = 1000
HEIGHT = 800   
# 창을 뜨울 건데 그 크기를 결정
k,b,c,d, = 10,100,15,10


L1, L2, L3, L4 = (k, -100), (k, b), (WIDTH/2 - c, 200), (WIDTH/2 - c , 200+d)
R1, R2, R3, R4 = (WIDTH-k, -100), (WIDTH-k,b), (WIDTH/2 +c, 200), (WIDTH/2 + c, 200+d)

window = pg.display.set_mode((WIDTH,HEIGHT)) # set_mode 인수가 2개 필요합니다. 


def draw(space, window, drawOption) :
    window.fill("white")
    space.debug_draw(drawOption)  
    # 이걸 왜 하는거더라?? 
    pg.display.update()
    # 덮어씌우기 해야함. 


def create_ball(space,position):
    radius = 50
    ball_body = pymunk.Body()
    ball_body.position = position
    ball_shape = pymunk.Circle(ball_body,radius)
    ball_shape.color = (255,0,0,100)  
    # R G B 불투명도 
    ball_shape.mass = 100
    ball_shape.elasticity = 0.7
    # 탄성력
    ball_shape.friction = 40
    # 마찰력

    space.add(ball_body, ball_shape)
    
    return ball_shape


def create_wall(space) : 
    rects = [ 
        # (중심좌표) (가로 세로) 
        [(WIDTH/2,HEIGHT),(WIDTH,50)]
    ]
    for center, size in rects :
        rect_body = pymunk.Body(body_type=pymunk.Body.STATIC)  # pymunk.body. 안에 static이라는 특성이 있는데 이걸 사용하면, 절대 움직이지 않는다. 
        rect_body.position = center   # position 은 좌표로 받는다.
        rect_shape = pymunk.Poly.create_box(rect_body,size)  # pymunk에서 poly는 다각형을 만든다.? 사각형인가? 
        rect_shape.color = (0,0,200,100)
        #rect_shape.mass = 1000
        rect_shape.elasticity = 0.3
        rect_shape.friction = 100
        space.add(rect_body,rect_shape)

def create_segment(space,from_,to_) : 
    segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_shape  = pymunk.Segment(segment_body,from_,to_,3)
    space.add(segment_shape,segment_body)







# main loop 
def comma(window, width, height):
    clock = pg.time.Clock()
    realspace = pymunk.Space()
    realspace.gravity = (10,981 )  # 중력 벡터 설정! 

    drawOption = pymunk.pygame_util.DrawOptions(window)  # 이 창에 구현하겠다! 
    create_segment(realspace,L1,L2)
    create_segment(realspace,L2,L3)
    create_segment(realspace,L3,L4)
    create_segment(realspace,R1,R2)
    create_segment(realspace,R2,R3)
    create_segment(realspace,R3,R4)

    
    fps = 60 
    delta_time = 1/fps
    comma = True
    realBall = create_ball(realspace,(WIDTH/2,HEIGHT/2))
    # create_segment(realspace,(0,0),(100,0))
    create_wall(realspace)
    while comma :
        #for 문은 종료 조건 확인 
        for now_event in pg.event.get():
            if now_event.type == pg.QUIT :
                comma = False
                break
        
        draw(realspace,window,drawOption)
        realspace.step(delta_time)
        
        clock.tick(fps)
        
        
    pg.quit()

        



if __name__ == "__main__" :
    comma(window,WIDTH,HEIGHT)

