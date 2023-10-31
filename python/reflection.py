text = input("Enter the text: ")
print(' '.join(word[::-1] if not word.isspace() else word for word in text.split()))
