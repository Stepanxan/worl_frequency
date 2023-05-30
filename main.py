import string

def word_frequency(paragraph):
    frequency = {}
    translator = str.maketrans("", "", string.punctuation)

    for sentence in paragraph:
        words = sentence.lower().split()
        for word in words:
            word = word.strip().translate(translator)
            if word != "":
                frequency[word] = frequency.get(word, 0) + 1

    return frequency


paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]

frequency = word_frequency(paragraph)
print(frequency)


