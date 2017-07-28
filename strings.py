#Create a array of words
words = ["I", "love", "the", "Python", "language."]
sentence_one = "".join(words)
print("\nThis is the sentence joined with no spaces")
print(sentence_one)
print("=" * 50)

sentence_two = " ".join(words)
print("\nThis is the sentence joined with spaces")
print(sentence_two)
print("=" * 50)

dogs = "\nDogs are the best kind of animals!"
print(dogs)
print("You can also replace letters in sentences!")
dogs = dogs.replace("a", "@")
print(dogs)
print("=" * 50)

print("You can sometimes split a string")
original_string = "This is the original string!"
print("Original String: " + original_string)
split_string = original_string[6:]
print("Split String: " + split_string)
rev_string = original_string[::-1]
print("Reversed String: " + rev_string)