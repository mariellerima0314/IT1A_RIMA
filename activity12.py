import getpass

username = 'capisces'
password = 'ceszrielle0103'

u = input("Enter Username ---->    ")
p = getpass.getpass("Enter Password ---->    ")

if username == u and password == p :
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED") 