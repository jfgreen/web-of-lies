import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn

# TODO
# Threshold percentage

def pos_filter(text, POS = "NN"):
    output = []
    input_list = text.split(" ")
    for i in range(0, len(input_list)):
        word = input_list[i]
        #print word
        word_POS = nltk.pos_tag(word_tokenize(text))[i]
        #print word_POS
        try:
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