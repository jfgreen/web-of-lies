from random import randint


def adjust_numbers(text):
    output = []
    for word in text.split(" "):
        print word
        try:
            x = int(word)
            x += randint(-x / 2, x / 2)
            output.append(str(x))
        except:
            output.append(word)
    print output
    return " ".join(output)


if __name__ == "__main__":
    print adjust_numbers("Foo bar 9000 is king.")
