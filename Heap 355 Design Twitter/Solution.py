'''
####################################################################################################
### Data Structures

#### Tweets
For each user, store all tweets in chronological order.
self.tweets[userId] = [(timestamp, tweetId), ...]
We'll maintain a global timestamp that increases with every tweet.

#### Follow Relationships
self.following[followerId] = {followee1, followee2, ...}
Using a set gives O(1) follow/unfollow.

####################################################################################################
### News Feed
The feed should contain:
* User's own tweets
* Tweets from everyone they follow
* Top 10 most recent tweets

Instead of gathering all tweets and sorting them, notice:
	Each user's tweet list is already sorted by time. This becomes a Merge K Sorted Lists problem.

Use a max heap:
* Push the most recent tweet from each relevant user.
* Pop the newest tweet.
* Push the next older tweet from the same user.
* Repeat until we have 10 tweets.

####################################################################################################
# Complexity Analysis

### postTweet
	Appending to list: O(1)

### follow / unfollow
	Set insertion/removal: O(1)

### getNewsFeed

	Let:
	* F = number of followed users + self

	Heap contains at most one tweet per user.

	Building heap: O(F)

	Generating feed:
	At most 10 heap pops/pushes: O(10 log F)

	Overall: O(F + 10 log F)

Space: O(F)
for the heap.

### Why this is optimal
A naive solution would collect all tweets from all followed users and sort them:
O(T log T) - where T is total tweets.
The heap approach only touches the tweets needed to produce the 10 most recent, making it much more efficient.
'''
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.timestamp = 0
        # userId -> [(timestamp, tweetId)]
        self.tweets = defaultdict(list)
        # followerId -> set(followeeIds)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:

        max_heap = []
        users = self.following[userId] | {userId}  # self.following[userId].union({userId})

        # add most recent tweet from each user, if each exists
        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                timestamp, tweet_id = self.tweets[user][idx]
                heapq.heappush_max(max_heap, (timestamp, tweet_id, user, idx))

        # build feed
        feed = []
        while max_heap and len(feed) < 10:
            timestamp, tweet_id, user, idx = heapq.heappop_max(max_heap)
            feed.append(tweet_id)
            idx -= 1
            if idx >= 0:
                timestamp, next_tweet = self.tweets[user][idx]
                heapq.heappush_max( max_heap, (timestamp, next_tweet, user, idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # discard not remove because key error can happen
        self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


if __name__ == "__main__":

    print("========== Test Case 1: Example from Question ==========")

    twitter = Twitter()

    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # Expected: [5]

    twitter.follow(1, 2)

    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # Expected: [6, 5]

    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # Expected: [5]

    print("\n========== Test Case 2: User sees own tweets only ==========")

    twitter = Twitter()

    twitter.postTweet(1, 101)
    twitter.postTweet(1, 102)
    twitter.postTweet(1, 103)

    print(twitter.getNewsFeed(1))
    # Expected: [103, 102, 101]

    print("\n========== Test Case 3: Follow user with older and newer tweets ==========")

    twitter = Twitter()

    twitter.postTweet(1, 1)
    twitter.postTweet(2, 2)

    twitter.follow(1, 2)

    twitter.postTweet(2, 3)

    print(twitter.getNewsFeed(1))
    # Expected: [3, 2, 1]

    print("\n========== Test Case 4: Unfollow removes tweets from feed ==========")

    twitter = Twitter()

    twitter.postTweet(1, 1)

    twitter.follow(1, 2)

    twitter.postTweet(2, 2)
    twitter.postTweet(2, 3)

    print(twitter.getNewsFeed(1))
    # Expected: [3, 2, 1]

    twitter.unfollow(1, 2)

    print(twitter.getNewsFeed(1))
    # Expected: [1]

    print("\n========== Test Case 5: More than 10 tweets ==========")

    twitter = Twitter()

    for tweet_id in range(1, 16):
        twitter.postTweet(1, tweet_id)

    print(twitter.getNewsFeed(1))
    # Expected:
    # [15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

    print("\n========== Test Case 6: Multiple followees ==========")

    twitter = Twitter()

    twitter.postTweet(1, 1)

    twitter.follow(1, 2)
    twitter.follow(1, 3)

    twitter.postTweet(2, 2)
    twitter.postTweet(3, 3)
    twitter.postTweet(2, 4)
    twitter.postTweet(3, 5)

    print(twitter.getNewsFeed(1))
    # Expected: [5, 4, 3, 2, 1]

    print("\n========== Test Case 7: Followee with no tweets ==========")

    twitter = Twitter()

    twitter.postTweet(1, 1)

    twitter.follow(1, 2)

    print(twitter.getNewsFeed(1))
    # Expected: [1]

    print("\n========== Test Case 8: Unfollow user never followed ==========")

    twitter = Twitter()

    twitter.postTweet(1, 1)

    twitter.unfollow(1, 2)

    print(twitter.getNewsFeed(1))
    # Expected: [1]

    print("\n========== Test Case 9: Empty feed ==========")

    twitter = Twitter()

    print(twitter.getNewsFeed(1))
    # Expected: []

    print("\n========== Test Case 10: Complex mixed operations ==========")

    twitter = Twitter()

    twitter.postTweet(1, 5)

    twitter.follow(1, 2)
    twitter.follow(1, 3)

    twitter.postTweet(2, 6)
    twitter.postTweet(3, 7)
    twitter.postTweet(2, 8)

    print(twitter.getNewsFeed(1))
    # Expected: [8, 7, 6, 5]

    twitter.unfollow(1, 2)

    print(twitter.getNewsFeed(1))
    # Expected: [7, 5]

    twitter.postTweet(3, 9)

    print(twitter.getNewsFeed(1))
    # Expected: [9, 7, 5]