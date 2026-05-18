class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        edges=defaultdict(list)
        for src,dst in tickets:
            edges[src].append(dst)
        res=["JFK"]
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in edges:
                return False
            for i,neighbor in enumerate(edges[src]):
                edges[src].pop(i)
                res.append(neighbor)
                if dfs(neighbor):
                    return True
                res.pop()
                edges[src].insert(i,neighbor)
                
            return False
        dfs("JFK")
        return res