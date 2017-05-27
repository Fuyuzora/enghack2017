from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

def find_polarity_scores(paragraph):
    sentences = tokenize.sent_tokenize(paragraph)
    sid = SentimentIntensityAnalyzer()
    score_list = []
    for sentence in sentences:
        print(sentence)
        ss = sid.polarity_scores(sentence)
        sentence_polarity_score = [ss['compound'], ss['neg'], ss['neu'], ss['pos']]
        print('[compound, neg, neu, pos]')
        print(sentence_polarity_score)
        score_list.append(sentence_polarity_score)
    return

def compile_polarity_scores(score_list):

    return

paragraph = "What if I have multiple sentences? This really sucks! Actually, yeah, this "\
            "is awful. Does it change if i add more? I hate this. this is an awesome paragraph."
find_polarity_scores(paragraph)