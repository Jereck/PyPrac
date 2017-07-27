first_name = input("What is your first name? ")
first_letter = first_name[0]

if first_letter.istitle():
	print ("Hello " + first_name + "!\n")
else:
	new_letter = first_letter.upper()
	new_name = new_letter + first_name[1:]
	print("Oops! You forgot to capitalize the first letter in your name, so we did it for you, " + new_name + ".")