class Solution(object):
    def largestAltitude(self, gain):
        maxaltitude = 0
        altitude = 0
        for i in range(len(gain)):
            altitude += gain[i] 
            maxaltitude = max(maxaltitude, altitude)
        return maxaltitude  