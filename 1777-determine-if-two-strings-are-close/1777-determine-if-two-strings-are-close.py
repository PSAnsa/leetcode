class Solution(object):
    def closeStrings(self, word1, word2):
        frequency_word1 = Counter(word1)
        frequency_word2 = Counter(word2)
        sorted_value1 = sorted(frequency_word1.values())
        sorted_value2  =  sorted(frequency_word2.values())
        keys_match = set(frequency_word1.keys()) == set(frequency_word2.keys())
        return sorted_value1 == sorted_value2 and keys_match