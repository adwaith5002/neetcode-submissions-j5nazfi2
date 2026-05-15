class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        wanted={i:[] for i in range(1,n+1)}
        for i in range(len(edges)):
            a,b=edges[i]
            wanted[a].append(b)
            wanted[b].append(a)
        visit=set()
        res=set()
        cycleStart=-1
        def dfs(node,parent):
            nonlocal cycleStart
            if node in visit:
                cycleStart=node
                return True
            visit.add(node)
            for child in wanted[node]:
                if child==parent:
                    continue
                if dfs(child,node):
                    if cycleStart!=-1:
                        res.add(node)
                    if node==cycleStart:
                        cycleStart=-1
                    return True
            return False

        dfs(1,-1)
        for u,v in reversed(edges):
            if u in res and v in res:
                return [u,v]
        return []
