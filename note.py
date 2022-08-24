import pyttsx3
from tkinter import *
from tkinter import filedialog
from time import strftime
import os

root = Tk()
root.geometry("640x480")
root.title("Notes")
icon = PhotoImage(file='C:\\Users\\maths\\Pictures\\pngkeys2.png')
root.iconphoto(True, icon)
root.config(bg='black')
root.resizable(False, False)



def save_file():
    print("")
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if open_file is None:
        return
    text = str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()


def open_file():
    file = filedialog.askopenfile(mode='r', filetype=[('text files', '*.txt')], defaultextension='.txt')
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)


# DIGITAL CLOCK TO SHOW THE TIME:
def get_time():
    string = strftime('%H:%M:%S %p')
    clock.config(text=string)
    clock.after(1000, get_time)

def speak():
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    textcontent = entry.get(1.0, END)
    speaker.say(textcontent)
    speaker.runAndWait()


#####################################################################################################################
#####################################################################################################################

# -------------------- OPEN A NEW WINDOW WITH A CALCULaTOR IN IT --------------------

def open_calc():
    global expression
    # globally declare the expression variable
    expression = ""

    # Function to update expression
    # in the text entry box
    def press(num):
        # point out the global expression variable
        global expression

        # concatenation of string
        expression = expression + str(num)

        # update the expression by using set method
        equation.set(expression)

    # Function to evaluate the final expression
    def equalpress():
        # Try and except statement is used
        # for handling the errors like zero
        # division error etc.

        # Put that code inside the try block
        # which may generate the error
        try:

            global expression

            # eval function evaluate the expression
            # and str function convert the result
            # into string
            total = str(eval(expression))

            equation.set(total)

            # initialize the expression variable
            # by empty string
            expression = ""

        # if error is generate then handle
        # by the except block
        except:

            equation.set(" error ")
            expression = ""

    # Function to clear the contents
    # of text entry box

    def clear():
        global expression
        expression = ""
        equation.set("")

    # Driver code

    # create a GUI window
    gui = Toplevel(root)

    # set the background colour of GUI window
    gui.configure(background="black")

    # set the title of GUI window
    gui.title("HolyCalc")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation, font=('Arial', 10, 'bold'), bg='white', fg='black')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='white', bg='black',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='white', bg='black',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='white', bg='black',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='white', bg='black',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='white', bg='black',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='white', bg='black',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='white', bg='black',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='white', bg='black',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='white', bg='black',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='white', bg='black',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='cadet blue',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='cadet blue',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='cadet blue',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='cadet blue',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='snow',
                   command=equalpress, height=1, width=7)
    equal.grid(row=6, column=3)

    clear = Button(gui, text='Clear', fg='black', bg='cadet blue',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column=1)

    decimal = Button(gui, text='.', fg='black', bg='cadet blue',
                     command=lambda: press('.'), height=1, width=7)
    decimal.grid(row=5, column=2)
    # start the GUI
    gui.mainloop()

######
#######################################################################################################################
#######################################################################################################################
#####

b1 = Button(root, width='10', height='1', bg='white', fg='black', text='SAVE FILE', command=save_file).place(x=140, y=5)
b2 = Button(root, width='10', height='1', bg='white', fg='black', text='OPEN', command=open_file).place(x=420, y=5)
b3 = Button(root, width='5', height='1', bg='black', fg='green', text='CALC', command=open_calc).place(x=590, y=20)
B4 = Button(root, width='5', height='1', bg='black', fg='green', text='TALK', command=speak).place(x=5, y=20)

entry = Text(root, height='26.5', width=58, background='black', wrap=WORD, font='Arial 15', fg='green')
entry.config(insertbackground="white")
entry.place(x=0.5, y=50)

######
##################################################################################################################
######




clock = Label(root, font=('Arial', 15), background="black", foreground="green")
clock.pack(anchor="n")
get_time()

#################
# use transparency level 0.1 to 1.0 (no transparency)
root.attributes("-alpha", 0.88,)

#################

root.mainloop()
