import os

def normal():
    os.system("DISPLAY:=0 xrandr --output HDMI-1 --auto")

def no_track():
    os.system("DISPLAY:=0 xrandr --output HDMI-1 --off")