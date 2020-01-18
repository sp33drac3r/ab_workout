#! /usr/bin/env python

import os
import time
import threading

beep = "beep-07.mp3"
eye_of_the_tiger = "eye_of_the_tiger_10s.mp3"

def play_beeps():
  os.system("mpg123 " + beep)
  time.sleep(7)
  os.system("mpg123 " + beep)
  time.sleep(1)
  os.system("mpg123 " + beep)
  time.sleep(1)
  os.system("mpg123 " + beep)
  time.sleep(1)
  os.system("mpg123 " + eye_of_the_tiger)

def run():
  threading.Timer(60.0, run).start()
  play_beeps()

run()