class Twitter:

    def __init__(self):
        self.users_followers = defaultdict(set)
        self.users_post = defaultdict(list)
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users_post[userId].append((self.time,tweetId))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.users_post[userId][:]
        for followeeId in self.users_followers[userId]:
            feed.extend(self.users_post[followeeId])

        feed.sort(key=lambda x:-x[0])
        return [tweetId for _,tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users_followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users_followers[followerId].discard(followeeId)
