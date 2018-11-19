from tkinter import *
from tkinter import messagebox
import tkinter.font
import random
import threading
import subprocess
import pyglet

def Mic(music1):
  BGM1 = pyglet.resource.media(music1)
  BGM1.play()
  pyglet.app.run()
  
Mic('BGM.mp3')

def gamestart():
  subprocess.call("leafgame.py", shell=True)
  getrank()
  scorelabel.config(text = rankstr)
    
window=Tk()
window.title("조선대학교 108계단 오르기")
window.geometry("340x340")
window.resizable(width = FALSE, height = FALSE)

background_image = PhotoImage(file = "background.png")
background_label = Label(window, image = background_image)
background_label.place(x = 0, y = 0)

label1=Label(window, text="조선대학교 108계단 오르기", bg = 'light blue')
label1.place(x=88, y=40)

label2=Label(window, text="최고점수", bg = 'light gray')
label2.place(x=145, y=90)

rankstr = ''
def getrank():
  global rankstr
  rankstr = ''
  score = open('scoreboard.txt','r')
  rank = score.readlines()
  score.close()
  rank = [int(i) for i in rank]
  rank.sort()
  rank.reverse()
  count = 0
  for i in rank :
    rankstr = rankstr+str(i) + "\n"
    count += 1
    if count >= 10 :
      break
      
getrank()   
scorelabel =Label(window, text=rankstr, bg = 'light gray')
scorelabel.place(x=155,y=110)

btn1=Button(window,text="게임시작", command = gamestart)
btn1.place(x=280, y=310)

window.mainloop()
