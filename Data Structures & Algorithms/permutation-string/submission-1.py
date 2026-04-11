class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        table= defaultdict(int)
        for i in range(len(s1)):
            table[s1[i]]+=1
        r=0
        table2= defaultdict(int)

        for l in range(len(s2)):
            table2.clear()
            if s2[l] in table:
                r=l
                for j in range(len(s1)):
                    if r>=len(s2):
                        break
                    if s2[r] in table:
                        table2[s2[r]]+=1
                        r+=1
            if table2==table:
                return True
        return False