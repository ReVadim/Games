from tkinter import *
from PIL import Image, ImageTk

WIDTH = 800
HEIGHT = 800
BODYSIZE = 40
STARTDELAY = 200
LENGHT = 3

count_bodysizeW = WIDTH / BODYSIZE
count_bodysizeH = HEIGHT / BODYSIZE
x = [0] * int(count_bodysizeW)
y = [0] * int(count_bodysizeH)

class Snake(Canvas):

    head_image = False
    head = False
    body = False
    target = False
    delay = 0
    direction = "Right"
    lose = False

    def __init__(self):
        Canvas.__init__(self, width=WIDTH, height=HEIGHT, background="black", highlightthickness=0)
        self.focus_get()
        self.bind_all("<Key>", self.onKeyPressed)
        self.load_resources()
        self.begin_play()
        self.pack()

    def load_resources(self):
        self.head_image = Image.open("images/head.png")
        self.head = ImageTk.PhotoImage(self.head_image.resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.body = ImageTk.PhotoImage(Image.open("images/snake_body.png").resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.target = ImageTk.PhotoImage(Image.open("images/target.png").resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))

    def begin_play(self):
        self.delay = STARTDELAY
        self.direction = "Right"
        self.lose = False
        self.delete(ALL)  # отчистка карты
        self.spawn_actors()  # создание игроков

    def spawn_actors(self):
        x[0] = int(count_bodysizeW / 2) * BODYSIZE
        y[0] = int(count_bodysizeH / 2) * BODYSIZE
        for i in range(1, LENGHT):
            x[i] = x[0] - BODYSIZE * i  # создаём голову
            y[i] = y[0]
        self.create_image(x[0], y[0], image=self.head, anchor="nw", tag="head")
        for i in range(1, LENGHT):
            self.create_image(x[i], y[i], image=self.body, anchor="nw", tag="body")


    def onKeyPressed(self, event):
        pass


root = Tk()
root.title("Змейка")

root.board = Snake()

root.resizable(False, False)


scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()

x = int(scr_width / 2 - WIDTH / 2)
y = int(scr_height / 2 - HEIGHT / 2)

root.geometry("+{0}+{1}".format(x, y))

root.mainloop()