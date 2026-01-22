from nltk.util import bigrams


# The bigrammer finds a bigram and prints the line where it appears. It is more complex then a simple bigram search which would return only the number of times the bigram turned up in the text.
def bigrammer(u,v,text):
    # text = gen_raw(raw)
    text = text.lower()
    text = text.splitlines()

    lines =	[]
    for string in text: # make a list of strings.
        lines.append(string)


    bigramlist = []

    x = 0
    # AS WHEN AS WHEN
    for line in lines:
        wordlist = [] # prep wordlist
        x += 1
        line_split = line.split()
        for word in line_split:
            wordlist.append(word)
            bigramlist = list(bigrams(wordlist))

        for gram in bigramlist:
            if gram[0] == u and gram[1] == v: # add it if it matches the required words
                mystring = (str(line))
                print(x, mystring)
            else:
                continue
