from turtle import Turtle
import random
from turtle import Screen
flag=1
screen=Screen()
screen.setup(width=500, height=400)

user_bet=screen.textinput(title="Make your bet!",prompt="Which turtle will be win? Make a guess!")
user_bet=user_bet.lower()

colors=["red","green","yellow","orange","blue","purple"]
a=-150
all_turtles=[]
for turtles in range(0,6):
    ecem_turtle=Turtle(shape="turtle")
    ecem_turtle.color(colors[turtles])
    ecem_turtle.penup()
    ecem_turtle.goto(x=-230 ,y=a)
    a+=62
    all_turtles.append(ecem_turtle)
while flag==1:
    for x in all_turtles:
        x.forward(random.randint(0,10))
        if x.xcor() > 230:
            winning_color=x.pencolor()
            if winning_color== user_bet:
                print(f"You win! The {winning_color} turtle is the winner!!")
                flag=0
            else:
                print(f"You lost! The {winning_color} turtle is the winner!!")
                flag=0
   

screen.exitonclick()