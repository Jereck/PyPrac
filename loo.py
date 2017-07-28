print("Print out the letters of your name!")
name = input("Enter your name: ")
for character in name:
	print(character)
print("=" * 50)

print("Or you can loop through a list, dict, or tuple of names!")
print("List: ")
characters_list = ["Mike", "Jim", "Dwight", "Pam", "Ryan"]
for person in characters_list:
	print("- "+ person)
print("Tuple: ")
character_tuple = ("Charlie", "Dennis", "Mac", "Frank", "Dee")
for person in character_tuple:
	print("- " + person)
print("Dictionary: ")
character_dict = {"Kelly": "Always Sunny", "Scott": "The Office", "Halpert": "The Office"}
for character in character_dict:
	print("- " + character)