# pi setup
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
* 