def is_unique(string):
	j = 0
	for letter in string:
		for j in range(string.index(letter)+1, len(string)):
			if letter == string[j]:
				return False
	return True

print(is_unique("cat"))
print(is_unique("catch"))
print(is_unique("wwwwwww"))
print(is_unique("qwerty"))
