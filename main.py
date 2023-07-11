import tkinter
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = None

try:
    data = pandas.read_csv(
        "C:/Users/anshm/Documents/Python Projects/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(
        "C:/Users/anshm/Documents/Python Projects/Flash Card App/data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = tkinter.Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Learn French")
flip_timer = window.after(3000, func=flip_card)


canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage(
    file="C:/Users/anshm/Documents/Python Projects/Flash Card App/images/card_front.png")
card_back_img = tkinter.PhotoImage(
    file="C:/Users/anshm/Documents/Python Projects/Flash Card App/images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tkinter.PhotoImage(
    file="C:/Users/anshm/Documents/Python Projects/Flash Card App/images/wrong.png")
no_button = tkinter.Button(
    image=cross_image, highlightthickness=0, command=next_card)
no_button.grid(row=1, column=0)

tick_image = tkinter.PhotoImage(
    file="C:/Users/anshm/Documents/Python Projects/Flash Card App/images/right.png")
yes_button = tkinter.Button(
    image=tick_image, highlightthickness=0, command=is_known)
yes_button.grid(row=1, column=1)

next_card()

window.mainloop()
