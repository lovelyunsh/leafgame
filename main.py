from tkinter import *
from tkinter import messagebox
import tkinter.font
import random
import threading
import subprocess

def gamestart():
  subprocess.call("leafgame.py", shell=True)
  getrank()
    
window=Tk()
window.title("조선대학교 108계단 오르기")
window.geometry("440x810")

label1=Label(window, text="조선대학교 108계단 오르기", font="Time 10")
label1.place(x=138, y=50)

label2=Label(window, text="최고점수")
label2.place(x=195, y=300)

def getrank():
  score = open('scoreboard.txt','r')
  rank = score.readlines()
  score.close()
  rank = [int(i) for i in rank]
  rank.sort()
  rank.reverse()
  rank = [(str(i) + '\n') for i in rank]
  scorelabel =Label(window, text=rank)
  scorelabel.place(x=210,y=320)
  
getrank()

btn1=Button(window,text="게임시작")
btn1.place(x=380, y=783, command = gamestart)

window.mainloop()
