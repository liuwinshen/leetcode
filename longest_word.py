def longest_word(s, d):
    lengths = [(entry, len(entry)) for entry in d]
    compare_d = sorted(lengths, key=lambda x: x[1], reverse = True)

    for word, length in compare_d:
        j = 0
        for i in range(0, len(s)):
            if word[j] == s[i]:
                j += 1
            if j == len(word)-1:
                return word
    return ''

print(longest_word('abpcplea', ["ale","apple","monkey","plea"]))
