def CountFreq(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    print(freq)


if __name__ == "__main__":
    s = input("Enter your string: ")
    CountFreq(s)
