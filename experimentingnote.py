import pyttsx3
from tkinter import *
from tkinter import filedialog
from tkinter import font
from time import strftime
import threading
import wikipedia as wiki
import customtkinter
import nltk
from nltk.corpus import wordnet


customtkinter.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light"
#customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

btncolor1 = 'darkorchid'

# Set the variable that grabs filename ( to make the save... function)
global open_file_name
open_file_name = False


def new_file():
    entry.delete("1.0", END)
    root.title("New       ")
    status_bar.configure(text='Created: New file       ')

    global open_file_name
    open_file_name = False


def open_file():
    entry.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open File", initialdir='C:/Users/mfran/Documents/DESKTOP/',
                                           filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"),
                                                      ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        global open_file_name
        open_file_name = text_file

    # Update Status Bars:
    name = text_file
    status_bar.configure(text=f'Opened file: {name}       ')
    name = name.replace("C:/Users/mfran/Documents/DESKTOP/", "")
    root.title(f'{name}     ')

    # Open the Text File:
    text_file = open(text_file, 'r', encoding='utf-8')
    stuff = text_file.read()
    entry.insert(END, stuff)
    text_file.close()


def save_file():
    text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir='C:/Users/mfran/Documents/DESKTOP/',
                                             title="Save File",
                                             filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"),
                                                        ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Updating the status bar and title
        name = text_file
        status_bar.configure(text=f'Saved file: {name}')
        name = name.replace("C:/Users/mfran/Documents/DESKTOP/", "")
        root.title(f'{name}       ')
        # Save file
        text_file = open(text_file, 'w')
        text_file.write(entry.get(1.0, END))
        text_file.close()
        global open_file_name
        open_file_name = text_file


def save():
    global open_file_name

    if open_file_name:

        text_file = open(open_file_name, 'w')
        text_file.write(entry.get(1.0, END))
        text_file.close()
        status_bar.configure(text=f'Saved file: {open_file_name}')
        name = open_file_name
        name = name.replace("C:/Users/mfran/Documents/DESKTOP/", "")
        root.title(f'{name}')


    else:
        save_file()


def websteros():
    global selected
    if entry.selection_get():
        selected = entry.selection_get()

    syn = wordnet.synsets(selected)
    defin = syn[0].definition()  # print definition

    synonyms = []
    for syn in wordnet.synsets(selected):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    #print(synonyms)  # print synonyms

    antonyms = []
    for syn in wordnet.synsets(selected):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    #print(antonyms)  # print antonyms

    entry.insert(END, "\n\n")
    status_bar.configure(text='Dictionary entries for highlited text')

    # output entries to textbox

    entry.insert(END, f"DEFINITION: {defin}\n\nSYNONYMS: {synonyms}\n\nANTONYMS: {antonyms}")



def wiki_sum():
    global selected
    if entry.selection_get():
        selected = entry.selection_get()
        data = wiki.summary(f'\'{selected}\'', sentences=35)
        entry.insert(END, "\n\n")
        status_bar.configure(text='Highlighted text searched on Wikipedia')
        # output wikipedia to textbox
        entry.insert(END, data)
    else:
        test = wiki.suggest
        entry.insert(END, test)


# A CLOCK:
def get_time():
    string = strftime('%H:%M:%S %p')
    clock.configure(text=string)
    clock.after(1000, get_time)


def speak():
    speaker = pyttsx3.init()
    status_bar.configure(text=f'Activated: speak command       ')
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    textcontent = entry.get(1.0, END)
    speaker.say(textcontent)
    threading.Thread(target=speaker.runAndWait).start()


def bold_it():
    bold_font = font.Font(entry, entry.cget("font"))
    bold_font.configure(weight="bold")

    entry.tag_configure("bold", font=bold_font)

    current_tags = entry.tag_names("sel.first")

    if "bold" in current_tags:
        entry.tag_remove("bold", "sel.first", "sel.last")
    else:
        entry.tag_add("bold", "sel.first", "sel.last")


def italics_it():
    italics_font = font.Font(entry, entry.cget("font"))
    italics_font.configure(slant="italic")

    entry.tag_configure("italic", font=italics_font)

    current_tags = entry.tag_names("sel.first")

    if "italic" in current_tags:
        entry.tag_remove("italic", "sel.first", "sel.last")
    else:
        entry.tag_add("italic", "sel.first", "sel.last")


# A CALCULATOR:
def open_calc():
    global expression
    # globally declare the expression variable
    expression = ""
    status_bar.configure(text=f'Opened: HolyCalc       ')

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

root = customtkinter.CTk()
root.geometry("640x640")
root.title("Note")
icon = PhotoImage(file='C:\\Users\\mfran\\PycharmProjects\\NotepadTTS\\pngkeys2.png')
root.iconphoto(True, icon)
root.configure(bg='black')
root.resizable(True, True)
root.attributes("-alpha", 0.88, )  # Transparency level up to 1.0
# -----------------------------------------------------------------------------------------------------------------------
#                                                  FRAMING BUTTONS:
button_frame = customtkinter.CTkFrame(root, background="black")
button_frame.pack()
#
# BUTTONS:
B4 = customtkinter.CTkButton(button_frame, text_color='black', text='SPEAK',
                             command=speak)
B4.pack(side="left")

B3 = customtkinter.CTkButton(button_frame, text_color='black', text='DICTIONARY',
                             command=websteros)
B3.pack(side="left")

B1 = customtkinter.CTkButton(button_frame, text_color='black', text='WIKIPEDIA',
                             command=wiki_sum)
B1.pack(side="left")

#
# -----------------------------------------------------------------------------------------------------------------------
# Digital CLOCK pack:
clock = customtkinter.CTkLabel(button_frame, text_color=btncolor1, fg_color='black')
clock.pack(side="left")
threading.Thread(target=get_time).start()

# FRAME for the entry text:
my_frame = customtkinter.CTkFrame(root)
my_frame.pack(expand=1, fill='both')

# Y-scrollbar for text-frame
text_scroll = customtkinter.CTkScrollbar(my_frame)
text_scroll.pack(side="right", fill='y')

# ENTRY TEXT
entry = Text(my_frame, background='black', wrap=WORD, insertbackground="white", font='Arial 15',
             fg='white', undo=True, selectforeground="black", selectbackground="yellow", yscrollcommand=text_scroll.set)

entry.pack(expand=1, fill='both')

# Configure SCROLLBAR:
text_scroll.configure(command=entry.yview)

###############################################################
#                         MENU:                               #
###############################################################
# MENU FRAME & CONFIG:
menu_frame = Frame(root)
menu_frame.pack()

my_menu = Menu(menu_frame)
root.configure(menu=my_menu)

# Add File --- Menu:
file_menu = Menu(my_menu, tearoff=False, bg="black", fg="snow")
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save As...", command=save_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Clear", command=lambda: entry.delete(1.0, END))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
# --------------------------------------------------------------
# Edit --- Menu:
edit_menu = Menu(my_menu, tearoff=False, bg="black", fg="snow")
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Bold", command=bold_it)
edit_menu.add_command(label="Italic", command=italics_it)
# edit_menu.add_command(label="Copy")
# edit_menu.add_command(label="Paste")
# edit_menu.add_command(label="Redo")
# --------------------------------------------------------------
# Tools  --- Menu:
# Edit --- Menu:
tools_menu = Menu(my_menu, tearoff=False, bg="black", fg="snow")
my_menu.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Calculator", command=open_calc)

# --------------------------------------------------------------
###############################################################

###############################################################
# Status Bar at the bottom:
status_bar = customtkinter.CTkLabel(root, text=f'       ', anchor=E)
status_bar.configure(background="black", foreground="snow")
status_bar.pack(fill='x', side=BOTTOM, ipady=0)

root.mainloop()
