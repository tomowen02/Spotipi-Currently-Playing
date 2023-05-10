import os

def normal():
    #os.system("DISPLAY=:0 xrandr --output HDMI-1 --auto") # Uncomment this if using HDMI
    #os.system("sudo echo 0 | sudo tee /sys/class/backlight/10-0045/bl_power") # Uncomment if using rpi official display

def no_track():
    #os.system("DISPLAY=:0 xrandr --output HDMI-1 --off") # Uncomment this if using HDMI
    #os.system("sudo echo 1 | sudo tee /sys/class/backlight/10-0045/bl_power") # Uncomment if using rpi official display