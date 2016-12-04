#!/usr/bin/env python3
# countdown.py - a simple countdown script

import time
import subprocess

time_left = 5
while time_left:
    print('Time left:', time_left)
    time.sleep(1)
    time_left -= 1

# At the end of the countdown, play a sound file (a default Ubuntu notification)
subprocess.Popen(['/usr/bin/mpv',
                  '/usr/share/sounds/ubuntu/notifications/Amsterdam.ogg'])
