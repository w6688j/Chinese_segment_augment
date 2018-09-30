from snownlp import SnowNLP
import time


class SnowNLPModel:
    def __init__(self, test_text, stopwords):
        self.test_text = test_text
        self.stopwords = stopwords

    def run(self):
        starttime = time.time()
        s = SnowNLP(self.test_text)

        print('SnowNLP:')
        print("".join([(x + '/ ') for x in s.words if x not in self.stopwords]))
        endtime = time.time()
        print('time cost:' + str(round((endtime - starttime), 4)) + ' seconds.\n')
