#!/bin/bash
############################################################
# to run this script on startup, add the following line
# @/bin/get-ips.sh
# to the file:
# /home/pi/.config/lxsession/LXDE-pi/autostart
############################################################

fname=/bin/get-ips.py
if [ -f "$fname" ];then
    out=$($fname)
    echo $out
    zenity --list --title="IP Addresses" --column="Name" --column="IP" $out
else
    echo "bad"
    zenity --error --title="Error" --text="not found $fname"
fi