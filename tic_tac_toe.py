from tkinter import *
import tkinter.messagebox

# Initialize the main application window
tk = Tk()
tk.title("Tic Tac Toe")
tk.configure(bg='#cb464e')

# Variables for player names and turn tracking
player_a_name = StringVar()
player_b_name = StringVar()
p1 = StringVar()
p2 = StringVar()
bclick = True  # True if Player 1's turn, False if Player 2's
flag = 0       # Move counter for detecting ties

# Create entry fields for player names
player1_entry = Entry(tk, textvariable=p1, bd=5, bg='#fcfcec', width=40)
player1_entry.grid(row=1, column=1, columnspan=8)
player2_entry = Entry(tk, textvariable=p2, bd=5, bg='#fcfcec', width=40)
player2_entry.grid(row=2, column=1, columnspan=8)

# Disable all buttons after a win or tie
def disable_buttons():
    for button in button_list:
        button.configure(state=DISABLED)

# Reset the game to allow players to play again
def reset_game():
    global bclick, flag
    bclick = True
    flag = 0
    for button in button_list:
        button.config(text=" ", state=NORMAL)

# Handle button clicks for player moves
def btn_click(button):
    global bclick, flag, player_a_name, player_b_name
    if button["text"] == " " and bclick:  # Player 1's turn
        button["text"] = "X"
        bclick = False
        player_a_name = p1.get() + " Wins!"
        player_b_name = p2.get() + " Wins!"
        check_for_win()
        flag += 1
    elif button["text"] == " " and not bclick:  # Player 2's turn
        button["text"] = "O"
        bclick = True
        check_for_win()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already clicked!")

# Check if there is a winner or if the game is a tie
def check_for_win():
    # Define winning combinations
    winning_combinations = [
        (button1, button2, button3),
        (button4, button5, button6),
        (button7, button8, button9),
        (button1, button5, button9),
        (button3, button5, button7),
        (button1, button4, button7),
        (button2, button5, button8),
        (button3, button6, button9)
    ]
    
    for combo in winning_combinations:
        if all(button['text'] == 'X' for button in combo):
            disable_buttons()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", player_a_name)
            reset_game()
            return
        elif all(button['text'] == 'O' for button in combo):
            disable_buttons()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", player_b_name)
            reset_game()
            return

    # If all 9 moves are made without a win, it's a tie
    if flag == 8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie!")
        reset_game()

# Create labels for player name entries
Label(tk, text="Player 1:", font='Times 20 bold', bg='#cb464e', fg='#fcfcec', height=1, width=8).grid(row=1, column=0)
Label(tk, text="Player 2:", font='Times 20 bold', bg='#cb464e', fg='#fcfcec', height=1, width=8).grid(row=2, column=0)

# Create Tic-Tac-Toe buttons
button1 = Button(tk, text=" ", font='Times 20 bold', bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda: btn_click(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda: btn_click(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda: btn_click(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda: btn_click(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda: btn_click(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda: btn_click(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda: btn_click(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda: btn_click(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='#4b7fa4', fg='#fcfcec', height=4, width=8, command=lambda: btn_click(button9))
button9.grid(row=5, column=2)

# List of buttons for easy access in functions
button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

# Start the main loop for the application
tk.mainloop()

