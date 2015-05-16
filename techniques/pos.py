import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn
import itertools as IT
from itertools import product

def compare(word1, word2):
    ss1 = wn.synsets(word1)
    ss2 = wn.synsets(word2)
    return max(s1.path_similarity(s2) for (s1, s2) in product(ss1, ss2))
#compare('hi', 'hello')

# TODO
# Threshold percentage

def pos_filter(text):
    POS = "NNS"
    output = []
    input_list = text.split(" ")
    for i in range(0, len(input_list)):
        word = input_list[i]
        #print word
        try:
            word_POS = nltk.pos_tag(word_tokenize(text))[i]
            #print word_POS
            if word_POS[1] == POS:
                synset = wn.synsets(word)[0]
                synonyms = synset.lemma_names()
                synonyms = [synonym.replace('_', ' ') for synonym in synonyms]
                #print ', '.join(synonyms)
                #print synonyms[-1]
                output.append(str(synonyms[-1]))
            else:
                output.append(word)
    
    #if word_POS[1] == "NN":
            #syn = wn.synsets(word)[0]
            #print ', '.join(syn.lemma_names())
    #try:
            #x = int(word)
            #x += randint(-x / 2, x / 2)
            #output.append(str(x))
        except:
            output.append(word)
    print text
    print output
    return " ".join(output)
