#not completed yet

from turtle import *
#setup()
colormode(255)
t = Turtle()
t.speed(0)

px = 10


f = open("randombytes", "rb")
f.seek(0,2)
size = f.tell()
side = int( (size/3)**(1/2) ) * px
f.seek(0)

t.hideturtle()
i = 0
j = 0
while f:
  try:
    r = ord(f.read(1))
    g = ord(f.read(1))
    b = ord(f.read(1))
  except:
    break

  if i == side:
    i = 0
    j -= px
  t.goto(i,j)
  i += px

  t.down()

  t.color(r,g,b)
  t.begin_fill()
  #t.circle(px)
  t.forward(px)
  t.right(90)
  t.forward(px)
  t.right(90)
  t.forward(px)
  t.right(90)
  t.forward(px)
  t.right(90)
  t.end_fill()

  t.up()



ts = getcanvas()
ts.postscript(file="rb.ps", colormode='color')

#done()

#to see
import time
time.sleep(5)
