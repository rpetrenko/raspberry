import subprocess
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier


class TextProcessor(object):
    def __init__(self, fname):
        self.cl = self.create_classifier(fname)

    def create_classifier(self, fname):
        with open(fname, 'r') as fp:
            cl = NaiveBayesClassifier(fp, format='csv')
        return cl

    def _exec(self, cmd_l):
        print(cmd_l)
        subprocess.call(cmd_l)

    def process_text(self, event_text):
        print('== execute start ==')
        tag = self.cl.classify(event_text)
        if tag == "dsp_on":
            self._exec(['display.sh', 'on'])
        elif tag == "dsp_off":
            self._exec(['display.sh', 'off'])
        else:
            raise NotImplementedError(tag)
        print('== execute done ==')


if __name__ == "__main__":
    epr = TextProcessor("words.txt")
    tests = [
        ('screen off', 'dsp_off'),
        ('monitor on', 'dsp_on'),
        ('please turn my monitor off', 'dsp_off'),
        ('Turn screen on', 'dsp_on'),
        ('turn off my screen', 'dsp_off'),
        ('turn off my display', 'dsp_off'),
        ('take a picture now', 'pic'),
        ('show me last picture', 'pic_last')
    ]

    for test, expected in tests:
        pred = epr.cl.classify(test)
        print("{}:{}".format(pred, test))

    print("Accuracy:{}".format(epr.cl.accuracy(tests)))
