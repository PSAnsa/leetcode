class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        count = [0] * 100
        result = 0

        for a, b in dominoes:
            key = 10 * min(a, b) + max(a, b)
            result += count[key]
            count[key] += 1

        return result
