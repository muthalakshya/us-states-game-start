import turtle
import pandas


screen = turtle.Screen()
turtle.bgpic("blank_states_img.gif")

states = pandas.read_csv("50_states.csv")
state_list = []

score = 0
correct_guess = []
while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{score}/50 Correct states", prompt="What's another state?").title()
    print(answer_state)

    for st in states.state:
       state_list.append(st)
       if answer_state == st:
           state_for_cord = states[states.state == st]
           x_cord = int(state_for_cord.x)
           y_cord = int(state_for_cord.y)
           turtle.penup()
           turtle.hideturtle()
           turtle.goto(x_cord, y_cord)
           turtle.write(st, align="center", font=('Arial', 7, 'normal'))
           score += 1
           correct_guess.append(st)

screen.exitonclick()