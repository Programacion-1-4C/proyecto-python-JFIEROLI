import turtle
import time
import pickle

window = turtle.Screen()
window.bgcolor("black")
window.title("Laberinto")
window.setup(700,700)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed(0)
        self.direction = 'stop'

class Final(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color("green")
        self.penup()
        self.speed(0)

niveles = []

# Nivel 1
nivel_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXP            X     X X",
"XX  XXXXXXX X X X x X   X",
"XX XXXXXXX  X XXXXXXXX XX",
"XX XXXXXXX X            X",
"XX XXXXXXX XXXXXXXXXXXFXX",
"XXXXXXXXXX XXXXXXXXXXXXXX",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"X X X                   X X X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
niveles.append(nivel_1)

bloques = []

def iniciar_lab(nivel):
    for fila in range(len(nivel)):
        for column in range(len(nivel[fila])):
            letraX = nivel[fila][column]
            screen_x = -288 + (column * 24)
            screen_y = 288 - (fila * 24)

            if letraX == "X":
                Nuevo_bloque = turtle.Turtle()
                Nuevo_bloque.speed(0)
                Nuevo_bloque.shape('square')
                Nuevo_bloque.color('white')
                Nuevo_bloque.penup()
                bloques.append(Nuevo_bloque)
                Nuevo_bloque.goto(screen_x, screen_y)

            if letraX == "P":
                player.goto(screen_x, screen_y)

            if letraX == "F":
                final.goto(screen_x, screen_y)  

player = Player()
final = Final()

iniciar_lab(niveles[0])

# Funciones

def arriba():
    player.direction = 'up'
def abajo():
    player.direction = 'down'
def derecha():
    player.direction = 'right'
def izquierda():
    player.direction = 'left'

def guarda_coor():
    eje_x = player.xcor()
    eje_y = player.ycor()
    with open("coordenada.pickle", "wb") as pickle_file:
        pickle.dump(eje_x, pickle_file)
        pickle.dump(eje_y, pickle_file)

def moverse():
    if player.direction == "up":
        guarda_coor()
        y = player.ycor()
        player.sety(y + 24)
        player.direction = "stop"
        
    if player.direction == "down":
        guarda_coor()
        y = player.ycor()
        player.sety(y - 24)
        player.direction = "stop"

    if player.direction == "left":
        guarda_coor()
        x = player.xcor()
        player.setx(x - 24)
        player.direction = "stop"

    if player.direction == "right":
        guarda_coor()
        x = player.xcor()
        player.setx(x + 24)
        player.direction = "stop"

# Teclado

window.listen()
window.onkey(arriba, "w")
window.onkey(abajo, "s")
window.onkey(derecha, "d")
window.onkey(izquierda, "a")

# Juego
while True:
    window.update()

    moverse()
    
    # Colision con las paredes despues de 1 segundo
    for Nuevo_bloque in bloques:
        if player.distance(Nuevo_bloque) < 24:
            with open("coordenada.pickle", "rb") as pickle_file:
                eje_x = pickle.load(pickle_file)
                eje_y = pickle.load(pickle_file)
            player.goto(eje_x, eje_y)

    time.sleep(0.1)