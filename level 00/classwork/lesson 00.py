from turtle import *
speed(30)
width(4)

# კვადრატი 
color("brown")
forward(200)
left(90)

forward(200)
left(90) 

forward(200)
left(90) 

forward(200)
left(90)
 
 # კარები 
forward(70)
color("gray") 
begin_fill()
left(90) 
forward(120) # karebis simaghle 
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup() #კალმის აღება
goto(200,200) 
pendown()  #კალმის ჩამოღება 

#სახურავის დახაზვა
color("saddle brown")
begin_fill() #შიგნით გაფერადება
right(150)
forward(200)
left(120)
forward(200) 
end_fill() #გაფერადება დასრულებულია




exitonclick()