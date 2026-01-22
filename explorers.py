from setupr import gen_raw, gen_text, gen_lines, gen_tokens, cont, br
# from setupr import gen_tokens, help
from bigrammer import bigrammer # I keep this script separate because it is fragile
from nltk.util import bigrams

# text0 = "[hom0.txt] Cowper's translation"
# text1 = "[hom1.txt] Pope's translation"
# text2 = "[hom2.txt] Chapman's translation"
# text3 = "[hom3.txt] Butcher and Lang's translation"
# text4 = "[hom4.txt] Butler's translation"


thisdict =	{
    "Chapman (1611)": "hom2.txt",
    "Pope (1712)": "hom1.txt",
    "Cowper (1791)": "hom0.txt",
    "Butcher & Lang (1879)": "hom3.txt",
    "Butler (1900)": "hom4.txt"
}

def concordances(word):
    print("CONCORDANCE FOR <",word,">", "(ARRANGED BY TEXT).")
    for m,n in thisdict.items():
        text = gen_text(n)
        print("****************************************************************\n",m)
        text.concordance(word)
        cont()

def text_sample(int1,int2): #range between two numbers
    br()
    for m,n in thisdict.items():
        text = gen_raw(n)
        print("****************************************************************\n",m)
        x=text[int1:int2]
        print(x)
        cont()

def vocab(word):
    print("INSTANCES OF THE WORD <",word,">", "(ARRANGED BY TEXT).")
    for m,n in thisdict.items():
        text = gen_text(n)
        print(m,":",text.vocab()[word])


def similar_words(word):
    print("WORDS THAT ARE DISTRIBUTIONALLY SIMILAR TO <",word,">", "(ARRANGED BY TEXT).")
    br()
    for m,n in thisdict.items():
        text = gen_text(n)
        print("********************************************************************************\n",m)
        text.similar(word)
        cont()

def bigramsearch(word1,word2):
    print("Lines with  <",word2,"> and <",word2,">","(ARRANGED BY TEXT).")
    for m,n in thisdict.items():
        text = gen_raw(n)
        print("********************************************************************************\n",m)
        print(bigrammer(word1,word2,text))
        cont()

def demo():
    bigramsearch("as","when")

def bigram_sample():
    print("SAMPLE OF BIGRAMS ARRANGED BY TEXT.")
    for m,n in thisdict.items():
        nltk_tokens = gen_tokens(n) # NLTK Tokens do not strip out stopwords
        print("****************************************************************\n",m)
        x = list(bigrams(nltk_tokens[30:60]))
        print(x)
        cont()


def collocations():
    print("SAMPLE OF BIGRAMS/COLLOCATIONS (ARRANGED BY TEXT).")
    br()
    for m,n in thisdict.items():
        text = gen_text(n)
        print("********************************************************************************\n",m)
        text.collocations()
        cont()

def wordsearch(word1):
    for m,n in thisdict.items():
        print("********************************************************************************\n",m)
        lines = gen_lines(n)
        x=0
        for line in lines:
            line_split = line.split()
            x += 1
            for word in line_split:
                if word ==word1:
                    print(x, line)

        cont()

#get a sample of the words in the text
def sample_words():
    for m,n in thisdict.items():
        text = gen_tokens(n)
        words = set(text)
        print("********************************************************************************\n",m)
        print(words)
        cont()
