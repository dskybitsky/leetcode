class Solution:
    def predictPartyVictory(self, senate: str, d_votes: int = 0, r_votes: int = 0) -> str:
        next_senate = ""

        has_d = False
        has_r = False

        for senator in senate:
            if senator == "D":
                has_d = True
                
                if r_votes > 0:
                    r_votes -= 1
                else:
                    d_votes += 1
                    next_senate += senator

            if senator == "R":
                has_r = True

                if d_votes > 0:
                    d_votes -= 1
                else:
                    r_votes += 1
                    next_senate += senator
        
        if not has_d:
            return "Radiant"
        
        if not has_r:
            return "Dire"

        return self.predictPartyVictory(next_senate, d_votes, r_votes)
    

if __name__ == "__main__":
    sol = Solution()

    assert sol.predictPartyVictory("RD") == "Radiant"
    assert sol.predictPartyVictory("RDD") == "Dire"
    assert sol.predictPartyVictory("DDRRR") == "Dire"