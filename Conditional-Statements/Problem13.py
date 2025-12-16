spam_keyword = ["free", "win", "click", "subscribe", "buy now", "offer"]

comment = input("Enter Your Commnt : ").lower()

print(comment)

comment_keyword = comment.split()

is_keyword = False
for keyword in comment_keyword:
    if keyword in spam_keyword:
        is_keyword = True
        break


if is_keyword == True:
    print("Comment is Spam")
else:
    print("Comment is not Spam")
