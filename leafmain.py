from tkinter import *
from tkinter import messagebox
import tkinter.font
import random
import threading
import subprocess

def gamestart():
  subprocess.call("leafgame.py", shell=True)
  getrank()
  scorelabel.config(text = rankstr)
    
window=Tk()
window.title("조선대학교 108계단 오르기")
window.geometry("440x810")

label1=Label(window, text="조선대학교 108계단 오르기", font="Time 10")
label1.place(x=138, y=50)

label2=Label(window, text="최고점수")
label2.place(x=195, y=300)

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
scorelabel =Label(window, text=rankstr)
scorelabel.place(x=210,y=320)

btn1=Button(window,text="게임시작", command = gamestart)
btn1.place(x=380, y=783)

window.mainloop()
