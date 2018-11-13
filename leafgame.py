from tkinter import *
from tkinter import messagebox
import tkinter.font
import random
import threading
import os

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
mantimer = 0

#점수 갱신
def update():
    update = open("scoreboard.txt", 'a')
    update.write(str(score) + '\n')
    update.close()

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

#ask continue
def askstart():
    result = messagebox.askyesno("ㅇㅎ","계속할꺼얌?")
    if result == False :
        os._exit(1)
        
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

#man img
ap1 = PhotoImage(file = "ap1.png")
ap2 = PhotoImage(file = "ap2.png")
ap3 = PhotoImage(file = "ap3.png")
ap4 = PhotoImage(file = "ap4.png")

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

#checkpos
def check_pos(i) :
    global gamestart
    global score
    global timer1
    if temp_leafx[0] == i :
        gamestart = True
        score = score+1
        scorelabel.configure(text = "Score : " + str(score))
        timer1 = start_time+1

    else :
        gamestart = False
        leaflabel[0].place(x=11111, y = 11111)
        update()
        messagebox.showinfo("게임 끝","game over\nyour point is "+ str(score))
        askstart()
        score = 0
        scorelabel.configure(text = "Score :" + str(score))
        timer1 = start_time
        leaflabel[0].configure(image = leafimg0)
        
#key input func
def Left_input(event) :
    manlabel.place(x = man_posx[0] , y = man_posy)
    leaf_down()
    check_pos(0)
    gamespeed()
    
def Up_input(event) :
    manlabel.place(x = man_posx[1] , y = man_posy)
    leaf_down()
    check_pos(1)
    gamespeed()
    
def Down_input(event) :
    manlabel.place(x = man_posx[2] , y = man_posy)
    leaf_down()
    check_pos(2)
    gamespeed()
    
def Right_input(event) :
    manlabel.place(x = man_posx[3] , y = man_posy)
    leaf_down()
    check_pos(3)
    gamespeed()
    
#time_function
def time_over() :
    global timer1
    global score
    global gamestart
    timer1 = start_time
    scorelabel.configure(text = "Score : " + str(score))
    gamestart = False
    leaflabel[0].configure(image = leafimg0)
    update()
    messagebox.showinfo("게임 끝","time over\nyour point is "+ str(score))
    askstart()
    score = 0

def leaf_time_img(i) :
    if i == 2 :
        leaflabel[0].configure(image = leafimg2)
    elif i == 1 :
        leaflabel[0].configure(image = leafimg1)
    elif i == 0 :
        leaflabel[0].configure(image = leafimg0)
    else :
        leaflabel[0].configure(image = leafimg)

def check_manimg(t) :
    if t==0 :
        manlabel.configure(image = ap1)
    elif t==1 :
        manlabel.configure(image = ap2)
    elif t==2 :
        manlabel.configure(image = ap3)                           
    else :
        manlabel.configure(image = ap4)
    
        
def timerleaf() :
    global timer1
    global Speed
    global mantimer
    timer1 -= 1
    mantimer += 1
    if mantimer > 3:
        mantimer = 0
    check_manimg(mantimer)
    
    leaf_time_img(timer1)
    if gamestart == False :
        timer1 = start_time
        leaflabel[0].configure(image = leafimg0)     
    timer = threading.Timer(Speed,timerleaf)
    timer.start()
    if timer1 < 1 :
        time_over()
timerleaf()
#game speed()
font= tkinter.font.Font(family="맑은 고딕", size=30, slant="italic")
Speeduplabel = Label(frame,text = "Speed up!",font = font)

def gamespeed() :
    global Speed
    if gamestart == True :
        if score%10 == 0 :
            Speed = Speed / 1.1
            Speeduplabel.place(x= 400, y= 0 )
        else :
            Speeduplabel.place(x= 111111, y= 0 )
    if score == 1 :
        Speed = Fspeed
        
        
root.bind('<Left>',Left_input)
root.bind('<Right>',Right_input)
root.bind('<Up>',Up_input)
root.bind('<Down>',Down_input)


for i in range(0,5) :
    place_leaf(leaflabel[i] ,i)
leaflabel[0].place( x = leaf_posx[0] , y = leaf_posy[0])

frame.grid()

root.mainloop()
