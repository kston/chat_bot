import numpy as np
import tensorflow as tf
import re
import time 



## DATA PREPROCESSING ##

#Importing the dataset

lines = open('./data/movie_lines.txt', encoding='utf-8', errors= 'ignore').read().split('\n')

conversations = open('./data/movie_conversations.txt', encoding='utf-8', errors= 'ignore').read().split('\n')


# creating  a dict that maps each line and its id


id2line = {}

for line in lines:
    _line = line.split('+++$+++')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]    
        
        
        
# creating list of all conversations 

conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")
    conversations_ids.append(_conversation.split(','))
    
    
    
    
    
    