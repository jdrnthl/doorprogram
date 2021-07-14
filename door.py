# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a door program.
"""
roughwidthtop = 31 + (1/2)
roughwidthmiddle = 32 + (1/8)
roughwidthbottom = 31 + (7/8)
roughwidth = min(roughwidthtop,roughwidthmiddle,roughwidthbottom)

roughheightleft = 80 + (1/4)
roughheightmiddle = 80.0
roughheightright = 80 + (1/4) 
roughheight = max(roughheightleft,roughheightmiddle, roughheightright) 


roughdepthtopleft = 8 + (1/4)
roughdepthtopmiddle = 8 + (3/8)
roughdepthtopright = 8 + (5/16)
roughdepth = min(roughdepthtopleft,roughdepthtopmiddle,roughdepthtopright)

gap = 0.125

newframethickness = 0.75
newframedepth = roughdepth
newframelengthtop = roughwidth - (gap * 2)
newframelengthsides = roughheight - newframethickness

oldframethickness = 3/8
oldframedepth = 8 + (5/8)
oldframelengthtop = 30 + (3/16)
oldframelengthsides = 0.0

gap = 0.125

olddoorwidth = 29 + (7/8)
olddoorheight = 77 + (15/16)

newdoorwidth = 0.0
newdoorheight = 0.0


totallengthneeded = (newframelengthsides * 2) + newframelengthtop

print("The top piece will need to be "+str(newframelengthtop)+" inches, and each side piece will need to be "+str(newframelengthsides)+" inches")
print("You'll need to cut a total of "+str(totallengthneeded)+" inches of wood.")
print("The widht of these boards will need to be "+str(newframedepth))
boardlength = 8*12
boards = 2
totalboardlength = boardlength * boards
leftoverboard = 17 + (3/8)

print("Each board will have " + str(leftoverboard) + " inches left after being cut into a side piece")
print("It will take "+str(newframelengthtop/leftoverboard)+" to make the top piece")      

    
def getNewDoorStats():
    # calculate door width
    newdoorwidth = roughwidth - (newframethickness * 2) - (gap * 2)
    #calculate door height
    newdoorheight = roughheight - newframethickness - gap - 1
    print("Door width is "+str(newdoorwidth)+", "+"Door height is "+str(newdoorheight))
    print("You'll have to lessen the width of the existing door by "+str(olddoorwidth - newdoorwidth)+" and the height by "+str(olddoorheight-newdoorheight))


    



