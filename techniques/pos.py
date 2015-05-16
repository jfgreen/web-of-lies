import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn
import itertools as IT
from itertools import product

def compare(word1, word2):
    ss1 = wn.synsets(word1)
    ss2 = wn.synsets(word2)
    return max(s1.path_similarity(s2) for (s1, s2) in product(ss1, ss2))
    
def compare(word1, word2):
    ss1 = wn.synsets(word1)
    ss2 = wn.synsets(word2)
    num_syns = 0
    for s1 in ss1:
        num_syns = num_syns + 1
    for s2 in ss2:
        num_syns = num_syns + 1
    cumulative_similarity = 0
    for s1 in ss1:
        for s2 in ss2:
            path_similarity = s1.path_similarity(s2)
            if isinstance(path_similarity, (int, long, float, complex)):
                cumulative_similarity = cumulative_similarity + s1.path_similarity(s2)
    similarity = cumulative_similarity/num_syns
    return similarity


threshold = 0.2
word = 'crazy'
synsets = wn.synsets(word)
curr_threshold = 1.0
def get_word_meets_threshold(word, synsets, threshold):
    for synset in synsets:
        synonyms = synset.lemma_names()
        synonyms = [synonym.replace('_', ' ') for synonym in synonyms]
        for curr_alt_word in synonyms:
            if compare(word, curr_alt_word) < threshold:
                return(curr_alt_word)
    return(word)




def pos_filter(text):
    POS = "NN"
    threshold = 0.5
    output = []
    input_list = text.split(" ")
    for i in range(0, len(input_list)):
        word = input_list[i]
        tokenized_text = word_tokenize(text)
        try:
            word_POS = nltk.pos_tag(tokenized_text[i:i+1])
        except:
            pass
        try:
            if word_POS[0][1] == POS:
                #new_word = get_word_meets_threshold(word, wn.synsets(word), threshold)
                #output.append(str(new_word))
                #print new_word
                synset = wn.synsets(word)[0]
                synonyms = synset.lemma_names()
                synonyms = [synonym.replace('_', ' ') for synonym in synonyms]
                #print ', '.join(synonyms)
                print synonyms[-1]
                output.append(str(synonyms[-1]))
            else:
                output.append(word)
        except:
            output.append(word)
    print
    print
    print text
    print output
    return " ".join(output)
