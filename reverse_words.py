def reverse_words(s):
    words = s.split()
    reversed_words = []
    while words:
        reversed_words.append(words.pop())
    return ' '.join(reversed_words)

print(reverse_words('the sky is blue'))
