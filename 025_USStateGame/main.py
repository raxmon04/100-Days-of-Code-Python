import turtle
import pandas

# --- Setup ---
screen = turtle.Screen()
screen.title("U.S. States Game")

IMAGE_PATH = "/mnt/d/Git/python/025_USStateGame/blank_states_img.gif"
CSV_PATH = "/mnt/d/Git/python/025_USStateGame/50_states.csv"

screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

data = pandas.read_csv(CSV_PATH)
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
	answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name? Type Exit to Quit")
	if answer_state:
		answer_state = answer_state.title()
	if answer_state == "Exit":
		missing_states = [state for state in all_states if state not in guessed_states]
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("/mnt/d/Git/python/025_USStateGame/states_to_learn.csv")
		break
	if answer_state in all_states:
		guessed_states.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == answer_state]
		t.goto(state_data.x.item(), state_data.y.item())
		t.write(answer_state)