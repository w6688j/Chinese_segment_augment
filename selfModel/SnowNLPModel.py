from snownlp import SnowNLP


class SnowNLPModel:
    def __init__(self, test_text, stopwords):
        self.test_text = test_text
        self.stopwords = stopwords

    def run(self):
        s = SnowNLP(self.test_text)

        print('SnowNLP:')
        print("".join([(x + '/ ') for x in s.words if x not in self.stopwords]))
        print('\n')
