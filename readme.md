# README FOR THE HOMERIC CORPUS EXPLORER

Prerequisites: TK/Tkinter

## QUICKSTART

Download the project zip and Extract it.

Open a new terminal window and navigate to the folder where you have extracted it.

Create and activate a virtual environment and then install nltk:

python -m venv venv
source venv/bin/activate
pip install nltk

and then: 

python # to enter interactive mode
import nltk
nltk.download('all')



## TROUBLESHOOTING

If you are having problems, make sure your virtual environment is active, your Python version is up to date, and that you have installed nltk via pip.

## GETTING HELP

Having a problem? Want to report a bug? Use this code for something cool and want to talk about it? Message me with the subject "SNAKES!" I might be able to help.

## About the Project
The Homeric Corpus Explorer is a natural language processing tool for exploring English language translations of Homer's Odyssey (although if you decide to use this code and adapt it to something else, I'd love to hear about it).

The Explorer is special in that it does textual analysis outside a Jupyter Notebook, relying instead on terminal outputs that can be easily saved and viewed without installing any specialised software (like Anaconda or jupyter) on your system.

The goal of the project is to facilitate my own research into the history of English Translations of the Odyssey, explore new ways of enjoying text in translation, and educate humanists on ways in which programming can be applicable, and possibly even fun, in their work.

## ARST559 NOTES / Q&A

The program was developed as part of ARST559C and as such has a number of constraints. Importantly, the largest constraint is that I am a beginner and am still learning all the things that Python has to offer.

### Why no classes?
I'm a newb lol.

### Why doesn't this program run on Windows?
See question #1. Plus I confirmed that my teacher and TA both use MAC / Linux so that meant I didn't need to worry about converting.

### Why do you have a database but only use it once?
The database was a component requested by my teacher, but wasn't really relevant to a project with only five pieces of data (the five texts) so I just used it to store some links.

### Why don't you use regex?
I'm using the NLTK which does the regex behind the scenes. I found adding my own on top could cause problems (+I'm a newb.)

### Why do your scripts have weird names like "setupr"
I haven't memorised all the things you can't name stuff, so I erred on the side of adding "s" or "r" at the end of words.

### Why didn't you implement feedback from checkpoint 2 and the final assignment?
I either never received feedback or it was never released to me.

### Why does your logger only save what tools you used and not their outputs?
I had difficulty navigating what datatype I needed in order to write to the file and kept getting nonetype errors, so I'm leaving that for a future iteration of the project.

### How did your project change based on feedback from the class?
1. I set up my menu so users can select tools by number and not name.
2. I made each tool run comparative analysis rather than running them one at a time.
3. I focussed on contextual tools rather than frequency comparisons
