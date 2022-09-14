from cmath import log10
import math
WIDTH = 1000
d = 30
root3 = math.sqrt(3)

Length = 27 #side length of hexagon
c = 17
x = Length +2*c/root3

Bdistance = x * root3/2
Bheight = x /2

def makeLpoint1(point) :
    NewPoint = [0,0]
    NewPoint[0] = point[0]-Bdistance
    NewPoint[1] = point[1]+Bheight
    return NewPoint

def makeLpoint2(point) :
    NewPoint = [0,0]
    NewPoint[0] = point[0]
    NewPoint[1] = point[1]+x
    return NewPoint

def makeRpoint1(point) :
    NewPoint = [0,0]
    NewPoint[0] = point[0]+Bdistance
    NewPoint[1] = point[1]+Bheight
    return NewPoint

def makeRpoint2(point) :
    NewPoint = [0,0]
    NewPoint[0] = point[0]
    NewPoint[1] = point[1]+x
    return NewPoint

L4 = (WIDTH/2 - c , 200+d)  # position3 
L5 = makeLpoint1(L4)
L6 = makeLpoint2(L5)
L7 = makeLpoint1(L6)
L8 = makeLpoint2(L7)
L9 = makeLpoint1(L8)
L10= makeLpoint2(L9)
L11= makeLpoint1(L10)
L12= makeLpoint2(L11)
L13= makeLpoint1(L12)
L14= makeLpoint2(L13)
L15= makeLpoint1(L14)
L16= makeLpoint2(L15)
L17= makeLpoint1(L16)
L18= makeLpoint2(L17)


R4 = (WIDTH/2 + c , 200+d)  # position3 
R5 = makeRpoint1(R4)
R6 = makeRpoint2(R5)
R7 = makeRpoint1(R6)
R8 = makeRpoint2(R7)
R9 = makeRpoint1(R8)
R10= makeRpoint2(R9)
R11= makeRpoint1(R10)
R12= makeRpoint2(R11)
R13= makeRpoint1(R12)
R14= makeRpoint2(R13)
R15= makeRpoint1(R14)
R16= makeRpoint2(R15)
R17= makeRpoint1(R16)
R18= makeRpoint2(R17)

LEFTLINE = [L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18]
RIGHTLINE = [R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18]


geori =30   #거리... 변수명 음차 실화냐
FFH = 200+d+geori #first floor height
pushvalue = root3/2*Length
floorheight = Length/2

h= root3*Length/2+c
i= 3*Length/2+root3*c

P0 = -1 #error number
P1 = (WIDTH/2 ,FFH)
P2= (WIDTH/2-h,FFH + i)
P3= (WIDTH/2+h,FFH + i)

P4= (WIDTH/2-2*h,FFH + 2*i)
P5= (WIDTH/2,FFH + 2*i)
P6= (WIDTH/2+2*h,FFH + 2*i)

P7= (WIDTH/2-3*h,FFH + 3*i)
P8= (WIDTH/2-h,FFH + 3*i)
P9= (WIDTH/2+h,FFH + 3*i)
P10= (WIDTH/2+3*h,FFH + 3*i)
P11 = (WIDTH/2-4*h ,FFH+4*i)
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


P = [P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10,P11, P12, P13, P14, P15, P16, P17, P18, P19, P20 ,P21, P22, P23, P24, P25, P26, P27, P28]
