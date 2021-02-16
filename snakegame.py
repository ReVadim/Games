import random
from tkinter import *
from PIL import Image, ImageTk

WIDTH = 600
HEIGHT = 600
BODYSIZE = 60
STARTDELAY = 500
MINDELAY = 100
STEPDELAY = 10
LENGTH = 3

count_bodysizeW = WIDTH / BODYSIZE
count_bodysizeH = HEIGHT / BODYSIZE
x = [0] * int(count_bodysizeW)
y = [0] * int(count_bodysizeH)


class Snake(Canvas):
    x, y = False, False
    background_image = False
    background = False
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
        self.background_image = Image.open("images/bg.png")
        self.background = ImageTk.PhotoImage(self.background_image)
        self.head_image = Image.open("images/head.png")
        self.head = ImageTk.PhotoImage(self.head_image.resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.body = ImageTk.PhotoImage(Image.open("images/body.png").resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.target = ImageTk.PhotoImage(Image.open("images/target.png").resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))

    def begin_play(self):
        self.direction = "Right"
        self.delay = STARTDELAY
        self.lose = False
        self.x = [0] * int(count_bodysizeW)
        self.y = [0] * int(count_bodysizeH)
        self.delete(ALL)  # отчистка карты
        self.spawn_actors()  # создание игроков
        self.after(self.delay, self.timer)  # создание анимации

    def spawn_actors(self):
        self.spawn_bcgnd()
        self.spawn_target()
        self.x[0] = int(count_bodysizeW / 2) * BODYSIZE
        self.y[0] = int(count_bodysizeH / 2) * BODYSIZE
        for i in range(1, LENGTH):
            self.x[i] = self.x[0] - BODYSIZE * i  # создаём голову
            self.y[i] = self.y[0]
        self.create_image(self.x[0], self.y[0], image=self.head, anchor="nw", tag="head")
        for i in range(LENGTH - 1, 0, -1):
            self.create_image(self.x[i], self.y[i], image=self.body, anchor="nw", tag="body")

    def spawn_bcgnd(self):
        self.create_image(self.x[0], self.y[0], image=self.background, anchor="nw", tag="background")

    def spawn_target(self):
        target = self.find_withtag("target")
        if target:
            self.delete(target[0])
        rx = random.randint(0, count_bodysizeW - 1)  # -1 чтобы мишень не оказалась за экраном
        ry = random.randint(0, count_bodysizeH - 1)  # -1 чтобы мишень не оказалась за экраном
        self.create_image(rx * BODYSIZE, ry * BODYSIZE, anchor="nw", image=self.target, tag="target")

    def check_target(self):
        target = self.find_withtag("target")[0]
        head = self.find_withtag("head")
        body = self.find_withtag("body")[-1]
        x1, y1, x2, y2 = self.bbox(head)  # программа находит координаты прямоугольника головы
        overlaps = self.find_overlapping(x1, y1, x2, y2)  # метод поиска пересечений объектов
        for actor in overlaps:
            if actor == target:
                temp_x, temp_y = self.coords(body)  # сохраняем текущие координаты
                self.spawn_target()  # создаем новую цель
                self.create_image(temp_x, temp_y, image=self.body, anchor="nw", tag="body")  # новый хвост
                if self.delay > MINDELAY:  # увеличиваем скорость (уменьшаем задержку)
                    self.delay -= STEPDELAY

    def check_collisions(self):
        head = self.find_withtag("head")
        body = self.find_withtag("body")
        x1, y1, x2, y2 = self.bbox(head)
        overlaps = self.find_overlapping(x1, y1, x2, y2)
        for b in body:
            for actor in overlaps:
                if actor == b:
                    self.lose = True  # проверяем не столкнулась ли змейка сама с собой
        params = [
            x1 < 0,
            x2 > WIDTH,
            y1 < 0,
            y2 > HEIGHT
        ]  # проверка на выход за пределы экрана
        if any(params):
            self.lose = True

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
        elif key == "space" and self.lose:
            self.direction_temp = "Right"
            self.begin_play()
        elif key == "q" and self.lose:
            exit()

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
        self.check_collisions()
        if not self.lose:
            self.check_target()
            self.update_direction()  # проверка нажатых клавиш
            self.move_snake()  # движение змейки
            self.after(self.delay, self.timer)  # создание анимации
        else:
            self.game_over()

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

    def game_over(self):
        body = self.find_withtag("body")
        self.delete(ALL)
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2 - 120, text="Конец игры", font="Tahoma 25", fill="white", tag="text")
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2 - 60, text="Длина змейки: " + str(len(body)+1), font="Tahoma 25", fill="white", tag="text")
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2, text="Нажмите пробел для новой игры", font="Tahoma 25", fill="white", tag="text")
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2 + 120, text="Нажмите q для выхода", font="Tahoma 15", fill="red", tag="text")


root = Tk()
root.title("Змейка")
root.board = Snake()
root.resizable(False, False)
scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()
x_root = int(scr_width / 2 - WIDTH / 2)
y_root = int(scr_height / 2 - HEIGHT / 2)
root.geometry("+{0}+{1}".format(x_root, y_root))
root.mainloop()