class Twitter:
    def __init__(self):
        self.count = 0  # acts like a timestamp (decreasing to simulate max heap behavior)
        
        # userId -> list of [timestamp, tweetId]
        # Each user's tweets are stored in order (newest at the end)
        self.tweetMap = defaultdict(list)
        
        # userId -> set of followeeIds
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append tweet with timestamp
        # Since count decreases, newer tweets have smaller values (higher priority)
        self.tweetMap[userId].append([self.count, tweetId])
        
        # Decrement timestamp for next tweet
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []        # final result (max 10 tweets)
        minHeap = []   # heap to merge tweets
        
        # Ensure user sees their own tweets
        self.followMap[userId].add(userId)

        # Step 1: Initialize heap with most recent tweet of each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # Start from most recent tweet (end of list)
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                
                # Push into heap:
                # [timestamp, tweetId, which user, next index to explore]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Step 2: Extract top 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            
            # Add most recent tweet to result
            res.append(tweetId)

            # Step 3: Push next tweet from same user (if exists)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followee to follower's set
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followee if present
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)