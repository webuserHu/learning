#!/bin/bash

cvt 650 900

xrandr --newmode "656x900_60.00" 48.25 656 696 760 864 900 903 913 934 -hsync +vsync

xrandr --addmode Virtual1 "656x900_60.00"

xrandr --output Virtual1 --mode "656x900_60.00"