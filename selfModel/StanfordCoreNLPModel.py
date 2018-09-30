from stanfordcorenlp import StanfordCoreNLP
import time


class StanfordCoreNLPModel:
    def __init__(self, test_text, stopwords):
        self.test_text = test_text
        self.stopwords = stopwords

    def run(self):
        starttime = time.time()
        nlp = StanfordCoreNLP(
            r'E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\selfModel\stanford-corenlp-full-2018-02-27',
            lang='zh')

        print('StanfordCoreNLP:')
        print("".join([(x + '/ ') for x in nlp.word_tokenize(self.test_text) if x not in self.stopwords]))
        endtime = time.time()
        print('time cost:' + str(round((endtime - starttime), 4)) + ' seconds.\n')

        nlp.close()
