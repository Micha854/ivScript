#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sql
import createMessage
import sendMessage
import time
import sys

class Module():
  def nuller(self,cfg,gmt):
    send = sendMessage.sendMessage()
    send.setConfig(cfg.token)
    send.my_config(cfg.channels)
    sys.stdout.write("\x1b]2;%s\x07")
    while 1 == 1:
      Sql = sql.Sql()
      create = createMessage.createMessage()
      Sql.startSQL(cfg,"0er")
      send.clearOutputList(Sql.encounter_id)
      create.create(Sql,send,cfg.sleepTime,cfg,gmt)
      time.sleep(int(cfg.sleepTime))