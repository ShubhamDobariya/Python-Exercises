def countFreq(sentence):
    freq = {}

    for ch in sentence:
        freq[ch] = freq.get(ch, 0) + 1

    print(freq)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    countFreq(sentence)
