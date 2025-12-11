username = input("username kiriting: ")

matn = username.replace("-", "")

if matn.isalpha():
    print('True')
else:
    print('False')
