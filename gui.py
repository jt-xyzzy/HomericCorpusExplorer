# I wanted to add a little bit of graphical interface to my project so I added this.
from tkinter import *
from explorers import demo
import os

def theme():
    cmd = "aplay \"8-bit.wav\""
    os.system(cmd)

def sneks():
    root  =  Tk()  # create root window
    root.title("Homeric Corpus Explorer")
    root.minsize(950, 300)  # width x height, this should work for most modern screens as of 2024
    root.config(bg="skyblue")

    # Create left and right frames
    make_frame  =  Frame(root,  width=1000,  height=1000,  bg='grey')
    make_frame.grid(row=0,  column=0,  padx=10,  pady=5)

    image  =  PhotoImage(file="sneklogo.ppm")  # edit the file name to use a different image

    Label(make_frame,  image=image).grid(row=1,  column=0,  padx=5,  pady=5)

    tool_bar  =  Frame(make_frame,  bg='grey')
    tool_bar.grid(row=2,  column=0,  padx=5,  pady=5)

    Label(tool_bar, text="The Project",font=('Helvetica', 18)).grid(row=1,  column=0,  padx=5,  pady=5, sticky='w'+'e'+'n'+'s')
    Label(tool_bar, text="""The Homeric Corpus Explorer was created by JT as an assignment for ARST559C.\nIt includes a small corpus of five texts, all English translations of Homer's Odyssey,\nand provides tools for comparative textual analysis. The Explorer is special in that it\ndoes textual analysis outside a Jupyter Notebook, relying on terminal outputs instead in\norder to provide a simpler and less buggy interface.
    """,font=('Helvetica', 14)).grid(row=2,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
    # Button for closing
    #
    Button(tool_bar,  text="Start Programme",  command=demo).grid(row=3,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s') # Spelling a reference to the BBC "Computer Programme" that ran in the 1980s. Runs the bigram "as when" demo program

    Button(tool_bar,  text="EXIT",  command=root.destroy).grid(row=4,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s') # destroys the window without killing the program.

    root.mainloop()
