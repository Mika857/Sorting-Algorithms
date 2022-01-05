from tkinter import *
from tkinter import ttk
import tkinter
 
frame = Tk()
frame.title("Sort Algorithm")
frame.geometry("600x600")
frame.resizable(False,False)
frame.configure(bg="#264653")

rects = []

canvas = Canvas(frame,width=600,height=600,bg="#264653")
canvas.config(bd=0,highlightthickness=0)
canvas.grid(row=0, column=0)


lastSelRec = 0

def DrawList(list):
    rects.clear()
    canvas.delete("all")
    widthData = 600/len(list)
    for x,element in enumerate(list):
        rects.append(canvas.create_rectangle(x*widthData,600,x*widthData+widthData,600-element,fill="black"))
    

def UpdateList(start, end, startValue, endValue, listLength):
    widthData = 600/listLength

    recStart = rects[start]
    recEnd = rects[end]

    heightStart = startValue
    heightEnd = endValue
    canvas.coords(recStart, start*widthData, 600, start*widthData+widthData, 600-heightStart)
    canvas.coords(recEnd, end*widthData, 600, end*widthData+widthData, 600-heightEnd)
    # canvas.itemconfig(recStart, fill="green")
    # canvas.itemconfig(recEnd, fill="black")

def PaintCurrentRec(currRec):
    global lastSelRec
    print(lastSelRec)

    cur = rects[currRec]
    last = rects[lastSelRec]

    canvas.itemconfig(last, fill="black")
    canvas.itemconfig(cur, fill="green")

    lastSelRec = currRec



#a class is not good here -> only one frame is needed -> static class -> class is not needed

# class SortGui(object):

#     def DrawList(self, list, listLength):
#         self.canvas.delete("all")
#         widthData = 600/listLength
#         for x,element in enumerate(list):
#             rect = self.canvas.create_rectangle(x*widthData,600,x*widthData+widthData,600-element,fill="black")

    # def __init__(self) -> None:
    #     self.frame = Tk()
    #     self.frame.title("Sort Algorithm")
    #     self.frame.geometry("600x600")
    #     self.frame.resizable(False,False)
    #     self.frame.configure(bg="#264653")
        

    #     self.canvas = Canvas(self.frame,width=600,height=600,bg="#264653")
    #     self.canvas.config(bd=0,highlightthickness=0)
    #     self.canvas.grid(row=0, column=0)
        #self.testRec = self.canvas.create_rectangle(0,0,30,30, fill="black")
            

    