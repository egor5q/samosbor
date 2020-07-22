# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback

token = os.environ['samosbor']
bot = telebot.TeleBot(token)


client=MongoClient(os.environ['database'])
db=client.samosbor
users=db.users
codes = db.codes
locs = db.locs
if codes.find_one({}) == None:
    codes.insert_one({'code':0})

if locs.find_one({}) == None:
    locs.insert_one({'locs':{}})
    
def createloc(name, id, nearlocs, cod):
    return {
        'name':name,
        'id':id,
        'items':{},
        'nearlocs':nearlocs,
        'players':{},
        'code':cod
    }
        
    
locss = {
    'testloc1':createloc(name = 'Тест1', id = -1001477215496, nearlocs = ['testloc2'], cod = 'testloc1'),
    
    'testloc2':createloc(name = 'Тест2', id = -1001187807260, nearlocs = ['testloc1', 'testloc3'], cod = 'testloc2'),
    
    'testloc3':createloc(name = 'Тест3', id = -1001264719525, nearlocs = ['testloc2'], cod = 'testloc3')


}

x = locs.find_one({})

for ids in locss:
    if ids not in x['locs']:
        locs.update_one({},{'$set':{'locs.'+ids:locss[ids])}})
        try:
            bot.send_message(441399484, 'Новая локация добавлена:\n\n'+str(locss[ids]))
        except:
            pass

def findloc(chat):
    loc = None
    for ids in locs:
        if locs[ids]['id'] == chat.id:
            loc = locs[ids]
    return loc
    
@bot.message_handler(content_types = ['new_chat_members'])
def newbie(m):
    loc = findloc(m.chat)
    if m.from_user.id not in 
    

def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode=None):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)   

def code():
    c = codes.find_one({})['code']
    codes.update_one({},{'$inc':{'code':1}})
    return str(c)

def createuser(user):
    return {
        'id':user.id,
        'units':{},
        'current_unit':None
    }

def createunit(user):
    c = code()
    return {c:{
        'code':c,
        'id':user.id,
        'name':None,
        'show_name':None,
        'inventory':{},
        'location':None,
        'stats':{
            'maxhunger':100,
            'hungher':100,
            
            'maxhealth':100,
            'health':100,
            
            'maxwater':100,
            'water':100,
            
            'maxrest':100,
            'rest':100,
            
            'maxsleep':100,
            'sleep':100,
            
            'strength':10,
            'agility':10,
            'intelligence':10,
            'stamina':10,
            
            'maxweight':100
        }
    }
           }


#print('7777')
#bot.polling(none_stop=True,timeout=600)

