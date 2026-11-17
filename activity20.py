from getpass import getpass

islogin = False

while islogin == False:
    username = input("Username: ---> ")
    password = getpass("Password: ---> ")

    if username == "naparabang" and password == "Bini":
        print("access granted")
        islogin = True
    else:
        print("Incorrect")