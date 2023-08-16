import RPi.GPIO as GPIO
import time
import pygame
import json
import psycopg2
from pushbullet import Pushbullet


pygame.mixer.init()
GPIO.setmode(GPIO.BCM)

with open("config.json") as config_file:
  config = json.load(config_file)


pb_api_key = config["pb_api_key"]
db_user = config["db_user"]
db_pass = config["db_pass"]

pb = Pushbullet(pb_api_key)

buttons = []
instances = []

#try:
#  connection = psycopg2.connect(
#    db_user = "SaradaSaysDB", 
#    db_pass = "NarutoUzumaki")
    


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
    instances.append(self)

  def load_clip(self):
    ''' loads and plays the appropriate sound clip for the button before it is played '''
    print("playing " + str(self.prompt) + str(self.pin))
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
food = button("food", "sounds/Food.mp3", 12, "message is Food")
summon = button("summon", "sounds/Summon.mp3", 22, "message is summon")
churu = button("churu", "sounds/Churu.mp3", 18, "message is Churu")
outside = button("outside", "sounds/Outside.mp3", 27, "Message is Outside")
play = button("play", "sounds/Play.mp3", 6, "message is Play")
litterbox = button("litterbox", "sounds/Litterbox.mp3", 13, "message is litterbox")
mom = button("mom", "sounds/Mom.mp3", 26, "message is mom")
dad = button("dad", "sounds/Dad.mp3", 20, "message is Dad")
mad = button("mad", "sounds/Mad.mp3", 21, "message is Mad")
pee = button("pee", "sounds/Pee.mp3", 16, "message is Pee")
poop = button("poop", "sounds/Poop.mp3", 25, "message is Poop")
bed = button("bed", "sounds/Bed.mp3", 24, "message is bed")
bellyrub = button("bellyrub", "sounds/BellyRub.mp3", 23, "message is bellyrub")


#sets up pin assignment
for i in instances:
  i.setup_pins()
  time.sleep(.5)

#main loop
# todo: Should try to stream line this if I can.  There will be alot of if statements within this while loop.
while True:
  # todo: figure out why the print in button.load_clip() doesn't print if the input_state_{BUTTON} is outside
  #       the while loop.  It doesn't make much sense to me.  Maybe it's the conflicting while loops???
  input_state_food = GPIO.input(food.pin)
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


  if input_state_food == False:
    food.send_pb_notification()
    food.load_clip()
  elif input_state_summon == False:
    summon.send_pb_notification()
    summon.load_clip()
  elif input_state_churu == False:
    churu.send_pb_notification()
    churu.load_clip()
  elif input_state_outside == False:
    outside.send_pb_notification()
    outside.load_clip()
  elif input_state_play == False:
    play.send_pb_notification()
    play.load_clip()
  elif input_state_litterbox == False:
    litterbox.send_pb_notification()
    litterbox.load_clip()
  elif input_state_mom == False:
    mom.send_pb_notification()
    mom.load_clip()
  elif input_state_dad == False:
    dad.send_pb_notification()
    dad.load_clip()
  elif input_state_mad == False:
    mad.send_pb_notification()
    mad.load_clip()
  elif input_state_pee == False:
    pee.send_pb_notification()
    pee.load_clip()
  elif input_state_poop == False:
    poop.send_pb_notification()
    poop.load_clip()
  elif input_state_bed == False:    
    bed.send_pb_notification()
    bed.load_clip()
  elif input_state_bellyrub == False:
    bellyrub.send_pb_notification()
    bellyrub.load_clip()
