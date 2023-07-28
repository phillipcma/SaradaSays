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
wow = button("wow", "sounds/Wow.mp3", 4)
#applause = button("applause", "sounds/applause-1.wav", 18)
summon = button("summon", "sounds/Summon.mp3", 22)
# unassigned buttons to be implemented later
churu = button("churu", "sounds/Churu.mp3", 17)
outside = button("outside", "sounds/Outside.mp3", 27)
# Commented out inside because its the least interesting).
#inside = button("inside", "sounds/Inside.mp3", 5)
play = button("play", "sounds/Play.mp3", 6)
litterbox = button("litterbox", "sounds/Litterbox.mp3", 13)
mom = button("mom", "sounds/Mom.mp3", 19)
dad = button("dad", "sounds/Dad.mp3", 20)
mad = button("mad", "sounds/Mad.mp3", 21)
pee = button("pee", "sounds/Pee.mp3", 16)
poop = button("poop", "sounds/Poop.mp3", 25)
bed = button("bed", "sounds/Bed.mp3", 24)
bellyrub = button("bellyrub", "sounds/Bellyrub.mp3", 23)

## reclaim from wow and applause if you need more....

#
wow.setup_pins()
#applause.setup_pins()
summon.setup_pins()
churu.setup_pins()
outside.setup_pins()
play.setup_pins()
litterbox.setup_pins()
mom.setup_pins()
dad.setup_pins()
mad.setup_pins()
pee.setup_pins()
poop.setup_pins()
bed.setup_pins()
bellyrub.setup_pins()

#main loop
# todo: Should try to stream line this if I can.  There will be alot of if statements within this while loop.
while True:
  # todo: figure out why the print in button.load_clip() doesn't print if the input_state_{BUTTON} is outside
  #       the while loop.  It doesn't make much sense to me.  Maybe it's the conflicting while loops???
  input_state_wow = GPIO.input(wow.pin)
  #input_state_applause = GPIO.input(applause.pin)
  input_state_summon = GPIO.input(summon.pin)
  input_state_churu = GPIO.input(churu.pin)
  input_state_outside = GPIO.input(outside.pin)
  input_state_play = GPIO.input(play.pin)
  input_state_litterbox = GPIO.input(litterbox.pin)
  input_state_mom = GPIO.input(mom.pin)
  input_state_dad = GPIO.input(dad.pin)
  input_state_mad = GPIO.input(mad.pin)
  input_state_pee = GPIO.input(pee.pin)
  input_state_poop = GPIO.input(poop.pin)
  input_state_bed = GPIO.input(bed.pin)
  input_state_bellyrub = GPIO.input(bellyrub.pin)




  if input_state_wow == False:
    wow.load_clip()
  #elif input_state_applause == False:
  #  applause.load_clip()
  elif input_state_summon == False:
    summon.load_clip()
  elif input_state_churu == False:
    churu.load_clip()
  elif input_state_outside == False:
    outside.load_clip()
  elif input_state_play == False:
    play.load_clip()
  elif input_state_litterbox == False:
    littterbox.load_clip()
  elif input_state_mom == False:
    mom.load_clip()
  elif input_state_dad == False:
    dad.load_clip()
  elif input_state_mad == False:
    mad.load_clip()
  elif input_state_pee == False:
    Pee.load_clip()
  elif input_state_poop == False:
    Poop.load_clip()
  elif input_state_bed == False:    
    bed.load_clip()
  elif input_state_bellyrub == False:
    bellyrub.load_clip()
