from tkinter import *
from tkinter import messagebox
import tkinter.font
import random
import threading

root = Tk()
root.title("108계단")
root.geometry('950x810')
    
frame = Frame(root,width = 950, height = 810)

score = 0
timer1 = 60
start_time = 3
Fspeed = 1
Speed = Fspeed
gamestart = False

#man위치좌표
man_posx = [50, 310, 570,830]
man_posy = 670


#leaf위치좌표
leaf_posx = [5,268,527,785]
leaf_posy = [775, 600, 425, 250, 75]



#중앙 기둥
road = PhotoImage(file = "12.png")
roadlabel1 = Label(frame, image = road)
roadlabel1.place(x = 170, y = 0)
roadlabel2 = Label(frame, image = road)
roadlabel2.place(x = 430, y = 0)
roadlabel3 = Label(frame, image = road)
roadlabel3.place(x = 690, y = 0)


#Arrow img
leftimg = PhotoImage(file = "left.png")
leftlabel = Label(frame, image = leftimg)
leftlabel.place(x = man_posx[0] , y = 0)

rightimg = PhotoImage(file = "right.png")
rightlabel = Label(frame, image = rightimg)
rightlabel.place(x = man_posx[3] , y = 0)

upimg = PhotoImage(file = "up.png")
uplabel = Label(frame, image = upimg)
uplabel.place(x = man_posx[1] , y = 0)

downimg = PhotoImage(file = "down.png")
downlabel = Label(frame, image = downimg)
downlabel.place(x = man_posx[2] , y = 0)

#place man
man = PhotoImage(file = "man.png")
manlabel = Label(frame, image = man)
manlabel.place(x = man_posx[0] , y = man_posy)

temp_leafx = []

#placeleaf()
def place_leaf(leaflabel,ynum):
    global temp_leafx
    xnum = random.randint(0, 3)
    leaflabel.place( x = leaf_posx[xnum] , y = leaf_posy[ynum])

    temp_leafx.append(xnum)

#leafdown()
def leaf_down() :
    global temp_leafx
    global leaflabel
    leaflabel[0].configure(image = leafimg)
    nxnum = random.randint(0, 3)
    temp_leafx = temp_leafx[1:] + [nxnum]
    leaflabel = leaflabel[1:] + [leaflabel[0]]
    leaflabel[4].place(x = leaf_posx[nxnum], y = leaf_posy[4])
    for i in range(0,4) :
        leaflabel[i].place(x = leaf_posx[temp_leafx[i]], y = leaf_posy[i])


#leaf  만들기
leafimg = PhotoImage(file = "leafimg.png")
leafimg0 = PhotoImage(file = "leafimg0.png")
leafimg1 = PhotoImage(file = "leafimg1.png")
leafimg2 = PhotoImage(file = "leafimg2.png")

leaflabel0 = Label(frame, image = leafimg)
leaflabel1 = Label(frame, image = leafimg)
leaflabel2 = Label(frame, image = leafimg)
leaflabel3 = Label(frame, image = leafimg)
leaflabel4 = Label(frame, image = leafimg)
leaflabel = [leaflabel0,leaflabel1,leaflabel2,leaflabel3,leaflabel4]
scorelabel = Label(frame,text = "Score : " + str(score))
scorelabel.place( x = 850, y=0)

for i in range(0,5) :
    place_leaf(leaflabel[i] ,i)
leaflabel[0].place( x = leaf_posx[0] , y = leaf_posy[0])

frame.grid()

