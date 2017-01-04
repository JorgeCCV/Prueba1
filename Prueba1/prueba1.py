###PROGRAMACION AVANZADA
###Nombre: Jorge Campoverde

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=250,bg="green")

canvas.pack()
tk.title("Futbolito")

x=0
y=50
balon=PhotoImage(file="balon.gif")
canvas.create_image(x,y,anchor=NW,image=balon)

arco=PhotoImage(file="porter.gif")
canvas.create_image(350,40,anchor=NW,image=arco)

def moverbalon(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
        print(x,y)

canvas.bind_all('<KeyPress-Up>', moverbalon)
canvas.bind_all('<KeyPress-Down>',moverbalon)
canvas.bind_all('<KeyPress-Left>', moverbalon)
canvas.bind_all('<KeyPress-Right>', moverbalon)

etiqueta=Label(tk,text="COORDENADAS")
etiqueta.pack()
var1 = StringVar()
var2 = StringVar()

label = Label( tk, textvariable=var1 )
var1.set(x)
label2 = Label( tk, textvariable=var2 )
var2.set(y)
label.pack()
label2.pack()

if x==350 and y==40:
    grito = StringVar()
    label = Label( tk, textvariable=grito )
    var.set("GOOOOLLLLL")
    label.pack()

tk.mainloop()
