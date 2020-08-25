# change origin setup.py file,  Add brackets to the line, like: except (ValueError, ve):
# install turtle at your environment like: pip install -e C:\turtle-0.0.2

import turtle as t

t.setup(1100,1000)
t.hideturtle()
t.speed(11)
t.penup()
t.goto(50,-450)
t.pensize(5)
t.pencolor('black')
t.seth(140)
t.pendown()
t.speed(10)
t.circle(-300,60)
t.fd(100)
#jiaodu80

#1叶子
t.seth(10)
t.fd(50)
t.fillcolor('green')
t.begin_fill()
t.right(40)
t.circle(120,80)
t.left(100)
t.circle(120,80)
t.end_fill()
t.seth(10)
t.fd(90)
t.speed(11)
t.penup()
t.fd(-140)
t.seth(80)

#2叶子
t.pendown()
t.speed(10)
t.fd(70)
t.seth(160)
t.fd(50)
t.fillcolor('green')
t.begin_fill()
t.right(40)
t.circle(120,80)
t.left(100)
t.circle(120,80)
t.end_fill()
t.seth(160)
t.fd(90)
t.speed(11)
t.penup()
t.fd(-140)
t.seth(80)
t.pendown()
t.speed(10)
#
t.fd(100)

#1花瓣
t.seth(-20)
t.fillcolor('crimson')
t.begin_fill()
t.circle(100,100)
t.circle(-110,70)
t.seth(179)
t.circle(223,76)
t.end_fill()

#2花瓣
t.speed(11)
t.fillcolor('red')
t.begin_fill()

t.left(180)
t.circle(-223,60)
t.seth(70)
t.speed(10)
t.circle(-213,15)#55
t.left(70)#125
t.circle(200,70)
t.seth(-80)
t.circle(-170,40)
t.circle(124,94)
t.end_fill()
#
t.speed(11)
t.penup()
t.right(180)
t.circle(-124,94)
t.circle(170,40)
t.pendown()
t.speed(10)

t.seth(-60)
t.circle(175,70)

t.seth(235)
t.circle(300,12)
t.right(180)
t.circle(-300,12)

t.seth(125)
t.circle(150,60)

t.seth(70)
t.fd(-20)
t.fd(20)

t.seth(-45)
t.circle(150,40)
t.seth(66)
t.fd(-18.5)
t.fd(18.5)

t.seth(140)
t.circle(150,27)
t.seth(60)
t.fd(-8)

t.speed(11)
t.penup()
t.left(20.8)
t.fd(-250.5)

#3花瓣
t.pendown()
t.speed(10)
t.fillcolor('crimson')
t.begin_fill()
t.seth(160)

t.circle(-140,85)
t.circle(100,70)
t.right(165)
t.circle(-200,32)
t.speed(11)
t.seth(-105)
t.circle(-170,14.5)
t.circle(123,94)
t.end_fill()

t.done()