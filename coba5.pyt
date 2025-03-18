import turtle
from PIL import Image

# Setup Screen
screen = turtle.Screen()
image = Image.open("himapsti.jpg")  # Membuka gambar dengan Pillow
image = image.resize((600, 600))  # Resize agar sesuai layar
image.save("himapsti_resized.gif")  # Simpan dalam format GIF (Turtle hanya mendukung GIF)

screen.bgpic("himapsti_resized.gif")  # Mengatur gambar sebagai background
screen.title("HIMA PSTI Logo")
screen.setup(width=600, height=600)

# Turtle Setup
t = turtle.Turtle()
t.speed(10)
t.pencolor("white")
t.pensize(3)

# Gambar Lingkaran Luar
t.penup()
t.goto(0, -200)
t.pendown()
t.circle(200)

# Gambar Tombol Power (Kanan Atas)
t.penup()
t.goto(50, 50)
t.pendown()
t.pensize(10)
t.seth(90)
t.circle(100, 180)
t.penup()
t.goto(50, 150)
t.pendown()
t.pensize(5)
t.circle(20)

# Wi-Fi Symbol (Kiri Atas)
t.penup()
t.goto(-30, 60)
t.pensize(5)
t.pendown()
t.seth(90)
t.circle(70, 180)
t.penup()
t.goto(-50, 40)
t.pendown()
t.circle(50, 180)
t.penup()
t.goto(-70, 20)
t.pendown()
t.circle(30, 180)

# Pena (Kiri Bawah)
t.penup()
t.goto(-100, -150)
t.pendown()
t.seth(45)
t.pensize(7)
t.forward(100)
t.penup()
t.goto(-100, -150)
t.pendown()
t.seth(-45)
t.forward(100)
t.penup()
t.goto(-100, -150)
t.pendown()
t.seth(0)
t.forward(70)

# Gear (Kanan Bawah)
t.penup()
t.goto(70, -70)
t.pendown()
t.pensize(3)
for _ in range(6):
    t.circle(50, 60)
    t.left(60)
    t.forward(20)
    t.backward(20)
    t.right(60)

# Selesai
t.hideturtle()
turtle.done()