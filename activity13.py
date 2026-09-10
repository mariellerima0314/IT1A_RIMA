#CONDITIONAL STATEMENT

name = input("Input NAME ---->	")
age = int(input("Input AGE ---->	"))

if age >= 1 and age <=5:
	print("INFANT")
elif age >= 6 and age <=5:
	print("KID")
elif age >= 13 and age <=19:
	print("TEENAGER")
elif age >= 20 and age <=29:
	print("EARLY_ADULTHOOD")
elif age >= 30 and age <=49:
	print("ADULT")
else:
	print("INVALID")
