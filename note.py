import pyttsx3
from tkinter import *
from tkinter import filedialog
from time import strftime
import threading


def new_file():
    entry.delete("1.0", END)
    root.title("New       ")
    status_bar.config(text='New File created       ')


def save_file():
    print("")
    text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir='C:/Users/mfran/Documents/DESKTOP/',
                                             title="Save File",
                                             filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"),
                                                        ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Updating the status bar and title
        name = text_file
        status_bar.config(text=f'Saved file: {name}')
        name = name.replace("C:/Users/mfran/Documents/DESKTOP/", "")
        root.title(f'{name}       ')
        # Save file
        text_file = open(text_file, 'w')
        text_file.write(entry.get(1.0, END))
        text_file.close()


def open_file():
    entry.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open File", initialdir='C:/Users/mfran/Documents/DESKTOP/',
                                           filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"),
                                                      ("Python Files", "*.py"), ("All Files", "*.*")))

    # Update Status Bars:
    name = text_file
    status_bar.config(text=f'Opened file: {name}       ')
    name = name.replace("C:/Users/mfran/Documents/DESKTOP/", "")
    root.title(f'{name}     ')

    # Open the Text File:
    text_file = open(text_file, 'r', encoding='utf-8')
    stuff = text_file.read()
    entry.insert(END, stuff)
    text_file.close()


# A CLOCK:
def get_time():
    string = strftime('%H:%M:%S %p')
    clock.config(text=string)
    clock.after(1000, get_time)


def speak():
    speaker = pyttsx3.init()
    status_bar.config(text=f'Activated speak command       ')
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    textcontent = entry.get(1.0, END)
    speaker.say(textcontent)
    threading.Thread(target=speaker.runAndWait).start()


# A WHOLE CALCULATOR:
def open_calc():
    global expression
    # globally declare the expression variable
    expression = ""
    status_bar.config(text=f'Opened: HolyCalc       ')
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


####################///#################///#################///#################///#################///#################
##                                                   THE GUI:                                                        ###
####################///#################///#################///#################///#################///#################

root = Tk()
root.geometry("640x640")
root.title("Note")
icon = PhotoImage(file='pngkeys2.png')
root.iconphoto(True, icon)
root.config(bg='black')
root.resizable(True, True)
root.attributes("-alpha", 0.88, )  # Transparency level up to 1.0
#-----------------------------------------------------------------------------------------------------------------------
#                                                  FRAMING BUTTONS:
button_frame = Frame(root, background="black")
button_frame.pack()
#
# BUTTONS:
B4 = Button(button_frame, width='10', height='1', bg='grey3', fg='green', text='SPEAK!',
            command=speak)
B4.pack(side="left")

B3 = Button(button_frame, width='12', height='1', bg='grey3', fg='green', text='CALCULATOR',
            command=open_calc)
B3.pack(side="left")

B1 = Button(button_frame, width='10', height='1', bg='grey3', fg='green', text='OPEN FILE',
            command=open_file)
B1.pack(side="left")

B2 = Button(button_frame, width='12', height='1', bg='grey3', fg='green', text='SAVE FILE',
            command=save_file)
B2.pack(side="left")
#
#-----------------------------------------------------------------------------------------------------------------------
# Digital CLOCK pack:
clock = Label(button_frame, font=('Arial', 15), background="black", foreground="green")
clock.pack(side="left")
get_time()

# FRAME for the entry text:
my_frame = Frame(root)
my_frame.pack(expand=1, fill='both')

# Y-scrollbar for text-frame
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side="right", fill='y')

# ENTRY TEXT
entry = Text(my_frame, background='black', wrap=WORD, insertbackground="white", font='Arial 15',
             fg='green', undo=True, selectforeground="black", selectbackground="yellow", yscrollcommand=text_scroll.set)

entry.pack(expand=1, fill='both')

# Configure SCROLLBAR:
text_scroll.config(command=entry.yview)

###############################################################
#                         MENU:                               #
###############################################################
# MENU FRAME & CONFIG:
menu_frame = Frame(root)
menu_frame.pack()

my_menu = Menu(menu_frame)
root.config(menu=my_menu)

# Add File --- Menu:
file_menu = Menu(my_menu, tearoff=False, bg="black", fg="snow")
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Save File", command=save_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
#--------------------------------------------------------------
# Edit --- Menu:
#edit_menu = Menu(my_menu, tearoff=False, bg="black", fg="snow")
#my_menu.add_cascade(label="Edit", menu=edit_menu)
#edit_menu.add_command(label="Cut")
#edit_menu.add_command(label="Copy")
#edit_menu.add_command(label="Paste")
#edit_menu.add_command(label="Redo")
#--------------------------------------------------------------
# Search Wikipedia --- Menu:

#--------------------------------------------------------------
###############################################################

###############################################################
# Status Bar at the bottom:
status_bar = Label(root, text=f'       ', anchor=E)
status_bar.config(background="black", foreground="snow")
status_bar.pack(fill='x', side=BOTTOM, ipady=0)

root.mainloop()
