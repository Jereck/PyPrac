def f(x=2):
	return x ** x

# 2 * 2
print(f())

# 4 * 4 * 4 * 4
print(f(4))

# First (2 * 2) = 4
# Then   4 * 4 * 4 * 4
print(f(f(2)))


def add_it (x, y = 10):
	return x + y

result = add_it(2)
print(result)
# Setting y
result = add_it(2, 4)
print(result)