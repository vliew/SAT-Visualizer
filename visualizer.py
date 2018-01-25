from Tkinter import *
import linecache
###########   Parameters   #########################
gridLength = 17  # Sets the size of the squares in grid

rectangular = True
# rectangular strip parameters
numCols = 4
numRows = 8

# multiplier strip parameters
lowCol = 5
highCol = 8

#inputFilename = "visualize_5to8_diag"

if rectangular:
    inputFilename = "visualize_%dby%d_rectangle_" % (numCols,numRows) 
else:
    inputFilename = "visualize_unmod_%dto%d" % (lowCol,highCol)
###################################################

class status:
    PAUSED = 1
    PLAY = 2
    REWIND = 3

lineCount = 0
for line in open(inputFilename):
    lineCount += 1

class App:
    def __init__(self, master):
        self.playspeed = 100
        self.playStatus = status.PAUSED
        self.drawnClause = []
        self.w = Canvas(master, width=400, height=700)
        self.w.pack(side=LEFT)
        self.slider = Scale(master, from_=1, to=lineCount, orient=VERTICAL, length = 650, command= self.updateClause)
        self.slider.pack()

        if not rectangular:
            drawMultiplier(self.w,gridLength,lowCol,highCol)
        else:
            drawRectangular(self.w,gridLength,numRows,numCols)

        frame = Frame(master)
        frame.pack()
        self.play()

        self.next_button = Button(
            frame, text="PREV", fg="blue", command=self.prevClause
            )
        self.next_button.pack(side=LEFT)

        self.play_button = Button(
            frame, text="REWIND", fg="blue", command=self.pressed_rewind
            )
        self.play_button.pack(side=LEFT)
        
        self.play_button = Button(
            frame, text="PLAY", fg="green", command=self.pressed_play
            )
        self.play_button.pack(side=LEFT)

        self.next_button = Button(
            frame, text="NEXT", fg="green", command=self.nextClause
            )
        self.next_button.pack(side=LEFT)
        
        self.pause_button = Button(
            frame, text="PAUSE", fg="grey", command=self.pause
            )
        self.pause_button.pack(side=LEFT)
        
        self.speed1_button = Button(
            frame, text="SPEED 100x", fg="grey", command=self.speed1
            )
        self.speed1_button.pack(side=LEFT)

        self.speed10_button = Button(
            frame, text="SPEED 10x", fg="grey", command=self.speed10
            )
        self.speed10_button.pack(side=LEFT)

        self.speed100_button = Button(
            frame, text="SPEED 1x", fg="grey", command=self.speed100
            )
        self.speed100_button.pack(side=LEFT)

        self.speed600_button = Button(
            frame, text="SPEED 0.2x", fg="grey", command=self.speed600
            )
        self.speed600_button.pack(side=LEFT)

        self.speed1000_button = Button(
            frame, text="SPEED 0.1x", fg="grey", command=self.speed1000
            )
        self.speed1000_button.pack(side=LEFT)
        
    def updateClause(self,clauseIndex):
        for var in self.drawnClause:
            self.w.delete(var)
        self.drawnClause = drawClause(self.w,gridLength,lowCol,highCol,rectangular,clauseIndex)
    
    def nextClause(self):
        self.slider.set(int(self.slider.get())+1)
        
    def prevClause(self):
        self.slider.set(int(self.slider.get())-1)

    def pressed_play(self):
        self.playStatus = status.PLAY

    def pressed_rewind(self):
        self.playStatus = status.REWIND

    def play(self):
        if self.playStatus == status.PLAY:
            root.after(self.playspeed,self.nextClause)
        elif self.playStatus == status.REWIND:
            root.after(self.playspeed, self.prevClause)
        root.after(self.playspeed,self.play)

    def pause(self):
        self.playStatus = status.PAUSED
        
    def speed1(self):
        self.playspeed = 1

    def speed600(self):
        self.playspeed = 600
        
    def speed10(self):
        self.playspeed = 10

    def speed100(self):
        self.playspeed = 100
        
    def speed1000(self):
        self.playspeed = 1000
        
def drawMultiplier(canvas,gridLength,lowCol,highCol):
    # Draw boxes
    for col in range(highCol-lowCol+1):
        for row in range(highCol - col+1):
            canvas.create_rectangle(4*col*gridLength + gridLength, 4*row*gridLength+3*gridLength, 4*col*gridLength+3*gridLength, 4*row*gridLength + 5*gridLength, width=4)

    # Draw vertical carries
    for col in range(highCol-lowCol+1):
        for row in range(highCol - col+1):
            canvas.create_line(4*col*gridLength + (1.7)*gridLength, 4*row*gridLength+5*gridLength, 4*col*gridLength+(1.7)*gridLength, 4*row*gridLength + 7*gridLength,width=3, arrow=LAST)
            canvas.create_line(4*col*gridLength + (2.3)*gridLength, 4*row*gridLength+gridLength, 4*col*gridLength+(2.3)*gridLength, 4*row*gridLength + 3*gridLength, width=3,arrow=FIRST,fill="red")
    # Draw horizontal carries
    for col in range(highCol-lowCol+1):
        for row in range(1,highCol - col-1+1):
            canvas.create_line(4*col*gridLength + 3*gridLength, 4*row*gridLength + 4*gridLength, 4*col*gridLength+5*gridLength, 4*row*gridLength + 4*gridLength, arrow=FIRST,width=3)
            canvas.create_line(4*col*gridLength + 3*gridLength, 4*row*gridLength + 4*gridLength, 4*col*gridLength+5*gridLength, 4*row*gridLength + gridLength, arrow=FIRST,fill="red",width=3)

def drawRectangular(canvas,gridLength,numRows,numCols):
    # Draw boxes
    for col in range(numCols):
        for row in range(numRows):
            canvas.create_rectangle(4*col*gridLength + gridLength, 4*row*gridLength+3*gridLength, 4*col*gridLength+3*gridLength, 4*row*gridLength + 5*gridLength, width=4)

    # Draw vertical carries
    for col in range(numCols):
        for row in range(numRows):
            canvas.create_line(4*col*gridLength + (1.7)*gridLength, 4*row*gridLength+5*gridLength, 4*col*gridLength+(1.7)*gridLength, 4*row*gridLength + 7*gridLength,width=3, arrow=LAST)
            canvas.create_line(4*col*gridLength + (2.3)*gridLength, 4*row*gridLength+gridLength, 4*col*gridLength+(2.3)*gridLength, 4*row*gridLength + 3*gridLength, width=3,arrow=FIRST,fill="red")
    # Draw horizontal carries
    for col in range(numCols):
        for row in range(numRows):
            canvas.create_line(4*col*gridLength + 3*gridLength, 4*row*gridLength + 3.7*gridLength, 4*col*gridLength+5*gridLength, 4*row*gridLength + 3.7*gridLength, arrow=FIRST,width=3)
            canvas.create_line(4*col*gridLength + 3*gridLength, 4*row*gridLength + 4.3*gridLength, 4*col*gridLength+5*gridLength, 4*row*gridLength + 4.3*gridLength, arrow=FIRST,fill="red",width=3)


# draws colored circle at (row,col) position in grid with offset
def drawMark(canvas,row,col,x_offset,y_offset,polarity):
    if polarity:
        color = "green"
    else:
        color = "magenta"
    return canvas.create_oval(4*col*gridLength + x_offset*gridLength, 4*row*gridLength + y_offset*gridLength, 4*col*gridLength+(x_offset+1)*gridLength, 4*row*gridLength + (y_offset+1)*gridLength,fill=color, width=2)

def drawClause(canvas,gridLength,lowCol,highCol,rectangular,clauseIndex):
    line = linecache.getline(inputFilename,int(clauseIndex)).split()
    # first word of line is 'a' if initial clause, 'l' if learned clause
    a_l = line[0]
    literals = line[1:]
    parsedVarInfo = []
    drawnClause = []
    for lit in literals:
        if lit[0] == '-':
            polarity = False
            var = lit[1:]
        else:
            polarity = True
            var = lit
        # varInfo holds the list [variable name, index1, index2]
        varInfo = var.split('_')
        varInfo.append(polarity)
        parsedVarInfo.append(varInfo)

    for varInfo in parsedVarInfo:
        if varInfo[0] == 'o':
            if rectangular:
                col = numCols-1-int(varInfo[1])
                row = numRows
            else:
                col = highCol - int(varInfo[1])
                row = int(varInfo[1])+1
            drawnClause.append(drawMark(canvas,row,col,1.2,2.5,varInfo[2]))
        elif varInfo[0] == 'o1':
            if rectangular:
                col = numCols-1 - int(varInfo[1])
                row = 0
            else:
                col = highCol - int(varInfo[1])
                row = 0
            drawnClause.append(drawMark(canvas,row,col,1.9,0.5,varInfo[2]))

        elif len(varInfo[0]) == 1:
            if rectangular:
                col = numCols-1 - int(varInfo[1])
                row = int(varInfo[2])
            else:
                col = highCol - (int(varInfo[1]) + int(varInfo[2]))
                row = int(varInfo[2])
                
            if varInfo[0] == 't':
                drawnClause.append(drawMark(canvas,row,col,1.5,3.5,varInfo[3]))
            elif varInfo[0] == 'd':
                drawnClause.append(drawMark(canvas,row,col,1.2,5.5,varInfo[3]))
            elif varInfo[0] == 'c':
                drawnClause.append(drawMark(canvas,row,col,-0.5,3.2,varInfo[3]))


        elif len(varInfo[0]) == 2:
            if rectangular:
                col = numCols-1 - int(varInfo[1])
                row = numRows-1 - int(varInfo[2])
            else:
                col = highCol - (int(varInfo[2]) + int(varInfo[1]))
                row = int(varInfo[1])

            if varInfo[0] == 't1':
                drawnClause.append(drawMark(canvas,row,col,1.5,3.5,varInfo[3]))
            elif varInfo[0] == 'd1':
                drawnClause.append(drawMark(canvas,row,col,1.9,1.5,varInfo[3]))
            elif varInfo[0] == 'c1':
                if rectangular:
                    drawnClause.append(drawMark(canvas,row,col,-0.5,4,varInfo[3]))
                else:
                    drawnClause.append(drawMark(canvas,row,col,-0.5,6,varInfo[3]))                 
    return drawnClause
    
    
    
    
root = Tk()
app = App(root)
root.mainloop()
root.destroy()
