class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count= [0]*26
        for task in tasks:
            count[ord(task)-ord('A')]-=1
        
        freq=[]
        for task,count in enumerate(count):
            if count==0:
                continue
            heapq.heappush(freq, count)

        q=deque()
        time =0
        while freq or q:
            time+=1
            if freq:
                task=heapq.heappop(freq)
                task+=1
                if task!=0:
                    q.append([task,time+n])
            if q and q[0][1]==time:
                task=q.popleft()
                heapq.heappush(freq,task[0])
        return time
            
