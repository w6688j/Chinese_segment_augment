import jieba
import time


class JiebaModel:
    def __init__(self, test_text, stopwords):
        self.test_text = test_text
        self.stopwords = stopwords

    def run(self):
        starttime = time.time()
        print('jieba全模式：')
        print("".join([(x + '/ ') for x in jieba.cut(self.test_text, cut_all=True) if x not in self.stopwords]))
        endtime1 = time.time()
        print('time cost:' + str(round((endtime1 - starttime), 4)) + ' seconds.\n')

        print('jieba精确模式：')
        print("".join([(x + '/ ') for x in jieba.cut(self.test_text, cut_all=False) if x not in self.stopwords]))
        endtime2 = time.time()
        print('time cost:' + str(round((endtime2 - starttime), 4)) + ' seconds.\n')

        print('jieba搜索引擎模式：')
        print("".join([(x + '/ ') for x in jieba.cut_for_search(self.test_text) if x not in self.stopwords]))
        endtime3 = time.time()
        print('time cost:' + str(round((endtime3 - starttime), 4)) + ' seconds.\n')
