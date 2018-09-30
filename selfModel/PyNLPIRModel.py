import pynlpir


class PyNLPIRModel:
    def __init__(self, test_text, stopwords):
        self.test_text = test_text
        self.stopwords = stopwords

    def run(self):
        pynlpir.open()

        print('PyNLPIR：')
        print("".join(
            [(x + '/ ') for x in pynlpir.segment(self.test_text, pos_tagging=False) if x not in self.stopwords]))
        print('\n')
