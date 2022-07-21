from tkinter import *
from tkinter import messagebox
import re

FONT_NAME = "Courier"
MINUTE = 60
opened_file = open("text_to_type.txt", "r+")
text = opened_file.read()
text_list = text.split()


def timer(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, timer, count - 1)
    if count == 0:
        answer = entry.get('1.0', 'end-1c')
        user_list = re.findall('\w+', answer)
        right_answer_list = []
        for word in user_list:
            word_index = user_list.index(word)
            if word.lower() == text_list[word_index]:
                right_answer_list.append(word)
        wpm = len(right_answer_list)
        right_answer = ""
        for item in right_answer_list:
            right_answer += item + " "

        if right_answer != "":
            message = f"Your speed is {wpm} words per minute.\nRight words are:\n{right_answer}"
        else:
            message = "You haven't typed any right word.\nPlease try again!"
        messagebox.showinfo("Score", message)


def start_typing():
    timer(10)


def clear_entry():
   entry.delete("1.0", "end")


def finish():
    opened_file.close()
    window.destroy()


window = Tk()
window.title("Welcome to a Type Speed Tester!")
window.config(padx=50, pady=50, bg="#fff", highlightthickness=0)

welcome_label = Label(text="Press 'Go!' and start typing as fast as you can!", bg="#fff", fg="#EB4747", font=(FONT_NAME, 15, "bold"))
welcome_label.grid(row=0, column=0)

canvas = Canvas(width=400, height=301, highlightthickness=0)
timer_img = PhotoImage(file="timer.png")
canvas.create_image(200, 150, image=timer_img)
timer_text = canvas.create_text(132, 150, text="00:00", fill="#EB4747", font=(FONT_NAME, 31, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

go_button = Button(text="Go!", width=18,  bg="#B25068", fg="#fff", font=(FONT_NAME, 15, "bold"), command=start_typing)
go_button.grid(row=2, column=1)

words_label = Label(text=text, bg="#4C3A51", fg="#fff", height=11, width=60, font=(FONT_NAME, 12), wraplength=600)
words_label.grid(row=1, column=0)

entry = Text(height=14, width=75, bg="#FFC18E", fg="#4C3A51")
entry.grid(row=2, column=0)

restart_button = Button(text="RESTART", bg="#B25068", fg="#fff", width=18, font=(FONT_NAME, 15, "bold"), command=clear_entry)
restart_button.grid(row=3, column=0)

done_button = Button(text="DONE", width=18, bg="#B25068", fg="#fff", font=(FONT_NAME, 15, "bold"), command=finish)
done_button.grid(row=4, column=0)


window.mainloop()















