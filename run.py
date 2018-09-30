from utils import getStopwords
from selfModel.JiebaModel import JiebaModel
from selfModel.SnowNLPModel import SnowNLPModel
from selfModel.ThulacModel import ThulacModel
from selfModel.PyNLPIRModel import PyNLPIRModel
from selfModel.StanfordCoreNLPModel import StanfordCoreNLPModel

if __name__ == "__main__":
    # 加载停用词
    stopwords = getStopwords()

    # 效果对比
    test = '蔡英文在昨天应民进党当局的邀请，准备和陈时中一道前往世界卫生大会，和谈有关九二共识问题'
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