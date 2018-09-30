import os
import jieba
import time
# 自定义
from model import TrieNode
from utils import getStopwords, loadWords, generate_ngram, saveModel, loadModel


class TrieModel:
    def __init__(self, test_text, stopwords, dir):
        self.test_text = test_text
        self.stopwords = stopwords
        self.rootDir = dir['rootDir']
        self.dictDir = dir['dictDir']
        self.demoDir = dir['demoDir']

    def run(self):
        starttime = time.time()
        rootName = (self.rootDir)

        if os.path.exists(rootName):
            root = loadModel(rootName)
        else:
            dictName = self.dictDir
            word_freq = loadWords(dictName)
            root = TrieNode('*', word_freq)
            saveModel(root, rootName)

        # 加载新的文章
        fileName = self.demoDir
        data = self.loadData(fileName, self.stopwords)
        # 将新的文章插入到Root中
        self.loadData2Root(root, data)

        # 定义取TOP5个
        N = 5
        result, add_word = root.wordFind(N)
        # 如果想要调试和选择其他的阈值，可以print result来调整
        print("\n----\n", '增加了 %d 个新词, 词语和得分分别为: \n' % len(add_word))
        print('#############################')
        for word, score in add_word.items():
            print(word + ' ---->  ', score)
        print('#############################\n')

        for word, score in add_word.items():
            jieba.add_word(word)

        print("互信息、信息熵：")
        print("".join([(x + '/ ') for x in jieba.cut(self.test_text, cut_all=False) if x not in self.stopwords]))
        endtime = time.time()
        print('time cost:' + str(round((endtime - starttime), 4)) + ' seconds.\n')

    def loadData(self, fileName, stopwords):
        # 加载数据集
        data = []
        with open(fileName, 'rb') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = [x for x in jieba.cut(line, cut_all=False) if x not in stopwords]
                data.append(line)

        # 按照行进行切分句子，得到一个数组
        # [[行，切词], [], []]
        # print(data)
        return data

    def loadData2Root(self, root, data):
        print('------> 插入节点')
        for i in data:
            # tmp 表示每一行自由组合后的结果（n gram）
            # tmp: [['它'], ['是'], ['小'], ['狗'], ['它', '是'], ['是', '小'], ['小', '狗'], ['它', '是', '小'], ['是', '小', '狗']]
            tmp = generate_ngram(i, 3)
            # print(tmp)
            for d in tmp:
                root.add(d)
        print('------> 插入成功')


if __name__ == "__main__":
    # 加载停用词
    stopwords = getStopwords('E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\data\stopword.txt')
    test = '蔡英文在昨天应民进党当局的邀请，准备和陈时中一道前往世界卫生大会，和谈有关九二共识问题'
    tinydict = {
        'rootDir': 'E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\data\\root.pkl',
        'dictDir': 'E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\data\dict.txt',
        'demoDir': 'E:\Projects\PyCharmProjects\Gitee\Chinese_segment_augment\data\demo.txt'
    }

    TrieModel = TrieModel(test, stopwords, tinydict)
    TrieModel.run()
