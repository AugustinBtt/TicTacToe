from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic Tac Toe")
window.config(padx=30, pady=30, bg='#505251')

button_frame = Frame(window, bg='#505251')
button_frame.grid(row=0, column=0)

def is_winner():
    global player_x, player_o
    # horizontal linesa
    if button1.cget("text") == button2.cget("text") == button3.cget("text"):
        if button1.cget("text") == 'X':
            player_x += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player X won", parent=window)
            reset_game()
        elif button1.cget("text") == 'O':
            player_o += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player O won", parent=window)
            reset_game()

    elif button4.cget("text") == button5.cget("text") == button6.cget("text"):
        if button4.cget("text") == 'X':
            player_x += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player X won", parent=window)
            reset_game()
        elif button4.cget("text") == 'O':
            player_o += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player O won", parent=window)
            reset_game()

    elif button7.cget("text") == button8.cget("text") == button9.cget("text"):
        if button7.cget("text") == 'X':
            player_x += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player X won", parent=window)
            reset_game()
        elif button7.cget("text") == 'O':
            player_o += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player O won", parent=window)
            reset_game()

    # vertical lines
    elif button1.cget("text") == button4.cget("text") == button7.cget("text"):
        if button1.cget("text") == 'X':
            player_x += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player X won", parent=window)
            reset_game()
        elif button1.cget("text") == 'O':
            player_o += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player O won", parent=window)
            reset_game()

    elif button2.cget("text") == button5.cget("text") == button8.cget("text"):
        if button2.cget("text") == 'X':
            player_x += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player X won", parent=window)
            reset_game()
        elif button2.cget("text") == 'O':
            player_o += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player O won", parent=window)
            reset_game()

    elif button3.cget("text") == button6.cget("text") == button9.cget("text"):
        if button3.cget("text") == 'X':
            player_x += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player X won", parent=window)
            reset_game()
        elif button3.cget("text") == 'O':
            player_o += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player O won", parent=window)
            reset_game()

    # Diagonals
    elif button1.cget("text") == button5.cget("text") == button9.cget("text"):
        if button1.cget("text") == 'X':
            player_x += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player X won", parent=window)
            reset_game()
        elif button1.cget("text") == 'O':
            player_o += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player O won", parent=window)
            reset_game()

    elif button3.cget("text") == button5.cget("text") == button7.cget("text"):
        if button3.cget("text") == 'X':
            player_x += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player X won", parent=window)
            reset_game()
        elif button3.cget("text") == 'O':
            player_o += 1
            update_score()
            messagebox.showinfo(title="Winner", message="Player O won", parent=window)
            reset_game()
    elif all([button1.cget("text"), button2.cget("text"), button3.cget("text"),
              button4.cget("text"), button5.cget("text"), button6.cget("text"),
              button7.cget("text"), button8.cget("text"), button9.cget("text")]):
        messagebox.showinfo(title="Draw", message="It's a draw!", parent=window)
        reset_game()

# Function to handle button click
def on_button_click(button):
    if game_state["is_player_x_turn"]:
        button.config(text="X")
    else:
        button.config(text="O")
    game_state["is_player_x_turn"] = not game_state["is_player_x_turn"]
    is_winner()

game_state = {"is_player_x_turn": True}

button1 = Button(window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e', activebackground='#edbc2e',
                 command=lambda: on_button_click(button1))
button2 = Button(window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e', activebackground='#edbc2e',
                 command=lambda: on_button_click(button2))
button3 = Button(window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e', activebackground='#edbc2e',
                 command=lambda: on_button_click(button3))
button4 = Button(window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e', activebackground='#edbc2e',
                 command=lambda: on_button_click(button4))
button5 = Button(window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e', activebackground='#edbc2e',
                 command=lambda: on_button_click(button5))
button6 = Button(window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e', activebackground='#edbc2e',
                 command=lambda: on_button_click(button6))
button7 = Button(window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e', activebackground='#edbc2e',
                 command=lambda: on_button_click(button7))
button8 = Button(window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e', activebackground='#edbc2e',
                 command=lambda: on_button_click(button8))
button9 = Button(window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e', activebackground='#edbc2e',
                 command=lambda: on_button_click(button9))

button1.grid(row=0, column=0, in_=button_frame)
button2.grid(row=0, column=1, in_=button_frame)
button3.grid(row=0, column=2, in_=button_frame)
button4.grid(row=1, column=0, in_=button_frame)
button5.grid(row=1, column=1, in_=button_frame)
button6.grid(row=1, column=2, in_=button_frame)
button7.grid(row=2, column=0, in_=button_frame)
button8.grid(row=2, column=1, in_=button_frame)
button9.grid(row=2, column=2, in_=button_frame)

def exit_game():
    window.destroy()

player_x = 0
player_o = 0

# Function to reset the game
def reset_game():
    button1.config(text="")
    button2.config(text="")
    button3.config(text="")
    button4.config(text="")
    button5.config(text="")
    button6.config(text="")
    button7.config(text="")
    button8.config(text="")
    button9.config(text="")
    game_state["is_player_x_turn"] = True

def update_score():
    score.config(text=f"X: {player_x} pts | O: {player_o} pts")

score = Label(window, text=f"X: {player_x} pts | O: {player_x} pts")
score.grid(row=1, column=0, pady=5)

exit_button = Button(window, text="Exit", command=exit_game)
exit_button.grid(row=2, column=0, pady=5)

window.geometry("+%d+%d" % (window.winfo_screenwidth() // 2.05 - 100, window.winfo_screenheight() // 2.3 - 100))

messagebox.showinfo(title="Welcome", message="First player will play as X", parent=window)


window.mainloop()











