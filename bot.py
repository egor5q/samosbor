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

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


client=MongoClient(os.environ['database'])
db=client.samosbor
users=db.users
codes = db.codes
if codes.find_one({}) == None:
    codes.insert_one({'code':0})
    
locs = {
    'testloc1':{
        'name':'Тест1',
        'id':-10035294,
        'items':{},
        'nearlocs':[]
    }

}

    
@bot.message_handler(commands=['move'])
def moveeee(m):
    pass
    

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


print('7777')
bot.polling(none_stop=True,timeout=600)

