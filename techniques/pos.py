import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn
import random 
import numpy # speeds up nltk

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
    
def pos_filter(text, threshold_percentage, NN):
    threshold_percentage = threshold_percentage/100.0
    output = []
    POS = "NN"
    input_list = text.split(" ")
    for i in range(0, len(input_list)):
        word = input_list[i]
        tokenized_text = word_tokenize(text)
        try:
            word_POS = nltk.pos_tag(tokenized_text[i:i+1])
        except:
            pass
        try:
            # Check pos, threshold
            if (((NN == True) and (POS in word_POS[0][1])) or ((NN == False) and (POS not in word_POS[0][1]))) and ((threshold_percentage > 0) and (random.random() < threshold_percentage)): 
                synset = wn.synsets(word)[0] # Get synonym sets
                synonyms = synset.lemma_names() # Get names for each set
                synonyms = [synonym.replace('_', ' ') for synonym in synonyms] 
                alt_word = synonyms[-1]
                if (alt_word != word[:-1]) and compare(alt_word, word) > 0.2: # Check that the selected synonym is not just removing an "s"
                    output.append(str(alt_word).lower())
                else:
                    output.append(word)
            else:
                output.append(word)
        except:
            output.append(word)
#     print
#     print
#     print text
#     print output
    return " ".join(output)

def noun_filter(text, threshold):
    return pos_filter(text, threshold, True)

def not_noun_filter(text, threshold):
    return pos_filter(text, threshold, False)
