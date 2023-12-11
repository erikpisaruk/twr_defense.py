#Tower Defense
#Time
#Kevin Munder
'''
3 hr = 11/16
1 hr = 11/27
1 hr = 12/4
1 hr = 12/6
1 hr = 12/8
3 hr = 12/12
'''
#Erik Pisaruk
'''
3 hr = 11/16
1 hr = 11/27
1 hr = 12/4
1 hr = 12/6
1 hr = 12/8
3 hr = 12/12
'''
# Erik and Kev
from tkinter import *
root = Tk()
root.configure(bg='white')
root.title('Tower Defense')
import random as rand

#Window - Erik and Kev
canvas = Canvas(root, width=900, height=700)
canvas.pack()

top_frame = Frame(root, bg = 'blue', width = 900, height = 100) 
top_frame.place(x=0,y=0) 

left_frame = Frame(root, bg = 'grey', width = 200, height = 600)
left_frame.place(x=0,y=100)

# - Kev
path = canvas.create_polygon(200,290,440,290,440,440,950,440,950,540,340,540,340,390,200,390,fill="#"+("%06x"%rand.randint(0,16777215)))
print('Please place a tower outside of the path.')

#-tower placement limit - Erik
twr_used = 3
bullet = 0
bullet1 = 0
bullet2 = 0
x10 = 0
y10 = 0
x11 = 0
y11 = 0
#Enemies - Kev
enemies = []
num_enemies = 1
k = 50
for i in range (num_enemies):
    enemy = canvas.create_oval(150-k,325,175-k,350,fill='red')
    k +=50
    enemy_health = 10
    enemies.append(enemy)

#Functions - Kev and Erik
#def quit
def stop():
    root.destroy()
quit_window = Button(root,text="Stop", command=stop)
quit_window.place(x=50,y=400)
#def place_twr():
def fx():
    def place_twr (event):
        global twr_used
        global bullet
        global bullet1
        global bullet2
        global twr_loc
        global twr_loc1
        global twr_loc2
        global x10
        global y10
        global x11
        global y11
        if twr_used == 3:
            twr1 = canvas.create_rectangle(event.x,event.y,(event.x + 100),(event.y + 100), fill="#"+("%06x"%rand.randint(0,16777215)))
            x10,y10,x11,y11 = canvas.coords(twr1)
            print(x10,y10,x11,y11)
            twr_used -= 1
            bullet = canvas.create_rectangle ((x10+48),(y10+48),(x11-48),(y11-48), fill= 'black')
        '''elif twr_used == 2:
            twr2 = canvas.create_rectangle(event.x,event.y,(event.x + 100),(event.y + 100), fill="#"+("%06x"%rand.randint(0,16777215)))
            x4,y4,x5,y5 = canvas.coords(twr2)
            twr_used -= 1
            bullet1 = canvas.create_rectangle ((x4+48),(y4+48),(x5-48),(y5-48), fill = 'black')
        elif twr_used == 1:
            twr3 = canvas.create_rectangle(event.x,event.y,(event.x + 100),(event.y + 100), fill="#"+("%06x"%rand.randint(0,16777215)))
            x6,y6,x7,y7 = canvas.coords(twr3)
            twr_used -= 1
            bullet2 = canvas.create_rectangle ((x6+48),(y6+48),(x7-48),(y7-48), fill = 'black')
        elif twr_used == 0:
            print("Too many towers! or Not enought money!")'''
        print("Towers left = " + str(twr_used))   
    canvas.bind('<Button-1>',place_twr)
    canvas.focus_set()
    canvas.pack
twr_select = Button(root, text='Tower 1', command= fx)
twr_select.place(x=50,y=200)
#def begin ():
def begin(): # Erik
    global enemy_health
    global enemy
    global enemy_alive
    global bullet
    global bullet1
    global bullet2
    global bullet_alive
    global bullet1_alive
    global bullet2_alive
    x0,y0,x1,y1 = canvas.coords(enemy)
    x2,y2,x3,y3 = canvas.coords(bullet)
    '''x4,y4,x5,y5 = canvas.coords(bullet1)
    x6,y6,x7,y7 = canvas.coords(bullet2)'''
    # Kev and Erik
    if x1<400:
        canvas.move(enemy,1,0)
    if x1==400:
        canvas.move(enemy,0,1)
    if y1>=500:
        canvas.move(enemy,1,0)
    if x1>=900:
            print("end game")
    a = ((x0-x2)//50)
    b = ((y1-y3)//50)
    '''c = ((x0-x4)//50)
    d = ((y1-y5)//50)
    e = ((x0-x6)//50)
    f = ((y1-y7)//50)'''
    
    canvas.move(bullet,a,b)
    '''canvas.move(bullet1,c,d)
    canvas.move(bullet2,e,f)'''
    
    #after getting close, move to the enemy
    if a ==-1:
        canvas.move(bullet,1,1)
    if b ==-1:
        canvas.move(bullet,1,1)
    '''if c ==-1:
        canvas.move(bullet1,1,1)
    if d ==-1:
        canvas.move(bullet1,1,1)
    if e ==-1:
        canvas.move(bullet2,1,1)
    if f ==-1:
        canvas.move(bullet2,1,1)'''
    
    root.after(10,begin)
    
    if (x1==x2):
        print('hit')
        enemy_health -= 5
        canvas.moveto(bullet,x10,y11)
        if enemy_health <= 0:
            print('Enemy killed!')
            with open('stat.txt','w') as f:
                f.write('Enemy killed!')
    '''if (x1==x4):
        print('hit')
        enemy_health -= 5
        canvas.moveto(bullet1,100,100)
        if enemy_health <= 0:
            print('enemy killed')
            enemy_alive = False
    if (x1==x6):
        print('hit')
        enemy_health -= 5
        canvas.moveto(bullet2,100,100)
        if enemy_health <= 0:
            print('enemy killed')
            enemy_alive = False'''
# Kev and Erik
start = Button(root, text='Start Wave', command=begin)
start.place(x=50,y=300)

root.mainloop()
