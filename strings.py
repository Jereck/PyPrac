#Create a array of words
words = ["I", "love", "the", "Python", "language."]
sentence_one = "".join(words)
print("\nThis is the sentence joined with no spaces")
print(sentence_one)
print("-" * 50)

sentence_two = " ".join(words)
print("\nThis is the sentence joined with spaces")
print(sentence_two)
print("-" * 50)

dogs = "\nDogs are the best kind of animals!"
print(dogs)
print("You can also replace letters in sentences!")
dogs = dogs.replace("a", "@")
print(dogs)