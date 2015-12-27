# CrazyDriver
Simple remote controlled car over WIFI with raspberry pi and servo motors

## Preparation

Tested on raspbian jesse (december 2015 version), on the first edition RPI.

Install webserver (eg. nginx), php 

Add www-data to sudoers file. [Note; this is very insecure! You need root to talk to GPIO pins, and this is a very easy way to execute scripts from the webserver. Do not use this unless you are POC this remote controlled car]

Setup your WIFI module to connect with your (adhoc) network. Stuff the credentials in /etc/wpa_supplicant/wpa_supplicant.conf

[optional] Make sure your hostname is crazydriver

## Setup

1. Mount continuous servo motors to gpio 11 and 12
1. Copy crazydriver to homedir
1. Add to path 'export PATH="$PATH:/home/pi/crazydriver"'
1. Copy webserver_public to public webdir
1. enjoy!

## How to use

1. On your mobile navigate to http://crazydriver/
2. Hit the buttons and drive or sound the horn!
