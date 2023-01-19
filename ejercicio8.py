def is_integer(word):
    patterns = "^[-+]?[1-9][\s\d]*$"
    if re.search(patterns,word):
        return "True"
    else:
        return "False"
word = input("Enter word:")
print(is_integer(word))
