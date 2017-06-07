# Pi setup
* create file /home/pi/.bash_aliases
* add home path there
```bash
export PATH=$PATH:$HOME/bin
```
* install some dependencies
```bash
sudo apt-get install pqiv
```

# rpi-google setup
* install requirements in rpi_google
```bash
pip install -r rpi_google/requirements.txt
```
* install requirements in rpi_actions
```bash
pip install -r rpi_google/rpi_actions/requirements.txt
```
* download data for nltk (134M unzipped)
```bash
python -m textblob.download_corpora
```

# test voice command (activate venv)
* activate google assistant
```python
python rpi-google/hotword.py
```
* say: "turn screen on"

# some useful commands that google assistant understands
* setup timer for 10 minutes
* time to work
* time to my home
* my agenda
* temperature now
* how many days till june 12th

## Upgrade
* upgrade packages
```bash
pip install --upgrade google-assistant-sdk
pip install --upgrade google-assistant-sdk[samples]
```
* verify samples work
```bash
googlesamples-assistant-pushtotalk
googlesamples-assistant-hotword
```

/home/pi/env/lib/python3.4/site-packages/googlesamples/assistant/library/hotword.py  
/home/pi/env/lib/python3.4/site-packages/googlesamples/assistant/grpc/pushtotalk.py                                               │