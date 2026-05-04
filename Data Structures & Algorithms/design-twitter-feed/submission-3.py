class Twitter:
    def __init__(self):
        self.followMap=defaultdict(set)
        self.tweetMap=defaultdict(list)
        self.time=0 
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        self.tweetMap[userId].append([self.time,tweetId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        res=[]
        minHeap=[]
        for followeeID in self.followMap[userId]:
            if followeeID in self.tweetMap:
                index=len(self.tweetMap[followeeID])-1
                count,tweetId=self.tweetMap[followeeID][index]
                minHeap.append([count,tweetId,followeeID,index-1])
        heapq.heapify(minHeap)
            
        while(minHeap and len(res)<10):
            count,tweetId,followeeID,index=heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                count,tweetId=self.tweetMap[followeeID][index]
                heapq.heappush(minHeap,[count,tweetId,followeeID,index-1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId!=followerId:
            self.followMap[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
    