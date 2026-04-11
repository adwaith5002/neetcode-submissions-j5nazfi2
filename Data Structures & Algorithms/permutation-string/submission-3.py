class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        table1= defaultdict(int)
        table2= defaultdict(int)
        for i in range(len(s1)):
            table1[ord(s1[i])-ord('a')]+=1
            table2[ord(s2[i])-ord('a')]+=1
        matches=0
        for i in range(26):
            if table1[i]==table2[i]:
                matches+=1
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            index=ord(s2[r])-ord('a')
            table2[index]+=1
            if table1[index]==table2[index]:
                matches+=1
            elif table1[index]+1==table2[index]:
                matches-=1
            
            index2=ord(s2[l])-ord('a')

            table2[index2]-=1
            if table1[index2]==table2[index2]:
                matches+=1
            elif table1[index2]-1==table2[index2]:
                matches-=1
            l+=1
        return matches==26