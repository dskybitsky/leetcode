class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        dist = 0

        while mainTank >= 5:
            dist += 50
            mainTank -= 5

            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
        
        dist += mainTank * 10

        return dist


sol = Solution()

assert sol.distanceTraveled(mainTank = 9, additionalTank = 2) == 110
assert sol.distanceTraveled(mainTank = 5, additionalTank = 10) == 60
assert sol.distanceTraveled(mainTank = 1, additionalTank = 2) == 10