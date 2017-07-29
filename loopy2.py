questions = ["What is your name? ", "What is your profession? ", "How old are you? ", "What is your quest? "]
i = 0
print("Type q to quit")
while True:
	a = input(questions[i])
	if a == "q":
		break
	i = (i + 1) % 3

