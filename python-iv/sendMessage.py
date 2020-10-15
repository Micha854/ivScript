#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import datetime
import json
import os
import sys
from termcolor import colored

class sendMessage():
  
  bot = ""
  overview_old = {}
  channels = {}
  clear = {}
  lengh = {}
  last_encounter_id = []
  list_output = []
  overviewId = 0
  chatID = 0
  isfile = 0
  noiv = 0

  # check config file
  def my_config(self,channels):
    for areas in channels:
      self.overview_old[areas['Name']] = ""
      if not os.path.exists(areas['Name']):
        os.mkdir(areas['Name'])
      if areas['Name'] not in self.clear:
        self.clear[areas['Name']] = {'encounter': [], 'isIV': [], 'messageID': [], 'listID': []}
      
      if not os.path.isfile(areas['Name']+"/iv-werte.txt"):
        print(colored("   ERROR:", 'red') + " file " + colored("iv-werte.txt", 'yellow') + " in folder " + colored(str(areas['Name']), 'yellow') + " does not exist!")
        self.isfile += 1
      if not os.path.isfile(areas['Name']+"/level-werte.txt"):
        print(colored("   ERROR:", 'red') + " file " + colored("level-werte.txt", 'yellow') + " in folder " + colored(str(areas['Name']), 'yellow') + " does not exist!")
        self.isfile += 1
      if not os.path.isfile(areas['Name']+"/mode-werte.txt"):
        print(colored("   ERROR:", 'red') + " file " + colored("mode-werte.txt", 'yellow') + " in folder " + colored(str(areas['Name']), 'yellow') + " does not exist!")
        self.isfile += 1
    
    self.channels = channels
    if self.isfile:
      sys.exit(colored("    INFO:", 'cyan') + " Das Script wurde beendet, da " + str(self.isfile) + " Dateien fehlen!!!")

  # save clear.json
  def write_json(self, clear, filename='clear.json'):
    with open(filename, 'w') as data:
      json.dump(self.clear, data, indent=4)

  def change(self,bolt_line,normal_line,encounter,latitude,longitude,ChatName,ChatId,messID,pos):
    try:
      self.bot.delete_message(ChatId,messID)
    except:
      print(colored("   ERROR:", 'red') + " NonIV Venue konnte nicht gelöscht werden")
    try:
      id = self.bot.send_venue(ChatId,latitude,longitude,bolt_line,normal_line,disable_notification=True)
      self.clear[ChatName]['messageID'][pos] = id.message_id
      self.clear[ChatName]['isIV'][pos] = 1
      self.write_json(self.clear)
      print(colored(" SUCCESS:", 'green') + " encounter " + colored(str(encounter) + " wurde zu IV", 'yellow'))
    except:
      print(colored("   ERROR:", 'red') + " encounter " + str(encounter) + " wurde zu IV und konnte nicht erneut versendet werden")

  # send venue messages
  def send(self,bolt_line,normal_line,encounter,latitude,longitude,ChatName,ChatId,isIV):
    try:
      id = self.bot.send_venue(ChatId,latitude,longitude,bolt_line,normal_line,disable_notification=True)
      self.list_output.append(encounter)
      self.clear[ChatName]['messageID'].append(id.message_id)
      self.clear[ChatName]['encounter'].append(encounter)
      self.clear[ChatName]['isIV'].append(isIV)
      self.write_json(self.clear)
      print(colored(" SUCCESS:", 'green') + " Sende encounter " + str(encounter) + " in " + str(ChatName))
      return id.message_id
    except:
      print(colored("   ERROR:", 'red') + " encounter " + str(encounter) + " konnte nicht versendet werden")
  
  # send overview message
  def sendOverview(self,message,new_pokemon,old_pokemon):
    for areas in self.channels:
      if areas['Name'] not in message:
        message[areas['Name']] = ""
      if areas['Name'] not in new_pokemon:
        new_pokemon[areas['Name']] = 0
      if areas['Name'] not in old_pokemon:
        old_pokemon[areas['Name']] = 0
      
      self.chatID = areas['chat_id']
      self.lengh[areas['Name']] = len(message[areas['Name']]) - len(self.overview_old[areas['Name']])

      if not message[areas['Name']] and self.overview_old[areas['Name']]:
        try:
          self.bot.delete_message(self.chatID,self.clear[areas['Name']]['listID'])
          self.clear[areas['Name']]['listID'] = []
          self.overview_old[areas['Name']] = message[areas['Name']]
          print(colored(" SUCCESS:", 'green') + " Overview in " + areas['Name'] + " wurde entfernt, keine Meldungen mehr")
        except:
          print(colored("   ERROR:", 'red') + " Overview in " + areas['Name'] + " konnte nicht entfernt werden")
      else:
        if not message[areas['Name']] == self.overview_old[areas['Name']]:
          if (len(message[areas['Name']]) <= len(self.overview_old[areas['Name']]) and new_pokemon[areas['Name']] == old_pokemon[areas['Name']]) or (len(message[areas['Name']]) > len(self.overview_old[areas['Name']]) and self.lengh[areas['Name']] == 1):
            try:
              self.bot.edit_message_text(message[areas['Name']],chat_id=self.chatID, message_id=self.clear[areas['Name']]['listID'], parse_mode='HTML',disable_web_page_preview=True) ##Nachricht
              self.overview_old[areas['Name']] = message[areas['Name']]
              print(colored(" SUCCESS:", 'green') + " Overview in " + areas['Name'] + " wurde editiert")
            except:
              try:
                self.bot.delete_message(self.chatID,self.clear[areas['Name']]['listID'])
                self.overviewId = self.bot.send_message(self.chatID,message[areas['Name']],parse_mode='HTML')
                self.clear[areas['Name']]['listID'] = self.overviewId.message_id
                self.overview_old[areas['Name']] = message[areas['Name']]
                print(colored(" WARNING:", 'yellow') + " Overview in " + areas['Name'] + " konnte nicht editiert werden")
              except:
                print(colored("   ERROR:", 'red') + " Overview in " + areas['Name'] + " konnte nicht erneut gesendet werden")
          else:
            try: 
              self.bot.delete_message(self.chatID,self.clear[areas['Name']]['listID'])
              self.overviewId = self.bot.send_message(self.chatID,message[areas['Name']],parse_mode='HTML')
              self.clear[areas['Name']]['listID'] = self.overviewId.message_id
              self.overview_old[areas['Name']] = message[areas['Name']]
              print(colored(" SUCCESS:", 'green') + " Overview in " + areas['Name'] + " wurde Neu gesendet")
            except:
              try:
                self.overviewId = self.bot.send_message(self.chatID,message[areas['Name']],parse_mode='HTML',disable_web_page_preview=True,disable_notification=False)
                self.clear[areas['Name']]['listID'] = self.overviewId.message_id
                self.overview_old[areas['Name']] = message[areas['Name']]
                print(colored(" SUCCESS:", 'green') + " Overview in " + areas['Name'] + " wurde gesendet")
              except:
                print(colored("   ERROR:", 'red') + " Overview in " + areas['Name'] + " konnte nicht gesendet werden")
        self.write_json(self.clear)
   
  # clear channels
  def clearOutputList(self,encounter):
    now = datetime.datetime.now()
    print(colored("    INFO:", 'cyan') + " Checke Outputliste " + now.strftime("%H:%M:%S") + ", Total Spawns " + str(len(self.last_encounter_id)) + " (davon noiv: " + str(self.noiv) + ", gemeldet: " + str(len(self.list_output)) + ")")

    for areas in self.channels:
      for encount in self.clear[areas['Name']]['encounter']:
        index = self.clear[areas['Name']]['encounter'].index(encount)
        if not encounter.__contains__(encount):
          try:
            self.bot.delete_message(areas['ivchat_id'],self.clear[areas['Name']]['messageID'][index])
            self.clear[areas['Name']]['messageID'].__delitem__(index)
            self.clear[areas['Name']]['encounter'].__delitem__(index)
            self.clear[areas['Name']]['isIV'].__delitem__(index)
            self.list_output.remove(encount)
            print(colored(" SUCCESS:", 'green') + " Entferne encounter " + str(encount) + " in " + areas['Name'])
          except:
            print(colored("   ERROR:", 'red') + " encounter " + str(encount) + " in " + areas['Name'] + " konnte nicht entfernt werden")

      self.write_json(self.clear)

    for encount in self.last_encounter_id:
        if encount not in encounter:
          self.last_encounter_id.remove(encount)

  def setConfig(self,token):
    self.bot = telebot.TeleBot(token)