#HOME Alexander
#HARAKAT Mohamed
#BARB06
import turtle

wn = turtle.Screen()  # module des graphiques tortue
tortue = turtle.Turtle()  # creer une nouvelle tortue
tortue.speed("fastest")  # tracee rapide


def square(size, color):
    """Trace un carre plein de taille `size` et de couleur `color`.

    pre: `color` specifie une couleur.
         La tortue `tortue` est initialisee.
         La tortue est placee a un sommet et orientee en direction d'un
         cote du carre.
    post: Le carre a ete trace sur la droite du premier cote.
          La tortue est a  la meme position et orientation qu'au depart.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()


def rectangle(width, height, color):
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for _ in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()


def three_color_flag(width, color1, color2, color3):
    width /= 3
    height = width * (3 / 2)

    for i in [color1, color2, color3]:
        rectangle(width, height, i)
        tortue.forward(width)
def belgian_flag(width):
    three_color_flag(width,"black","yellow","red")

def dutch_flag(width):
    height = width * ((1 / 6))
    for i in ["red", "white", "blue"]:
        rectangle(width, height, i)
        tortue.right(90)
        tortue.forward(height)
        tortue.left(90)
    # va en haut a droite du drapeau
    tortue.left(90)
    tortue.forward((height * 3))
    tortue.right(90)
    tortue.forward(width)


def german_flag(width):
    height = width * ((1 / 6))
    for i in ["black", "red", "yellow"]:
        rectangle(width, height, i)
        tortue.right(90)
        tortue.forward(height)
        tortue.left(90)
    # va en haut a droite du drapeau
    tortue.left(90)
    tortue.forward((height * 3))
    tortue.right(90)
    tortue.forward(width)


def luxembourg_flag(width):
    height = width * ((1 / 6))
    for i in ["red", "white", "cyan"]:
        rectangle(width, height, i)
        tortue.right(90)
        tortue.forward(height)
        tortue.left(90)
    # va en haut a droite du drapeau
    tortue.left(90)
    tortue.forward((height * 3))
    tortue.right(90)
    tortue.forward(width)


def french_flag(width):
    three_color_flag(width, "blue", "white", "red")


def star(size):
    tortue.color("yellow")
    tortue.pensize(1)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(5):
        tortue.forward(size)
        tortue.right(144)
    tortue.end_fill()
    tortue.forward(size * (1 / 3))
    tortue.right(90)
    tortue.forward(size * (15 / 100))
    tortue.begin_fill()
    tortue.circle(size * (20 / 100))
    tortue.end_fill()


def start_circle(radius, star_size):
    for x in range(12):
        tortue.penup()
        tortue.circle(radius, extent=30)
        tortue.left(90)
        tortue.penup()
        star(star_size)
        tortue.penup()


def european_flag(width):
    height = width * ((1 / 2))
    rectangle(width, height, "blue")
    tortue.forward(width * (35 / 100))
    tortue.right(90)
    tortue.forward(width * (30 / 100))
    start_circle(width * (15 / 100), width * (5 / 100))

def belgium_circle(radius, flag_size):
    for _ in range(12):
        tortue.penup()
        tortue.circle(radius, extent=30)
        tortue.left(90)
        tortue.forward(flag_size / 2)
        tortue.right(90)
        belgian_flag(flag_size)
        tortue.right(90)
        tortue.forward(flag_size / 2)
        tortue.left(90)
tortue.penup()
tortue.left(180)
tortue.forward(500)
tortue.left(180)
german_flag(200)
tortue.penup()
tortue.forward(500)
dutch_flag(200)
tortue.left(90)
tortue.forward(250)
tortue.left(90)
tortue.forward(550)
tortue.left(180)
luxembourg_flag(200)
tortue.right(90)
tortue.forward(600)
tortue.right(90)
tortue.forward(200)
tortue.right(90)
tortue.forward(100)
tortue.right(90)
french_flag(200)
tortue.left(90)
tortue.forward(250)
tortue.left(90)
tortue.forward(200)
tortue.left(180)
european_flag(200)
tortue.forward(10)
tortue.right(90)
tortue.forward(155)
tortue.left(90)

belgium_circle(90,50)
wn.mainloop()