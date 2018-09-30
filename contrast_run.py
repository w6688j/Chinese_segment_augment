from utils import getStopwords
from selfModel.JiebaModel import JiebaModel
from selfModel.SnowNLPModel import SnowNLPModel
from selfModel.ThulacModel import ThulacModel
from selfModel.PyNLPIRModel import PyNLPIRModel
from selfModel.StanfordCoreNLPModel import StanfordCoreNLPModel
from selfModel.TrieModel import TrieModel


def getTestText(dir):
    test_text = ''
    with open(dir, 'r', encoding='UTF-8') as f:
        i = 1
        lines = f.readlines()
        for line in lines:
            test_text += line.strip()
            if i == 5:
                break
            i += 1
    return test_text


if __name__ == "__main__":
    # 加载停用词
    stopwords = getStopwords('data/stopword.txt')

    # 效果对比
    # test = '蔡英文在昨天应民进党当局的邀请，准备和陈时中一道前往世界卫生大会，和谈有关九二共识问题'
    test = getTestText('E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\data\electric.txt')

    print('\n======================效果对比======================')
    print('text:')
    print(test + '\n')

    # Jieba
    JiebaModel = JiebaModel(test, stopwords)
    JiebaModel.run()

    # SnowNLP
    SnowNLPModel = SnowNLPModel(test, stopwords)
    SnowNLPModel.run()

    # Thulac
    ThulacModel = ThulacModel(test, stopwords)
    ThulacModel.run()

    # PyNLPIR
    PyNLPIRModel = PyNLPIRModel(test, stopwords)
    PyNLPIRModel.run()

    # StanfordCoreNLP
    StanfordCoreNLPModel = StanfordCoreNLPModel(test, stopwords)
    StanfordCoreNLPModel.run()

    # TrieModel
    TrieModel = TrieModel(test, stopwords, {
        'rootDir': 'E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\data\\root.pkl',
        'dictDir': 'E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\data\dict.txt',
        'demoDir': 'E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\data\demo.txt'
    })
    TrieModel.run()
