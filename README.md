sudo apt-get update
apt-get install python2.7 #if not installed
sudo apt-get install -y python-pip
sudo apt-get install -y xvfb
sudo echo -e "\ndeb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main" | sudo tee -a /etc/apt/sources.list > /dev/null
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29
sudo apt-get update
sudo apt-get install -y firefox
sudo apt-get install -y firefox-mozilla-build

wget "https://github.com/mozilla/geckodriver/releases/download/v0.10.0/geckodriver-v0.10.0-linux64.tar.gz"
tar xfv geckodriver-v0.10.0-linux64.tar.gz 
sudo cp geckodriver /usr/bin/

sudo nano /etc/locale.gen  # UNCOMENT the line "es_ES.UTF-8 UTF-8"
sudo locale-gen

git clone https://github.com/umamario/hashtag-downloader.git
sudo pip install -r hashtag-downloader/pip_requirements.txt


#To run the script
Xvfb :10 -ac & #if it is not already running
export DISPLAY=:10 
python hashtag-downloader/dowload_hashtag.py

# if you want to left it running, I recommend use a screen command typin "screen". It will permit to you go back to the program screen 
# after close de ssh. To go back to the screen write "screen -x" 


#You will be asked about the hashtag to be downloaded.
Please, pay attention if the global vars are according your requirements:

TIME_TO_WAIT = 60  #Time to wait between each page refresh
FTP_DIR = '/tmp/' #Directory of the ftp. The files will be downloaded on a Directory with same name than the hashtag
