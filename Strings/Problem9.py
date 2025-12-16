def FirstOccurrence(str, word):
    index = str.find(word)
    print(index)


if __name__ == "__main__":
    str = "I developed machine learning project"
    word = "machine"

    FirstOccurrence(str, word)
