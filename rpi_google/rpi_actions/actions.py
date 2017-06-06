import subprocess
import json
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier


class TextProcessor(object):
    def __init__(self, fname_words, fname_actions):
        self.cl = self.create_classifier(fname_words)
        self.actions = self.read_actions(fname_actions)

    def create_classifier(self, fname):
        with open(fname, 'r') as fp:
            cl = NaiveBayesClassifier(fp, format='csv')
        return cl

    def read_actions(self, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
            return data

    def _exec(self, cmd_l):
        if cmd_l:
            print(cmd_l)
            # subprocess.call(cmd_l)
        else:
            raise Exception("action not defined")

    def process_text(self, event_text):
        print('== execute start ==')
        tag = self.cl.classify(event_text)
        if tag in self.actions:
            act = self.actions[tag]
            print("found tag {}, executing action {}".format(tag, act))
            self._exec(act)
        else:
            raise NotImplementedError(tag)
        print('== execute done ==')


if __name__ == "__main__":
    epr = TextProcessor("words.txt", "actions.json")
    tests = [
        ('screen off', 'dsp_off'),
        ('monitor on', 'dsp_on'),
        ('please turn my monitor off', 'dsp_off'),
        ('Turn screen on', 'dsp_on'),
        ('turn off my screen', 'dsp_off'),
        ('turn off my display', 'dsp_off'),
        ('take a picture now', 'pic'),
        ('show me last picture', 'pic_last'),
        ('temperature in the kitchen', 'temp_kitchen')
    ]

    for test, expected in tests:
        pred = epr.cl.classify(test)
        print("{}:{}".format(pred, test))

    print("Accuracy:{}".format(epr.cl.accuracy(tests)))

    epr.process_text("turn my display on")
