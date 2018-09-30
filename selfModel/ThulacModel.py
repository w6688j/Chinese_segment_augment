import thulac
import time


class ThulacModel:
    def __init__(self, test_text, stopwords):
        self.test_text = test_text
        self.stopwords = stopwords

    def run(self):
        starttime = time.time()
        thu = thulac.thulac(seg_only=True)

        print('Thulac:')
        print("".join([(x + '/ ') for x in thu.cut(self.test_text, text=True) if x not in self.stopwords]))
        endtime = time.time()
        print('time cost:' + str(round((endtime - starttime), 4)) + ' seconds.\n')
