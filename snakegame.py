import random
from tkinter import *
from PIL import Image, ImageTk

WIDTH = 800
HEIGHT = 800
BODYSIZE = 40
STARTDELAY = 500
LENGTH = 3

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
    direction_temp = "Right"
    lose = False

    def __init__(self):
        Canvas.__init__(self, width=WIDTH, height=HEIGHT, background="black", highlightthickness=0)
        self.focus_get()
        self.bind_all("<Key>", self.on_key_pressed)
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
        self.after(self.delay, self.timer)  # создание анимации

    def spawn_actors(self):
        self.spawn_apple()
        x[0] = int(count_bodysizeW / 2) * BODYSIZE
        y[0] = int(count_bodysizeH / 2) * BODYSIZE
        for i in range(1, LENGTH):
            x[i] = x[0] - BODYSIZE * i  # создаём голову
            y[i] = y[0]
        self.create_image(x[0], y[0], image=self.head, anchor="nw", tag="head")
        for i in range(LENGTH - 1, 0, -1):
            self.create_image(x[i], y[i], image=self.body, anchor="nw", tag="body")

    def spawn_apple(self):
        target = self.find_withtag("target")
        if target:
            self.delete(target[0])
        rx = random.randint(0, count_bodysizeW - 1)  # -1 чтобы мишень не оказалась за экраном
        ry = random.randint(0, count_bodysizeH - 1)  # -1 чтобы мишень не оказалась за экраном
        self.create_image(rx * BODYSIZE, ry * BODYSIZE, anchor="nw", image=self.target, tag="target")

    def on_key_pressed(self, event):
        key = event.keysym
        if key == "Left" and self.direction != "Right":
            self.direction_temp = key
        elif key == "Right" and self.direction != "Left":
            self.direction_temp = key
        elif key == "Up" and self.direction != "Down":
            self.direction_temp = key
        elif key == "Down" and self.direction != "Up":
            self.direction_temp = key

    def update_direction(self):
        self.direction = self.direction_temp
        head = self.find_withtag("head")
        headx, heady = self.coords(head)  # ищем координаты головы
        self.delete(head)
        if self.direction == "Left":
            self.head = ImageTk.PhotoImage(self.head_image.transpose(Image.FLIP_LEFT_RIGHT).
                                           resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))  # отражение головы
        else:
            rotates = {"Right": 0, "Up": 90, "Down": - 90}
            self.head = ImageTk.PhotoImage(self.head_image.rotate(rotates[self.direction]).
                                           resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))

        self.create_image(headx, heady, image=self.head, anchor="nw", tag="head")

    def timer(self):
        if not self.lose:
            self.update_direction()  # проверка нажатых клавиш
            self.move_snake()  # движение змейки
            self.after(self.delay, self.timer)  # создание анимации

    def move_snake(self):
        head = self.find_withtag("head")
        body = self.find_withtag("body")
        items = body + head
        for i in range(len(items) - 1):  # все элементы кроме головы
            currentxy = self.coords(items[i])
            nextxy = self.coords(items[i + 1])
            self.move(items[i], nextxy[0] - currentxy[0], nextxy[1] - currentxy[1])  # двигаем хвосты
        if self.direction == "Left":
            self.move(head, -BODYSIZE, 0)
        elif self.direction == "Right":
            self.move(head, BODYSIZE, 0)
        elif self.direction == "Up":
            self.move(head, 0, -BODYSIZE)
        elif self.direction == "Down":
            self.move(head, 0, BODYSIZE)


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