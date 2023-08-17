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

while True:
  for i in instances:
    if GPIO.input(i.pin) == False:
      i.send_pb_notification()
      i.load_clip()
