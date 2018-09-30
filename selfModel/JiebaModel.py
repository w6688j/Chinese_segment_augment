import jieba


class JiebaModel:
    def __init__(self, test_text, stopwords):
        self.test_text = test_text
        self.stopwords = stopwords

    def run(self):
        print('jieba全模式：')
        print("".join([(x + '/ ') for x in jieba.cut(self.test_text, cut_all=True) if x not in self.stopwords]))
        print('\n')

        print('jieba精确模式：')
        print("".join([(x + '/ ') for x in jieba.cut(self.test_text, cut_all=False) if x not in self.stopwords]))
        print('\n')

        print('jieba搜索引擎模式：')
        print("".join([(x + '/ ') for x in jieba.cut_for_search(self.test_text) if x not in self.stopwords]))
        print('\n')
