from stanfordcorenlp import StanfordCoreNLP


class StanfordCoreNLPModel:
    def __init__(self, test_text, stopwords):
        self.test_text = test_text
        self.stopwords = stopwords

    def run(self):
        nlp = StanfordCoreNLP(
            r'E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\selfModel\stanford-corenlp-full-2018-02-27',
            lang='zh')

        print('StanfordCoreNLP:')
        print("".join([(x + '/ ') for x in nlp.word_tokenize(self.test_text) if x not in self.stopwords]))
        print('\n')

        nlp.close()
