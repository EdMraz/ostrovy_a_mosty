import tkinter, random
cw = random.randrange(4, 7)
ch = random.randrange(3, 10)
pw = 50
ph = 50
water = []
islands = []

root = tkinter.Tk()
canvas = tkinter.Canvas(width=300, height=400)
canvas.pack()
img = tkinter.PhotoImage(file="ostrov3.png")
img1 = tkinter.PhotoImage(file="ostrov0.png")
img2 = tkinter.PhotoImage(file="ostrov1.png")
img3 = tkinter.PhotoImage(file="ostrov2.png")


def setup():
    for y in range(ch):
        for x in range(cw):
            result = random.random()
            if result <= 0.2:
                islands.append(canvas.create_image(pw*x, ph*y, anchor="nw", image=img1))
            else:
                water.append(canvas.create_image(pw*x,  ph*y, anchor="nw", image=img))


def changer(e):
    global water
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if len(zoz) != 0 and zoz[0] in water:
        nx = (e.x // pw)*pw
        ny = (e.y // ph)*ph
        temp = zoz[0]
        canvas.delete(temp)
        water.remove(temp)
        canvas.create_image(nx, ny, anchor="nw", image=img2, tag="bridge")


def spinner(e):
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    print(canvas.itemcget(zoz[0], "image"))
    canvas.itemconfig(zoz[0], image=img3)


canvas.bind("<Button-1>", changer)
canvas.tag_bind("bridge", "<Button-1>", spinner)
setup()
root.mainloop()
