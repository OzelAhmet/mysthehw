#not completed yet

from turtle import *
#setup()
#colormode(255)
t = Turtle()

"""
# no writing in turtle
fp1 = open("/tmp/a.txt","w+")
with fp1:
  for i in range(5):
    fp1.write("line" + str(i))
"""

i = 0
fp2 = open("/tmp/a.txt", "rb")
try:
  while fp2:
    r = ord(fp2.read(1))
    g = ord(fp2.read(1))
    b = ord(fp2.read(1))


    t.goto(0,i)
    i += 10
    t.down()
    t.color(r,g,b)

    t.begin_fill()
    #t.circle(10)
    t.forward(10)  # forward takes a number which is the distance to move
    t.right(90)  # turn right
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.end_fill()

    t.up()
except:
  pass
