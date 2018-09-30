import pynlpir
import time


class PyNLPIRModel:
    def __init__(self, test_text, stopwords):
        self.test_text = test_text
        self.stopwords = stopwords

    def run(self):
        starttime = time.time()
        pynlpir.open()

        print('PyNLPIR：')
        print("".join(
            [(x + '/ ') for x in pynlpir.segment(self.test_text, pos_tagging=False) if x not in self.stopwords]))
        endtime = time.time()
        print('time cost:' + str(round((endtime - starttime), 4)) + ' seconds.\n')
