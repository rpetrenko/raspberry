#!/bin/bash
############################################################
# to run this script on startup, add the following line
# @/bin/get-ips.sh
# to the file:
# /home/pi/.config/lxsession/LXDE-pi/autostart
############################################################

zenity --info --title="IP Addresses" --text="$(/bin/get-ips.py)"
