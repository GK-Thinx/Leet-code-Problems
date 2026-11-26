class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.followees = {}
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets.setdefault(userId, []).append((self.time, tweetId))
    def getNewsFeed(self, userId: int) -> list[int]:
        import heapq
        heap = []
        followees = self.followees.get(userId, set())
        followees = set(followees)
        followees.add(userId)
        for uid in followees:
            lst = self.tweets.get(uid)
            if not lst:
                continue
            for ts, tid in lst[-10:]:
                if len(heap) < 10:
                    heapq.heappush(heap, (ts, tid))
                else:
                    if ts > heap[0][0]:
                        heapq.heapreplace(heap, (ts, tid))
        return [tid for _, tid in sorted(heap, key=lambda x: -x[0])]
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followees.setdefault(followerId, set()).add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        s = self.followees.get(followerId)
        if s:
            s.discard(followeeId)