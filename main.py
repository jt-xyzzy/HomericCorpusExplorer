
from sqls import tiny_database
import os
from gui import theme, sneks
from explorers import concordances,vocab, bigramsearch,collocations, wordsearch, text_sample,sample_words,demo

import datetime

os.system("clear")

# SET UP DATE-TIME AND SAVE IT TO A FILE TO CREATE A LOG OF THE CURRENT SESSION
dt= datetime.datetime.now()
def timewrite(dt):
    sdate = dt.strftime("%Y")+"-"+ dt.strftime("%m")+"-"+dt.strftime("%d")
    stime = dt.strftime("%X")
    return sdate, stime

# CALL THE VARIABLE AND SAVE IT, ALONG WITH SOME HEADINGS.
x = timewrite(datetime.datetime.now())
with open("logger.txt", "a") as f: # this method of opening files means I don't need to close them later'
    f.write("")
with open("logger.txt", "a") as f:
    f.write("\n\n\n-------------------------------------------------------------\n# SESSION LOG\n")
with open("logger.txt", "a") as f:
    f.write("Session date: "+x[0]+"; Start time: " + x[1])
with open("logger.txt", "a") as f:
    f.write("\nDuring this session you used the following tools:\n\n")

#     Please ensure you have followed the nltk installation instructions and activated your virtual environment.


def menu():
    print("""
    WELCOME TO THE HOMERIC CORPUS EXPLORER

    HELP MENU
    [x]         EXIT PROGRAMME
    [menu]      RETURN TO THIS MENU
    [about]     ABOUT PROJECT.
    [texts]     ABOUT TEXTS
    [demo]      DEMONSTRATE AN "AS WHEN" BIGRAM.
    [log]       READ THE SESSION LOGS

    TOOLS MENU
    [0] WORD SAMPLE             Sample of unique words in the text.
    [1] TEXT SAMPLE             Sample text from each translation.
    [2] CONCORDANCE             Context of a given word within the text.
    [3] VOCAB COUNT             Frequency of a word within a text.
    [4] WORD SEARCH             Print the lines where a given word appears. Saveable.
    [5] BIGRAM SAMPLE           Sample of collocations, words that appear together.
    [6] BIGRAM SEARCH           For a given bigram, the lines where it appears.

        """)


menu()

myint = ""
while myint != "x": # My cyclomatic complexity is just fine thank you pyflake.

    myint = input("> ")
    if myint == "menu":
        menu()

    elif myint == "about":
        theme()
        sneks()

    elif myint == "log":
        with open("logger.txt", "r") as f:
            print(f.read())

    elif myint == "texts":
        print("PLEASE ENJOY THIS DEMONSTRATION OF MY SQL ABILITES\nLicense info for all texts available via source urls.\n\n")
        print("Name of translator, title of translation, publication date, source url, id")
        tiny_database()

    elif myint == "demo":
        demo()


# START IF THE EXPLORER TOOL SECTION, CALLED BY NUMBER
# each refers to something in the explorer.py file
# I haven't annotated these because their names are incldued'
#
    elif myint == "0":
        X = "WORD SAMPLE"
        print(X)
        with open("logger.txt", "a") as f:
            f.write(X)
        with open("logger.txt", "a") as f:
            f.write("\n")
        print(sample_words())

    elif myint == "1":
        X = "SELECTION: TEXT SAMPLE"
        print(X)
        with open("logger.txt", "a") as f:
            f.write(X)
        with open("logger.txt", "a") as f:
            f.write("\n")
        x = input("Start selection at [integer] > ")
        try:
            x = int(x) # My editor flags this as incorrect, but it runs anyhow.
            y = x + 200
            text_sample(x,y)
        except:
            print("Input not valid: Defaulting to 10:200")
            text_sample(10,200)

    elif myint == "2":
        X = "SELECTION: CONCORDANCE"
        print(X)
        with open("logger.txt", "a") as f:
            f.write(X)
        with open("logger.txt", "a") as f:
            f.write("\n")
        word = input("Enter word: ")
        print(concordances(word))

    elif myint == "3":
        X = "SELECTION: VOCAB COUNT"
        print(X)
        with open("logger.txt", "a") as f:
            f.write(X)
        with open("logger.txt", "a") as f:
            f.write("\n")
        word = input("Enter word: ")
        print(vocab(word))

    elif myint == "4":
        X = "SELECTION: WORD SEARCH"
        with open("logger.txt", "a") as f:
            f.write(X)
        with open("logger.txt", "a") as f:
            f.write("\n")
        print(X)
        word1 = input("Enter word: ")
        print(wordsearch(word1))

    elif myint == "5":
        X = "SELECTION: SAMPLE BIGRAMS / COLLOCATIONS"
        with open("logger.txt", "a") as f:
            f.write(X)
        with open("logger.txt", "a") as f:
            f.write("\n")
        print(X)
        print(collocations())

    elif myint == "6":
        X = "SELECTION: BIGRAM SEARCH"
        with open("logger.txt", "a") as f:
            f.write(X)
        with open("logger.txt", "a") as f:
            f.write("\n")
        print(X)
        word1 = input("Enter first word: ")
        word2 = input("Enter second word: ")
        print(bigramsearch(word1, word2))

    else:
        continue
