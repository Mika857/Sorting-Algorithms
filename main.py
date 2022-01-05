import SortGui, SortAlgo
from tkinter import *
from tkinter import ttk
import tkinter

algoListLength = 300
algoMaxSize = 400
algo = SortAlgo.Algo(algoListLength, 0, algoMaxSize)

def SortData():    
    #algo.BubbleSort()
    algo.InsertionSort()
    
def newRandomData():
    algo.CreateRandomData(algoListLength, 0, algoMaxSize)
    #SortGui.DrawList(algo.data)   


def keyPress(e):
    #print(f"press: {e.char}")
    if e.char == "r":
        newRandomData()
    elif e.char == "s":
        SortData()
    elif e.char == "t":
        rem = algo.data[0]
        algo.data[0] = algo.data[1]
        algo.data[1] = rem
        SortGui.UpdateList(0, 1, algo.data[0], algo.data[1], len(algo.data))

def keyRelease(e):
    #print(f"release: {e.char}")
    pass

def main():
    SortGui.frame.bind("<KeyPress>", keyPress)
    SortGui.frame.bind("<KeyRelease>", keyRelease)
    SortGui.DrawList(algo.data)



    SortGui.frame.mainloop()

if __name__ == "__main__":
    main()