# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

olddoorheight = 66
olddoorwidth = 30
oldframethickness = 0.375
oldshims = .75
roughheight = 80.5
roughwidth = 32.0
framethickness = 0.75
gap = 0.125



def getNewDoorStats:
    #calculate door width
    doorwidth = roughwidth - (framethickness * 2) - (gap * 2) - oldshims
    #calculate door height
    doorheight = roughheight - framethickness - gap - 1
    print("Door width is "+str(doorwidth)+", "+"Door height is "+str(doorheight))

#calculate door frame requirements
def getHewFrameStats:
    topjambpiece = roughwidth    
    sidejambpiece = roughheight - framethickness
    totaljamblength = topjambpiece + (sidejambpiece * 2)

print("total length of board required for jamb is "+ str(totaljamblength)+", or "+str(totaljamblength/12)+" feet" )