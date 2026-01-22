import nltk
from nltk import word_tokenize


# Open the text files and work with them as raw text, ntlk tokens, nltk text, etc.

# This function creates a line break. I've phased it out in most places.'
def br():
    print("")

def cont():
    userIO = input("... ")
    for i in userIO:
        if i == "exit":
            exit()
        else:
            continue

def gen_raw(txt):
    myfile = open(txt,"r") #opened as _io.TextIOWrapper

    raw = myfile.read() # read in as str
    myfile.close()

    return raw

def gen_lines(txt):
    myfile = open(txt,"r") #opened as _io.TextIOWrapper
    raw = myfile.read() # read in as str
    line_tokens = raw.split("\n")
    myfile.close()
    return line_tokens


def gen_tokens(txt):
    myfile = open(txt,"r") #opened as _io.TextIOWrapper
    raw = myfile.read() # read in as str
    tokens = word_tokenize(raw) # tokenized as a list
    return tokens


def gen_text(txt):
    myfile = open(txt,"r") #opened as _io.TextIOWrapper
    raw = myfile.read() # read in as str
    tokens = word_tokenize(raw) # tokenized as a list
    text= nltk.Text(tokens) # converted into a nltk.text.Text
    myfile.close()

    return text
