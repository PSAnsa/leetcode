class Solution(object):
    def pushDominoes(self, dominoes):
        # creating consistent force boundaries at the start and end, allowing uniform           processing of all standing domino segments without special edge case handling. 
        s = 'L'+ dominoes + 'R'
        prev = 0
        res = ''
        for curr in range(1, len(s)):
            #domino is standing , skip
            if s[curr] == ".":
                continue
            #calculating the standing dominos between prev and current
            span = curr - prev -1
            if prev > 0:
                res += s[prev]
            if s[prev] == s[curr]:
                res += s[prev] * span
            elif s[prev] == "L" and s[curr] == 'R':
                res  += '.' *  span
            else:#s[prev] == "R" and s[curr] == 'L': 5 will get affected, left = 2 , right = 2 and standing 1
                res += 'R' * (span // 2) + '.' * (span % 2) + 'L' * (span // 2)
            prev = curr
        return res
 
        