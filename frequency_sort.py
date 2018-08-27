from collections import defaultdict

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequencies = defaultdict(int)
        for letter in s:
            frequencies[letter] += 1

        printout = ''
        while len(frequencies.items()) > 0:
            max_count = max(frequencies.values())
            key = [key for key, value in frequencies.items() if value == max_count]
            letter = key[0]
            frequencies.pop(key[0])
            for i in range(0, max_count):
                printout += letter
        return printout
