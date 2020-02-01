#!/usr/bin/python3

# game : 'pong'.
# player who loses 10 points first, loses the game.

# left paddle controls :
''' a : up
    d : down
'''
# right paddle controls :
''' up arrow key : up
    down arrow key : down
'''

# it is kind of an extension to the  game : 'bounce'.
# i've resued much of bounce game's code here.



from tkinter import *
import random
import time

# global variables :
counter = 0
counter1 = 0


# main window objects :
tk = Tk()
tk.title("Pong!")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width = 500, height = 400, bd = 0 ,highlightthickness = 0)
canvas.config(bg = "black")
canvas.pack()

tk.update()



# line-of-separation between the two players.
canvas.create_line(250,0,250,400,fill = "white")







# required   C L A S S E S : 
# the ball :
class Ball:
    def __init__(self,canvas,color,paddle,paddle1):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle1 = paddle1

        self.id = canvas.create_oval(10,10,25,25, fill=color)
        
        self.canvas.move(self.id, 235,200)
        
        starts = [-3,3]
        random.shuffle(starts)
        
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = 500
    


    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
               return True
            return False



    def hit_paddle1(self,pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False



    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        
        #value of 'counter' incremented if right boundary is touched.  (in favor of Player 1 (left))
        if pos[0] <= 0:
            self.x = 3
            self.score(True)

        # value of 'counter1' incremented if left boundary touched.    (in favor of Player 2 (right))
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(False)

        if self.hit_paddle(pos) == True:
            self.x = 3
        if self.hit_paddle1(pos) == True:
            self.x = -3


    
    # keeping the S C O R E :
    def score(self, val):
        global counter
        global counter1
        
        if val == True:
            # to hide previous count
            a = self.canvas.create_text(125,40, text = counter, font =("Arial", 60), fill = "white")
            canvas.itemconfig(a,fill = "black")
            counter += 1
            # to display new count
            a = self.canvas.create_text(125,40, text = counter, font =("Arial", 60), fill = "white")
        

        if val == False:
            # to hide previous count
            a = self.canvas.create_text(375,40, text = counter1, font= ("Arial", 60), fill = "white")
            canvas.itemconfig(a,fill = "black")
            counter1 += 1
            # to display new count
            a = self.canvas.create_text(375,40, text = counter1, font= ("Arial", 60), fill = "white")






# the  L E F T  P A D D L E :
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,150,30,250, fill = color)
        self.y = 0
        
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
        self.canvas.bind_all('a', self.turn_left)
        self.canvas.bind_all('d', self.turn_right)
    
  
  
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    
    
    def turn_left(self,evt):
        self.y = -3

    
    def turn_right(self,evt):
        self.y = 3









# the  R I G H T  P A D D L E :
class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(470,150,500,250, fill = color)
        self.y = 0

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
        self.canvas.bind_all('<KeyPress-Down>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_right)
    
    
    
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0



    def turn_left(self,evt):
        self.y = 3
    
    
    def turn_right(self,evt):
        self.y = -3
















# the required   O B J E C T S :
paddle = Paddle(canvas, "blue")

paddle1 = Paddle1(canvas, "pink")

ball = Ball(canvas, "orange", paddle, paddle1)  
# the paddles should, obviously, come before ball as it takes the left paddle(paddle) and the right paddle(paddle1) object as parameter.
















# to  E X E C U T E  : 
while (1):
    ball.draw()
    paddle.draw()
    paddle1.draw()
    

    if counter == 5 :
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(250,200, text = "Player 1 Wins !", font = 32, fill = "red")
        canvas.create_text(250,215, text = "Score :" + str(counter) + " - " + str(counter1), font = 32, fill = "white")

    if counter1 == 5 :
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(250,200, text = "Player 2 Wins!", font = 32, fill = "red")
        canvas.create_text(250,215, text = "Score : " + str(counter1) + " - " + str(counter), font = 32, fill = "white")


    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


    if counter == 5 or counter1 == 5 :
        # the halts to show the result for 10 seconds.
        # keeping a very high sleeping time here is here is okay but :
            # 1 : after that sleeping time is complete, the game will continue (beyond end point).
            # 2 : the window object is not destroyed.
        # so, instead, do this :  
        time.sleep(10)

        # after 10 secs,the tkinter window object is destroyed automatically (otherwise the game would go on indefinitely.)
        tk.destroy()
        

