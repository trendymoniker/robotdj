
# SETUP MASTER PYTHON ENVIRONMENT WITH VIRTUALENV TOOLS
sudo apt-get -y install python-setuptools  # gets easy_install
#python-dev and gcc are needed for c extensions to work
sudo apt-get -y install python2.7 python2.7-dev gcc
sudo easy_install virtualenv
sudo easy_install pip
sudo pip install ipython
sudo pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
mkdir -p $WORKON_HOME
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

mkvirtualenv -p python2.7 --no-site-packages robotdj
sudo pip install ipython
easy_install ez_setup
pip install pyttsx

# rhythmbox plugin files go in /home/kevin/.local/share/rhythmbox/plugins/robotdj
