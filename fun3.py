# These are lists
print("This is the first list of fruit...")
fruit = ['apple', 'orange', 'pear']
print (fruit)
print('-' * 50)

# Adding fruit to our list
print("This list has a few added fruits from .append()")
fruit.append("banana")
fruit.append("peach")
print (fruit)
print('-' * 50)

print("Lists of mutable... you can change list items!")
fruit[1] = "kiwi"
print (fruit)
print('-' * 50)

print ("You can .pop() off the last item in a list...")
print (fruit)
last_item = fruit.pop()
print(last_item)
print('-' * 50)

print ("You can also find out if something is IN a list and return a bool")
print ("So if 'Apple' is in the fruit list, it will return True")
if "Apple" in fruit:
	print ("True")
else:
	print ("Apple was not in Fruit[]")
print('-' * 50)

print("You can also use input to see if anything is in a list: ")
guess = input("Guess a fruit: ").lower()
if guess in fruit:
	print("You guessed correctly!")
else:
	print("You guessed wrong!")