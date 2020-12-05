#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

####Hier wird die Config aus dem Configfile geladen und den einzelen
####Werten zugewiesen

class Config():
  channels = ""
  host = ""
  database = ""
  user = ""
  password = ""
  token = ""
  language = ""
  sort_pokemon = bool
  sleepTime = ""
  iv100 = ""
  iv0 = ""

  def readConfig(self,cfgFile):  
    with open(cfgFile, 'r') as config_file:
      config = json.load(config_file)

    self.channels = config['channels']
    
    self.host = config['mysql']['host']
    self.database = config['mysql']['database']
    self.user = config['mysql']['user']
    self.password = config['mysql']['password']

    self.token = config['settings']['token']
    self.language = config['settings']['language']
    self.sort_pokemon = config['settings']['sort_pokemon']
    self.sleepTime = config['settings']['sleep_time']
    self.iv100 = config['settings']['highlighting_100']
    self.iv0 = config['settings']['highlighting_0']