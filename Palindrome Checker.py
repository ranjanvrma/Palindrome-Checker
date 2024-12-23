#Palindrome Checker

from tkinter import *

root = Tk()

root.geometry("500x400")
root.title("Palindrome Checker")


def palindromeOutput():
    input_string = input1.get()
    output_string = input_string.upper()
    reversed_string = output_string[::-1]
    if(input1.get() == ""):
        myLabel1 = Label(frame4, text=f"Enter a Valid String")
        myLabel1.pack()

    elif(output_string == reversed_string) :
        myLabel1 = Label(frame4, text=f"{input1.get()} is an Palindrome")
        myLabel1.pack()
    else :
        myLabel1 = Label(frame4, text=f"{input1.get()} is not an Palindrome")
        myLabel1.pack()


frame1 = Frame(root)
frame1.pack()

titleLabel = Label(frame1, text="Palindrome Checker", font=("Arial", 23))
titleLabel.pack()

frame2 = Frame(root)
frame2.pack()

textLabel1 = Label(frame2, text="Enter text to check for Palindrome:")
textLabel1.grid(row=0, column=0)

input1 = Entry(frame2, relief=SUNKEN, width=30)
input1.grid(row=0, column=1)

frame3 = Frame(root)
frame3.pack()

textLabel2 = Label(frame3, text="")
textLabel2.grid(row=0, column=0)

checkButton = Button(frame3, text="Check", relief=RAISED, font=("Arial", 12), command=palindromeOutput)
checkButton.grid(row=1, column=0)

frame4 = Frame(root)
frame4.pack()

textLabel3 = Label(frame4, text="Result:")
textLabel3.pack()



root.mainloop()