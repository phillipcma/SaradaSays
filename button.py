import RPi.GPIO as GPIO
import time
import pygame
from pushbullet import Pushbullet

pygame.mixer.init()
GPIO.setmode(GPIO.BCM)
pb = Pushbullet("o.8SH4Ij4fyTjSU9yx5x8gBFYPjeNWfOdK")

buttons = []


def send_notification(title, message):
  push = pb.push_note(title, message)

class button:
  def __init__(self, prompt, clip, pin, message):
    self.prompt = prompt
    self.clip = clip
    self.pin = pin
    self.message = message
    button_attributes = [prompt, clip, pin, message]
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

  def send_pb_notification(self):
    if __name__ == "__main__":
      send_notification("Sarada Says:", self.message)




# creates buttons from button class
wow = button("wow", "sounds/Wow.mp3", 4, "message is Wow")
#applause = button("applause", "sounds/applause-1.wav", 18, "message is applause")
summon = button("summon", "sounds/Summon.mp3", 22, "message is summon")
# unassigned buttons to be implemented later
churu = button("churu", "sounds/Churu.mp3", 17, "message is Churu")
outside = button("outside", "sounds/Outside.mp3", 27, "Message is Outside")
# Commented out inside because its the least interesting).
play = button("play", "sounds/Play.mp3", 6, "message is Play")
litterbox = button("litterbox", "sounds/Litterbox.mp3", 13, "message is litterbox")
mom = button("mom", "sounds/Mom.mp3", 19, "message is mom")
dad = button("dad", "sounds/Dad.mp3", 20, "message is Dad")
mad = button("mad", "sounds/Mad.mp3", 21, "message is Mad")
pee = button("pee", "sounds/Pee.mp3", 16, "message is Pee")
poop = button("poop", "sounds/Poop.mp3", 25, "message is Poop")
bed = button("bed", "sounds/Bed.mp3", 24, "message is bed")
bellyrub = button("bellyrub", "sounds/Bellyrub.mp3", 23, "message is bellyrub")

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
    summon.send_pb_notification()
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
