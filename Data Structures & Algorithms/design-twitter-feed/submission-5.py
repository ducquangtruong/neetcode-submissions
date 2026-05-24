class Twitter:

    def __init__(self):
        # followerId: set(followeeId)
        self.userStore = defaultdict(set)
        # followerId: list((tweetTime, tweetId))
        self.tweetStore = defaultdict(list)
        # Keep track of when tweets are posted
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetStore[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set(self.userStore[userId])
        users.add(userId)
        # Heap
        tweetHeap = []
        for user in users:
            for tweet in self.tweetStore[user]:
                heapq.heappush(tweetHeap, tweet)
                if len(tweetHeap) > 10:
                    heapq.heappop(tweetHeap)
        
        return [x[1] for x in sorted(tweetHeap, reverse = True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userStore[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userStore[followerId]:
            self.userStore[followerId].remove(followeeId)
