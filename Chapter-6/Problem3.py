comment = input("Enter comment : ")

text = comment.lower()

is_spam = False

if "make a lot of money" == text:
    is_spam = True
elif "buy now" == text:
    is_spam = True
elif "subscribe this" == text:
    is_spam = True
elif "click this" == text:
    is_spam = True


if is_spam == True:
    print("comment is spam!")
else:
    print("comment is not spam!")
