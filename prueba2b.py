
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1000, height=400)
canvas.pack()
x=0
y=100
my_image = PhotoImage (file="captura.png")
canvas.create_image(0,100,anchor=NW, image=my_image)
my_image1 = PhotoImage (file="arco.png")
canvas.create_image(700,30,anchor=NW, image=my_image1)

def balon(event):
    global x
    global y
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
        y=y-3
        print(y)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
        y=y+3
        print(y)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
        x=x-3
        print(x)
    else:
        canvas.move(1, 3, 0)
        x=x+3
        print(x)
        
canvas.bind_all('<KeyPress-Up>', balon)
canvas.bind_all('<KeyPress-Down>', balon)
canvas.bind_all('<KeyPress-Left>', balon)
canvas.bind_all('<KeyPress-Right>', balon)

tk.mainloop()
