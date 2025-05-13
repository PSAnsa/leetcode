class Solution(object):
    def lengthAfterTransformations(self, s, t):
        count = [0] * 26
        n, mod = len(s), int(1e9 + 7)
        for i in range(n):
            count[ord(s[i]) - ord('a')] += 1
        for _ in range(t):
            temp_count = [0] * 26
            temp_count[0] = count[25]
            temp_count[1] = count[25]
            for index in range(25):
                temp_count[index + 1] += count[index] % mod
            count = temp_count
        ans = 0
        for index in range(26):
            ans += count[index] % mod
        return ans % mod
        # s = list(s)
        # while(t>0):
        #     news= ""
        #     for j in range(len(s)):
        #         if s[j] == 'z':
        #             news+="ab"
        #         else:
        #             news+=chr(ord(s[j]) + 1)
        #     s = news
        #     t-=1
        # return len("".join(s))
        