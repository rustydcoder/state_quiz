import tkinter as tk
from tkinter import simpledialog, messagebox
from turtle import TurtleScreen, RawTurtle
from countdown import Countdown
from quiz import Quiz

# ---------------------------- CONSTANTS ------------------------------- #
IMAGE = "assets/plain_map.gif"
BG_COLOR = "#352F44"
FONT = ("Arial", 25, "bold")
QUIZ_TIME = 1
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800


# ---------------------------- Play Game ------------------------------- #
def play_game():
    quiz_time = QUIZ_TIME * 60
    timer = Countdown(label=countdown_label, frame=window, status=status_label, close_dialog=empty_frame)
    timer.start_counting(quiz_time)
    quiz = Quiz(turtle)

    flag = True
    while flag:
        score = quiz.get_score()
        scoreboard_label.config(text=score)
        answer = simpledialog.askstring(parent=empty_frame,
                                        title="Enter a state", prompt="Name another state?\t\t")

        if answer is None or answer.lower() == "exit":
            flag = False
            timer.stop_counting()
            time = countdown_label.cget("text")
            summary = quiz.quiz_summary(time=time)
            messagebox.showinfo(title="Summary", message=summary)
        else:
            quiz.set_answer(answer.lower())
            quiz.display_position()

    window.destroy()


# ---------------------------- UI ------------------------------- #
window = tk.Tk()
window.geometry("%dx%d" % (WINDOW_WIDTH, WINDOW_HEIGHT))
window.title("Nigerian State Quiz Game")
window.config(bg=BG_COLOR)

# TOOLBAR
toolbar_frame = tk.Frame(window, relief="sunken", width=800, height=100)
toolbar_frame.pack()

start_btn = tk.Button(toolbar_frame, text="Start", highlightthickness=0, width=12, pady=8, command=play_game)
start_btn.grid(row=0, column=0, pady=3, padx=30)

countdown_label = tk.Label(toolbar_frame, text="00:00", font=FONT)
countdown_label.grid(row=0, column=1, pady=3, padx=30)

scoreboard_label = tk.Label(toolbar_frame, text="00/00", font=FONT)
scoreboard_label.grid(row=0, column=2, pady=3, padx=30)

status_label = tk.Label(toolbar_frame, text="Status: Not playing", width=15, font=(FONT[0], 15, "bold"))
status_label.grid(row=0, column=3, pady=3, padx=30)

# CANVAS
turtle_frame = tk.Frame(window, width=750, height=577)
turtle_frame.pack()

empty_frame = tk.Frame(turtle_frame)
empty_frame.pack()

canvas = tk.Canvas(turtle_frame, width=750, height=577)
canvas.pack()

screen = TurtleScreen(canvas)
screen.bgpic(IMAGE)
turtle = RawTurtle(screen)

window.mainloop()
