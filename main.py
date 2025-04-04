from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(10)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(background=YELLOW)
window.config(padx=100, pady=50, height=400, width=400)
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 34,"bold"))
label.grid(column=1,row=0)
canvas = Canvas(window, height=226, width=204, highlightthickness=0)
canvas.config(background=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
image = canvas.create_image(103,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset",highlightthickness=0)
reset_btn.grid(column=2, row=2)
check_mark_lbl = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark_lbl.grid(column=1, row=3)









window.mainloop()