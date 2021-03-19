import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title='Guess the state', prompt='What\'s another states name?').title()
data = pandas.read_csv('50_states.csv')
state_name = data['state'].to_string()

if answer_state in state_name:
    print(answer_state)
