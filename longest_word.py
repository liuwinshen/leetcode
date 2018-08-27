def longest_word(s, d):
    lengths = [(entry, len(entry)) for entry in d]
    sorted_d = sorted(lengths, key = lambda x: (-x[1], x[0]))

    for word, length in sorted_d:
        j = 0
        for i in range(0, len(s)):
            if j < len(word) and word[j] == s[i]:
                j += 1
            if j == len(word):
                return word
    return ''

print(longest_word("abpcplea", ["a", "b", "c"]))
print(longest_word("abpcplea", ["ba", "ab", "a", "b"]))
print(longest_word('abpcplea', ["ale","apple","monkey","plea"]))
