class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        wanted={i:[] for i in range(numCourses)}
        res=[]
        path=set()
        visited=set()
        for i in range(len(prerequisites)):
            a,b =prerequisites[i]
            wanted[a].append(b)
        
        def dfs(crc,path):
            if crc in path:
                return False
            if crc in visited:
                return True
            visited.add(crc)
            if wanted[crc]==[]:
                res.append(crc)
                return True
            path.add(crc)
            for x in wanted[crc]:
                if not(dfs(x,path)):
                    return False 
            res.append(crc)
            path.remove(crc)
            return True
        for i in range(numCourses):
            if not dfs(i,path):
                return []
        return res