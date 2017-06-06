import subprocess


def execute_event(event_text):
    print('== execute start ==')
    # print(event.args.items())
    words = event_text.split()
    print("words: [{}]".format(words))
    if set(['turn', 'screen', 'off']).issubset(words):
        subprocess.call(['display.sh', 'off'])
    if set(['turn', 'screen', 'on']).issubset(words):
        subprocess.call(['display.sh', 'on'])
    print('== execute done ==')
