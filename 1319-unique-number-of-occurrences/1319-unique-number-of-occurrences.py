class Solution(object):
    def uniqueOccurrences(self, arr):
        result = {}#hashset
        for num in arr:
            if num in result:
                result[num]  += 1
            else:
                result[num] = result.get(num,0)+1         

        return len(result.values()) == len(set(result.values()))
        
        