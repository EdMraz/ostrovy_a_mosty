import tkinter, random
cw = random.randrange(4, 7)
ch = random.randrange(3, 10)
pw = 50
ph = 50
w=400
h=400
count = 0
water = []
islands = []
status = True

root = tkinter.Tk()
canvas = tkinter.Canvas(width=w, height=h)
canvas.pack()
img = tkinter.PhotoImage(file="ostrov3.png")
img1 = tkinter.PhotoImage(file="ostrov0.png")
img2 = tkinter.PhotoImage(file="ostrov1.png")
img3 = tkinter.PhotoImage(file="ostrov2.png")
img4 = tkinter.PhotoImage(file="ostrov_kruh0.png")
img5 = tkinter.PhotoImage(file="ostrov_kruh1.png")

def setup():
    for y in range(ch):
        for x in range(cw):
            result = random.random()
            if result <= 0.2:
                islands.append(canvas.create_image(pw*x, ph*y, anchor="nw", image=img1))
            else:
                water.append(canvas.create_image(pw*x,  ph*y, anchor="nw", image=img))
    canvas.create_image(w-50,2,anchor="nw",image=img4,tags="switcher")

def changer(e):
    global water,count
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if len(zoz) != 0 and zoz[0] in water:
        nx = (e.x // pw)*pw
        ny = (e.y // ph)*ph
        temp = zoz[0]
        canvas.delete(temp)
        water.remove(temp)
        if status == True:
            canvas.create_image(nx, ny, anchor="nw", image=img2, tag="bridge")
            count+=10
        elif status == False:
            canvas.create_image(nx,ny,anchor="nw",image=img1)
            count+=50
    counter()


def spinner(e):
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    print(canvas.itemcget(zoz[0], "image"))
    if canvas.itemcget(zoz[0], "image")=="pyimage3":
        canvas.itemconfig(zoz[0], image=img3)
    else:
        canvas.itemconfig(zoz[0], image=img2)

def switch(e):
    global status
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if status == True:
        canvas.itemconfig(zoz[0],image=img5)
        status = False

    elif status == False:
        canvas.itemconfig(zoz[0],image=img4)
        status = True

def counter():
    global count
    canvas.delete('pocitac')
    canvas.create_text(w-75, 25, text=count,font="Arial 20",tag="pocitac")

canvas.tag_bind("switcher","<Button-1>",switch)
canvas.bind("<Button-1>", changer)
canvas.tag_bind("bridge", "<Button-1>", spinner)
counter()
setup()
root.mainloop()
