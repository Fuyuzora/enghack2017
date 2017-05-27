# Created by Yuchen on 5/26/17.
import praw
import config
from nltk_polarity_scores.nltk_polarity_scores import Sentiment

class UserComment(object):
    def __init__(self, user):
        reddit = praw.Reddit(client_id=config.app_id,
                             client_secret=config.app_secret,
                             user_agent=config.app_ua)
        self._user = reddit.redditor(user)
        self._comments = self._user.comments.new(limit=None)

    @property
    def comments(self):
        return self._comments


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
    test()
    ucomment = UserComment('ViaGamma')
    sent = Sentiment()
    for comment in ucomment.comments:
        print(comment.body)
        sent.analyze(comment.body)
        print(sent.get_sentiment())

