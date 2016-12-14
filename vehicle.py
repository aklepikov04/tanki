import turtle

# Defining main vehicle class
class vehicle:
    def __init__(self):
        self.tur = turtle.Turtle()
        self.tur.speed(0)
        self.max_length = 20
        self.length_step = 2
        self.length = 0
        self.screen = turtle.Screen()
        self.tur.pencolor("black")
        self.color_finder = 0

    # Event handlers:
    def moving(self):
        if self.length > 0:
            self.tur.fd(self.length)
        self.screen.ontimer(self.moving, 40)

    def speed_up(self):
        if self.length < self.max_length:
            self.length += self.length_step

    def go_left(self):
        self.tur.left(15)

    def go_right(self):
        self.tur.right(15)

    def speed_down(self):
        if self.length > 0:
            self.length -= self.length_step

    # setup event handlers
    def set_handlers(self, fd, bd, lt, rt):
        self.screen.onkeypress(self.speed_up, fd)
        self.screen.onkeypress(self.go_left, lt)
        self.screen.onkeypress(self.go_right, rt)
        self.screen.onkeypress(self.speed_down, bd)
        self.screen.ontimer(self.moving, 40)

    def color(self, color):
        self.tur.color(color)


    def run(self):
        self.screen.listen()

