import RPi.GPIO as GPIO
import time
import pygame

pygame.mixer.init()
GPIO.setmode(GPIO.BCM)

buttons = []


class button:
  def __init__(self, prompt, clip, pin):
    self.prompt = prompt
    self.clip = clip
    self.pin = pin
    button_attributes = [prompt, clip, pin]
    buttons.append(button_attributes)

  def load_clip(self):
    ''' loads and plays the appropriate sound clip for the button before it is played '''
    print("playing " + str(self.prompt))
    pygame.mixer.music.load(self.clip)    
    pygame.mixer.music.play()
    time.sleep(1)
    while pygame.mixer.music.get_busy() == True:
      continue

  def setup_pins(self):
    ''' Assigns the GPIO pins and makes it ready to press '''
    GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("pin " + str(self.pin) + " has been setup" )


# creates buttons from button class
wow = button("wow", "wow.mp3", 4)
applause = button("applause", "applause-1.wav", 18)
summon = button("summon", "summon.mp3", 22)

# unassigned buttons to be implemented later

# churu = button("churu", "churu.mp3", 17)
# outside = button("outside", "outside.mp3", 27)
# inside = button("inside", "inside.mp3", 5)
# play = button("play", "play.mp3", 6)
# litterbox = button("litterbox", "litterbox.mp3", 13)
# mom = button("mom", "mom.mp3", 19)
# dad = button("dad", "dad.mp3", 20)
# mad = button("mad", "mad.mp3", 21)
# pee = button("pee", "pee.mp3", 16)
# poop = button("poop", "poop.mp3", 25)
# bed = button("bed", "bed.mp3", 24)
# bellyrub = button("bellyrub", "bellyrub.mp3, 23)

## reclaim from wow and applause if you need more....

#
wow.setup_pins()
applause.setup_pins()
summon.setup_pins()
#input_state_wow = GPIO.input(wow.pin)

#main loop
# todo: Should try to stream line this if I can.  There will be alot of if statements within this while loop.
while True:
  # todo: figure out why the print in button.load_clip() doesn't print if the input_state_{BUTTON} is outside
  #       the while loop.  It doesn't make much sense to me.  Maybe it's the conflicting while loops???
  input_state_wow = GPIO.input(wow.pin)
  input_state_applause = GPIO.input(applause.pin)
  input_state_summon = GPIO.input(summon.pin)
  if input_state_wow == False:
    wow.load_clip()
  elif input_state_applause == False:
    applause.load_clip()
  elif input_state_summon == False:
    summon.load_clip()
