from cmath import log10
import math
WIDTH = 1000
d = 30
a = math.sqrt(3)

Length = 35
c = 17
x = Length +2*c/a

Bdistance = x * a/2
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
