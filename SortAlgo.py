import random, time, SortGui

class Algo(object):

    data = list()

    #Merge Sort -> split the array until there are only two left -> sort them and then add together
    def MergeSort(self):
        #first split up the array
        data = self.data
        n = len(data)

        

    #Insertion Sort
    def InsertionSort(self):
        SortGui.lastSelRec = 0
        data = self.data
        n = len(data)

        for i in range(1, n):
            #check if element is smaller than predecessor
            if data[i] < data[i-1]:
                for j in range(i):
                    if data[i-j-1] <= data[i-j]:
                        break

                    rem = data[i-j-1]
                    data[i-j-1] = data[i-j]
                    data[i-j] = rem

                    SortGui.UpdateList(i-j, i-j-1, data[i-j], data[i-j-1], len(data)) 
                    SortGui.PaintCurrentRec(i-j)
                    SortGui.frame.update()
                    #time.sleep(.1)

        # print data
        for val in data:
            print(val)

                   



    #Bubble Sort
    def BubbleSort(self):
        #always check in pairs of two and switch if needed -> if nothing changed -> sorting is finnished
        data = self.data
        n = len(data)

        

        for i in range(n):
            swapped = False

            for j in range(0, n - i - 1):
                if data[j] > data[j+1]:
                    #switch j and j+1
                    rem = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = rem

                    swapped = True

                    #-- this is fuked up -- takes ages and does not work properly??? whyy??
                    SortGui.UpdateList(j, j+1, data[j], data[j+1], len(data)) 
                    SortGui.PaintCurrentRec(j)
                    SortGui.frame.update()
                    #time.sleep(0.1)

                    
            if not swapped:
                print("done")
                SortGui.DrawList(data)
                break
            

    def CreateRandomData(self, listLength, rangeStart, rangeStop):
        self.data.clear()
        for i in range(0,listLength):
            self.data.append(random.randrange(rangeStart,rangeStop))

        SortGui.DrawList(self.data)

    def PrintData(self):
        for i, data in enumerate(self.data):
            print(f"{i, data = }")

    def __init__(self, listLength, rangeStart, rangeStop) -> None:
        self.CreateRandomData(listLength, rangeStart, rangeStop)

