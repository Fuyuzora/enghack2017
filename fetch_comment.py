# Created by Yuchen on 5/26/17.
import praw
import config
from nltk_polarity_scores.nltk_polarity_scores import Sentiment


class User(object):
    def __init__(self, user):
        reddit = praw.Reddit(client_id=config.app_id,
                             client_secret=config.app_secret,
                             user_agent=config.app_ua)
        self._user = reddit.redditor(user)

    @property
    def comments(self):
        return self._user.comments.new(limit=None)


def test():
    reddit = praw.Reddit(client_id=config.app_id,
                         client_secret=config.app_secret,
                         user_agent=config.app_ua)
    for submission in reddit.subreddit('learnpython').hot(limit=10):
        print(submission.author)

    # user = reddit.redditor('ViaGamma')
    # for comment in user.comments.new(limit=None):
    #     print(comment.body)

if __name__ == '__main__':
    test_users = ['ghostcheck', 'ViaGamma', 'rogueqd']
    # test()
    # ucomment = User(test_users[2])
    ucomment = User('the-realDonaldTrump')
    sent = Sentiment()
    for comment in ucomment.comments:
        if comment.score < 0:
            print(comment.body)
            print(sent.get_sentiment(comment.body, comment.score))
            print("Score %d" % comment.score)
            print("Score weighted %f" % Sentiment.score_func(comment.score))
            print("Score nltk %f" % sent.get_compound())

