from turtle import * 
speed(10000)

#bmw circle
goto(0, -250)
width(8)
fillcolor("black")
begin_fill()
pencolor("grey")
circle(250)
end_fill()


penup()
goto(0,300)
pendown() 

#f90 m5 competition 
color("black")
write("f90 m5 competition", align="center", font=('arial', 40 ) ) 

# bmw შიგნითა წრე 
width(3)
penup()
goto(0, -150)
pendown()
fillcolor("white")
begin_fill()
circle(150)
end_fill()

#ბმწ ცისფერი ლოგოს ნაწილი

fillcolor("deepskyblue")
begin_fill()
circle(150,90)
left(90)
width(2)
pencolor("black")
forward(150)
left(90)
forward(150)
end_fill()

# bmw ცისფერი ლოგოს ნაწილი 2

penup()
goto(-150,0)
pendown()
begin_fill()
width(3)
pencolor("black")
circle(150,-90)
left(90)
width(2)
pencolor("black")
forward(150)
right(90)
forward(150)
end_fill() 

width(12)
pencolor("white")

#B
penup()
goto(0,0)
right(30)
forward(165)
right(5)
pendown()
forward(65)
right(90)
forward(35)
circle(-16,180)
forward(35)
right(90)
right(90)
forward(35)
circle(-16,180)
forward(35)


#M
penup()
goto(-32,165)
setheading(90)
pendown()
forward(62)
goto(0,180)
goto(32,227)
right(180)
forward(62)


#w

penup()
goto(0,0)
setheading(52)
forward(228)
pendown()
right(170)
forward(65)
left(140)
forward(50)
right(140)
forward(50)
left(140)
forward(65)




















exitonclick()