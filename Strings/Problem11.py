def anagrams(str1, str2):
    if len(str1) != len(str2):
        print("No, Two strings are anagrams.")

    else:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(str1)):
            freq1[ord(str1[i]) - 97] += 1
            freq2[ord(str2[i]) - 97] += 1

        if freq1 == freq2:
            print("Yes, Two strings are anagrams.")
        else:
            print("No, Two strings are anagrams.")


if __name__ == "__main__":
    str1 = input("Enter your string 1 : ")
    str2 = input("Enter your string 2 : ")
    anagrams(str1, str2)
