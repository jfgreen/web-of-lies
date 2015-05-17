from pymarkovchain import MarkovChain
import random

corpus_data = [
    "corpus/time_machine",
    "corpus/pride",
    "corpus/people",
    "corpus/art",
]

mc = MarkovChain("./markov")
for path in corpus_data:
    sources = []
    with open(path) as f:
        sources.append(f.read())
    mc.generateDatabase("\n".join(sources))


hints = [
    "of",
    "was",
    "the",
    "in",
    "is"
    "and",
    "to",
    "from",
    "the",
    "with",
]

skip_min = 2
skip_max = 5

max_per_iter = 3

def markov_replace(text, juice):
    print juice
    while juice > 0:
        if juice > max_per_iter:
            text = multi_markov_replace(text, max_per_iter)
            juice -= max_per_iter
        else:
            text = multi_markov_replace(text, juice)
            juice = 0
    return text


def multi_markov_replace(text, max_replaces):
    output = []
    #tokenised = word_tokenize(text)
    tokenised = text.split()

    # Find some good points to inject.
    replaced = 0
    still_replacing = True
    replace_points = []
    while replaced < max_replaces and still_replacing:
        random.shuffle(hints)
        found = False
        for h in hints:
            indexes = [i for i, x in enumerate(tokenised) if x == h and i not in replace_points]
            random.shuffle(indexes)
            if len(indexes) > 0:
                replace_points.append(indexes[0])
                replaced += 1
                found = True
        still_replacing = found

    # Generate altered version
    i = 0
    output = []
    while i < len(tokenised):
        if i in replace_points:
            output.append(get_good_markov(tokenised[i]))
            skip_ahead = random.randint(skip_min, skip_max)
            i += skip_ahead
        else:
            output.append(tokenised[i])
            i += 1

    return " ".join(output)

ideal_min = 3
ideal_max = 10
bad_bits = ["(", ")", "_"]
max_attempts = 16
def get_good_markov(seed):
    i = 0
    while i < max_attempts:
        attempt = mc.generateStringWithSeed(seed)
        l = len(attempt)
        if l <= ideal_max and l >= ideal_min:
            if True not in [b in attempt for b in bad_bits]:
                return attempt
        i += 1

    # Give up and return any old chain.
    return mc.generateStringWithSeed(seed)
