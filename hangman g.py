from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

window=Tk()

cars=["FORD","MUSTANG","MAHINDRA","SUZUKI","TATA","MARUTI","TOYOTA","HYUNDAI","HONDA","MERCEDES","BMW"]
fruits=["APPLES","BANANA","MANGO","KIWI","PINEAPPLE","WATERMELON","ORANGE","STRAWBERRY","LITCHI","GRAPES"]
country=["INDIA","AUSTRALIA","NEPAL","BANGLADESH","SRILANKA","CHINA","AFGHANISTAN","SWITZERLAND","NEWZELAND","SCOTLAND","BERLIN","PORTUGAL","ARGENTINA","BRAZIL","ENGLAND","CRAOTIA","FRANCE","ISRAEL","RUSSIA"]
states_of_india=["RAJASTHAN","UTTRAKHAND","KERALA","HARYANA","GUJRAT","GOA","PUNJAB","HYDERABAD","CHANDIGARH"]
flowers=["ROSE","LOTUS","SUNFLOWER","LILY","JASMINE","HIBISCUS","LAVENDER","DAISY","ALOEVERA","HIPTAGE"]
sports=["CRICKET","FOOTBALL","HOCKEY","BASEBALL","FOOSEBALL","TENNIS","BADMINTON","BASKETBALL","SWIMMIMG","POLO","HORSE RIDING","VOLLEYBALL"]
animals = ["RAFAY", "LION", "PANDA", "TIGER", "DOG", "CAT", "RABIT", "MOUSE"]
main_list = [cars,fruits,country,states_of_india,flowers,sports,animals]
photos = [PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang0.png"), PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang1.png"), PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang2.png"), PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang3.png"),
          PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang4.png"), PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang5.png"), PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang6.png"), PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang7.png"),
          PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang8.png"), PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang9.png"), PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang10.png"), PhotoImage(file="/Users/yogeshpoonia/Documents/work/python/images 3/hang11.png")]

def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    global the_word
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    word_list = random.choice(main_list)
    the_word=random.choice(word_list)
    if word_list == cars:
        messagebox.showinfo("Hangman", "Its a Car Brand!")
    elif word_list == country:
        messagebox.showinfo("Hangman", "Its name of a country!")
    elif word_list == fruits:
        messagebox.showinfo("Hangman", "Its a Fruit!") 
    elif word_list == states_of_india:
        messagebox.showinfo("Hangman", "Its a Indian state!")
    elif word_list == flowers:
        messagebox.showinfo("Hangman", "Its a flower!")  
    elif word_list == sports:
        messagebox.showinfo("Hangman", "Its a sport!")  
    elif word_list == animals:
        messagebox.showinfo("Hangman", "Its a animal!")
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))



def guess(letter):
    global numberOfGuesses
    global the_word
    if numberOfGuesses<11:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You Guessed it")
                    newGame()
        else:
                numberOfGuesses+=1
                imgLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses==11:
                 messagebox.showwarning("Hangman", f"    Game Over \n The word was {the_word}")
    
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar() 
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)
n=0
for let in ascii_uppercase:
    Button(window, text=let, command=lambda let=let:guess(let), font=("Helvetica 18"), width=4,bg = 'black',fg = 'grey').grid(row=1+n//9, column=n%9,sticky="NSWE")
    n+=1

Button(window, text="New\nGame", command=lambda:newGame(),font=("Helvetica 10 bold"),bg = 'black',fg = 'red').grid(row=3, column=8, sticky="NSWE")

newGame()    
window.mainloop()