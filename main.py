from tkinter import *
import pandas
import random

learn = {
        "English": [],
        "French": []

    }

num = random.randint(0, 100)
words = pandas.read_csv(".\data\\french_words.csv")
french_word = words["French"].tolist()

def did_not_get_it():
    global learn

    words = pandas.read_csv(".\data\\french_words.csv")
    english_word = words["English"].tolist()
    eng_word = english_word[num]
    learn["English"].append(eng_word)


    words = pandas.read_csv(".\data\\french_words.csv")
    french_word = words["French"].tolist()
    frn_word = french_word[num]
    learn["French"].append(frn_word)

    learning_words = pandas.DataFrame(learn)
    learning_words.to_csv("the letters which u missed.csv")

def change_color():
    words = pandas.read_csv(".\data\\french_words.csv")
    english_word = words["English"].tolist()
    word.config(text=english_word[num])

    card.create_image(400, 263, image = card_back)
    title.config(bg=back_background, text="English")
    word.config(bg= back_background)
    window.after(3000, color_change)

def color_change():
    words = pandas.read_csv(".\data\\french_words.csv")
    french_word = words["French"].tolist()
    word.config(text= french_word[num])

    card.create_image(400, 263, image=card_front)
    title.config(bg=front_background, text="French")
    word.config(bg=front_background)
    window.after(3000, change_color)


def right_random_word():
    global num
    num = random.randint(0, 100)

def wrong_random_word():
    global num
    did_not_get_it()
    num = random.randint(0, 100)

BACKGROUND_COLOR = "#B1DDC6"


# window
window = Tk(className= "Flashy")
window.config(bg= BACKGROUND_COLOR)
window.config(padx=50, pady=50)


# cards being displayed
card = Canvas(height=526, width=800, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=".\images\card_front.png")
card_back = PhotoImage(file=".\images\card_back.png")
card.create_image(400, 263, image=card_front)
card.grid(column=0, row=0, columnspan=2)

# buttons
wrong = PhotoImage(file=".\images\wrong.png")
x_button = Button(image=wrong, highlightthickness= 0, command=wrong_random_word)
x_button.grid(column=0, row=1, pady=10)

right = PhotoImage(file= ".\\images\\right.png")
y_button = Button(image= right, highlightthickness=0, command=right_random_word)
y_button.grid(column=1, row=1, pady=10)




# labels
front_background ="#FBFBFB"
back_background ="#91C2AF"
title = Label(text="French", font=("Ariel",40,"italic"), bg= front_background)
title.place(x = 300, y=150)

word = Label(text=french_word[num], font=("Ariel", 60, "bold"), bg = front_background)
word.place(x= 300, y=263)

window.after(3000, change_color)


window.mainloop()