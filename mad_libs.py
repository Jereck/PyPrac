noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective1 = input("Enter an adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")

sentence = """The {} dog ran around the {} and began to {} the cat.
It scared the {} which began to {}.""".format(adjective1, noun1, verb1, noun2, verb2)

print(sentence)