"""Twitter."""
import re


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets

    def __repr__(self):
        """
        Repr magic method.

        :return:
        """
        return f"TWEET:{self.user}, {self.time}, {self.retweets}"


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    result = sorted(tweets, key=lambda t: (t.retweets / t.time), reverse=True)
    return result[0]


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    result = list(sorted(tweets, key=lambda t: (t.retweets, -t.time), reverse=True))
    return result


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    contains_given_hashtag = []
    for tweet in tweets:
        if hashtag in tweet.content:
            contains_given_hashtag.append(tweet)
    return contains_given_hashtag


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    dic = {}
    for tweet in tweets:
        match = re.findall(r"(#\w*[0-9a-zA-Z]+)", tweet.content)
        try:
            for hashtag in match:
                if hashtag not in dic.keys():
                    dic[hashtag] = tweet.retweets
                else:
                    dic[hashtag] += tweet.retweets
        except AttributeError:
            continue
    return sorted(dic, key=lambda k: (-int(dic[k]), k))


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweet4 = Tweet("@Test", "See on sama populaarne, aga uuem #bigsmart", 1, 166500)
    tweet5 = Tweet("@Test", "See on kõige esimese tähega väiksuselt teine ja võrdne tweet #aaa", 2192, 284200)

    tweet6 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #AJW, #YYTV", 100, 30000)
    tweet7 = Tweet("@elonmusk", "Technically, alcohol is a solution #YYTV", 100, 30000)
    tweet8 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #rQPJOVDXU", 100, 25000)
    tweet9 = Tweet("@Test", "See on sama populaarne, aga uuem #VERbSPlJ'", 100, 20000)
    tweet10 = Tweet("@Test", "See on kõige esimese tähega väiksuselt teine ja võrdne tweet #PMgnWVd", 100, 15000)

    # tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]
    tweets = [tweet6, tweet7, tweet8, tweet9, tweet10]

    # print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

    filtered_by_popularity = sort_by_popularity(tweets)
    # print(filtered_by_popularity[0].user)  # -> "@CIA"
    # print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    # print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"

    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    # print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    # print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags)  # -> "#heart"
