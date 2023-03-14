from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        buttons[row][column]["text"] = player
        if player == players[0]:

            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + "'s turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins!"))

            elif check_winner() is None:
                label.config(text="Draw!")

        else :
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + "'s turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins!"))

            elif check_winner() is "draw":
                label.config(text="Draw!")

    else:
        label.config(text="This space is already taken")



def check_winner():
    winner = False

    # Check for horizontal wins
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            winner = True
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")

    # Check for vertical wins
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            winner = True
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")

    # Check for diagonal wins
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        winner = True
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")

    if buttons[2][0]["text"] == buttons[1][1]["text"] == buttons[0][2]["text"] != "":
        winner = True
        buttons[2][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[0][2].config(bg="green")

    # Check for a draw
    if winner is False:
        if empty_spaces() is False:
            label.config(text="Draw!")
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")

            return "draw"

    return winner

def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    player = random.choice(players)

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="SystemButtonFace")

    label.config(text=player + "'s turn")

window = Tk()
window.title("Tic Tac Toe")
window.geometry("300x450")

players = ["#", "%"]
player = random.choice(players)

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(window, text= player + "'s turn", font=("Arial", 20))
label.pack(side="top")

reset_button = Button(window, text="New Game", command=new_game, font=("Arial", 10))
reset_button.pack(side="top")

frame = Frame(window) # Create a frame for the buttons
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("Arial",40), width=2, height=1, command= lambda row=row, column=column: next_turn(row, column))

        # Place the button in the frame
        buttons[row][column].grid(row=row, column=column)
window.mainloop()
