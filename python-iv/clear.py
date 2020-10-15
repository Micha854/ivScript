import telebot
import time
import json
import sys
import os
from termcolor import colored

class Clear():

  def clear(self,token,cfg):
    bot = telebot.TeleBot(token)

    # load clear
    if os.path.isfile('clear.json'):
      data = open('clear.json').read()
      clr = json.loads(data)
    else:
      clr = {}
      for areas in cfg.channels:
        if areas['Name'] not in clr:
          clr[areas['Name']] = {'encounter': [], 'isIV': [], 'messageID': [], 'listID': []}

    print("\n" + colored("    INFO:", 'cyan') + " Starte CleanUp....................................")
    time.sleep(1)

    for areas in cfg.channels:
      try:
        IDlist = clr[areas['Name']]['messageID']
      except:
        print(colored("   ERROR:", 'red') + " Irgendwas stimmt nicht mit deiner " + colored("clear.json", 'yellow') + ", entferne sie und starte das script neu!")
        sys.exit(colored("    INFO:", 'cyan') + " Das Script wurde beendet!!!")
      #print(IDlist)
      for messageID in IDlist:
        try:
          bot.delete_message(areas['ivchat_id'],message_id=messageID)
          print(colored(" SUCCESS:", 'green') + " Entferne message in " + areas['Name'])
        except:
          print(colored(" WARNING:", 'yellow') + " Message in " + areas['Name'] + " konnte nicht entfernt werden")
        
        time.sleep(0.1)

      if clr[areas['Name']]['listID']:
        try:
          bot.delete_message(areas['ivchat_id'],message_id=clr[areas['Name']]['listID'])
          print(colored(" SUCCESS:", 'green') + " Entferne Overview in " + areas['Name'])
        except:
          print(colored(" WARNING:", 'yellow') + " Overview in " + areas['Name'] + " konnte nicht entfernt werden")