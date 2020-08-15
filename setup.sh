#!/bin/sh
echo "pocketsphinxをインストールしますか?(y/n)"
read pocketsphinx
echo "espeakをインストールしますか?(y/n)"
read espeak
echo "svoxpicoをインストールしますか?(y/n)"
read svoxpico

sudo apt-get install git
if [ $pocketsphinx = 'y' ]; then
    sudo apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev
    sudo apt-get install libasound2-dev
    git clone https://github.com/cmusphinx/pocketsphinx-python.git
    cd
    sudo pip install pocketsphinx
fi

if [ $espeak = 'y' ]; then
    sudo apt-get install espeak
fi

if [ $svoxpico = 'y' ]; then
    sudo apt-get install -y libttspico-utils
fi

echo "pocketsphinx, espeak　をインストールしました."

exit 1
