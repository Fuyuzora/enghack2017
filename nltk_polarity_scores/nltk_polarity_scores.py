from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import math
import numpy as np

class Sentiment(object):

    sentiment = ["neg","neu","pos"]

    def __init__(self):
        self._compound_score = []

    def _analyze(self, paragraph):
        neg_score = []
        neu_score = []
        pos_score = []
        sentences = tokenize.sent_tokenize(paragraph)
        sid = SentimentIntensityAnalyzer()

        for sentence in sentences:
            ss = sid.polarity_scores(sentence)
            neg_score.append(ss['neg'])
            neu_score.append(ss['neu'])
            pos_score.append(ss['pos'])
            self._compound_score.append(ss['compound'])

    def get_compound(self):
        return sum(self._compound_score)/float(len(self._compound_score))

    def get_sentiment(self, paragraph, score, weight=[0.5,0.5]):
        self._analyze(paragraph)
        if score == 0:
            weighted_score = 0
        else:
            weighted_score = Sentiment.score_func(score)

        if self.get_compound()*weight[0] + weighted_score*weight[1] >= 0.1:
            return 1
        elif self.get_compound()*weight[0] + weighted_score*weight[1] <= -0.1:
            return -1
        else:
            return 0

    @staticmethod
    def score_func(x, scale_factor=6.652146493630526):
        x = np.array(x)
        return 2 * np.arctan(x / scale_factor) / math.pi

if __name__ == '__main__':
    paragraph = "I'M TIRED OF CORRUPT POLITICIANS LIKE CROOKED HILLARY THINKING THEY CAN GET AWAY WITH KILLING HARAMBE WITH NO CONSEQUENCES "
    # paragraph = "What if I have multiple sentences? This really sucks! Actually, yeah, this "\
    #             "is awful. Does it change if i add more? I hate this. This is a awesome paragraph!"

    sent = Sentiment()
    print(sent.get_sentiment(paragraph, 165))
    print("Score weighted %f" % Sentiment.score_func(165))
    print("Score nltk %f" % sent.get_compound())
