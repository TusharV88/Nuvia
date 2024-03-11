from itertools import cycle
from random import randrange
from tkinter import Tk , Canvas , messagebox , font

def main_eggame():
    global score, egg_speed, egg_interval, lives_remaning
    canvas_width = 800
    canvas_height = 400

    win = Tk()
    win.minsize(canvas_width, canvas_height)
    win.maxsize(canvas_width, canvas_height)
    win.title('Egg Catcher Game')
    c = Canvas(win , width = canvas_width ,  height = canvas_height , background = '#2979FF')
    c.create_rectangle(-5, canvas_height - 100 , canvas_width + 5 , canvas_height + 5 , fill='#76FF03', width=2)
    c.create_oval(-80,-80,120,120,fill='#FFFF00' , width=2)
    c.pack()

    color_cycle = cycle(['#00B0FF' , '#F50057' , '#FFEA00','#00E676' , 'red', '#3D5AFE' , '#1DE9B6','#6D4C41'])
    egg_width = 45
    egg_height = 55
    egg_score = 10
    egg_speed = 500
    egg_interval = 4000
    difficulty_factor = 0.95

    catcher_color = '#AA00FF'
    catcher_width = 100
    catcher_height = 100
    catcher_start_x = canvas_width / 2 - catcher_width / 2
    catcher_start_y = canvas_height -catcher_height - 20
    catcher_start_x2 = catcher_start_x + catcher_width
    catcher_start_y2 = catcher_start_y + catcher_height

    catcher = c.create_arc(catcher_start_x ,catcher_start_y ,catcher_start_x2,catcher_start_y2 , start=200 , extent = 140 , style='arc' , outline=catcher_color , width=5)

    text_bg = c.create_text(400, 30, text="Egg Catcher", font=("Helvetica", 40), fill='black')
    text_fg = c.create_text(408, 30, text="Egg Catcher", font=("Helvetica", 40), fill='#C6FF00')


    score = 0
    score_text = c.create_text(canvas_width-10,10,anchor='ne' , font=('Arial',18,'bold'),fill='#FF8F00',text='Score : ' + str(score))

    lives_remaning = 3
    lives_text = c.create_text(canvas_width-10,50,anchor='ne' , font=('Arial',18,'bold'),fill='#FF8F00',text='Lives : ' + str(lives_remaning))

    eggs = []

    def create_eggs():
        x = randrange(10,740)
        y = 40
        new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=2)
        eggs.append(new_egg)
        win.after(egg_interval,create_eggs)

    def move_eggs():
        for egg in eggs:
            (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
            c.move(egg,0,10)
            if egg_y2 > canvas_height:
                egg_dropped(egg)
        win.after(egg_speed,move_eggs)

    def egg_dropped(egg):
        eggs.remove(egg)
        c.delete(egg)
        lose_a_life()
        if lives_remaning == 0:
            messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score))
            win.destroy()

    def lose_a_life():
        global lives_remaning
        lives_remaning -= 1
        c.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))

    def catch_check():
        (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher)
        for egg in eggs:
            (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
            if catcher_x < egg_x and egg_x2  < catcher_x2 and catcher_y2 - egg_y2 < 40:
                eggs.remove(egg)
                c.delete(egg)
                increase_score(egg_score)
        win.after(100,catch_check)

    def increase_score(points):
        global score , egg_speed , egg_interval
        score += points
        egg_speed = int(egg_speed * difficulty_factor)
        egg_interval = int(egg_interval * difficulty_factor)
        c.itemconfigure(score_text , text='Score : ' + str(score))

    def move_left(event):
        (x1,y1,x2,y2) = c.coords(catcher)
        if x1 > 0:
            c.move(catcher,-20,0)

    def move_right(event):
        (x1,y1,x2,y2) = c.coords(catcher)
        if x2 < canvas_width:
            c.move(catcher,20,0)

    c.bind('<Left>' , move_left)
    c.bind('<Right>' , move_right)
    c.focus_set()

    win.after(1000,create_eggs)
    win.after(1000,move_eggs)
    win.after(1000,catch_check)

    win.mainloop()

if __name__ == '__main__':
    main_eggame()
