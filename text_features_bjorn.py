#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:01:13 2020

@author: bjrn
"""

import profanity_check as pc
from fuzzywuzzy import fuzz

#empty revision
##checks if edit is is empty or non empty
def empty(text_list):
    if len(text_list) == 0:
        empty = 1
    else:
        empty = 0

    return empty


#ratio between old text and new text; if  > 1 new text is longer than old text
#i would consider it vandal if there is a significant deviation from 1
def size_ratio(old_text_list, new_text_list):
    len_old_text = len(old_text_list)
    len_new_text = len(new_text_list)
    
    ratio = len_new_text / len_old_text
    
    return ratio

#counts the alphanumberic strings in the diffrence list eg (dkfdj125kd,...) the strings with numbers and letters
## Since these strings are likely to be vandal
## Absolute count or ratio better?
def alphanumeric_ratio(difference_list):
    alpha_num = 0
    for element in difference_list:
        alpha_num = 1
        if element.isdigit():
            continue
        elif element.isalpha():
            continue
        else:
            alpha_num += 1
            
    return alpha_num


#ratio of vulgar words in the edit
def vulgar(difference_list, old_text_list):
    vulgar_list_edit = pc.predict(difference_list)
    vulgar_list_old = pc.predict(old_text_list)
    count1 = 0
    count2 = 0
    for i in vulgar_list_edit:
        count1 += i
        
    for k in vulgar_list_old:
        count2 += k
        
    ratio1 = count1 #/ len(difference_list)
    ratio2 = count1 / count2
        
    return ratio1, ratio2


#Gives a simularity metric between original and new text
#How less simular the more suspicous
def simularity(old_text_list, new_text_list):
    old = ''.join(old_text_list)
    print(old)
    new = ''.join(new_text_list)
    ratio = fuzz.token_set_ratio(old, new)
    
    return ratio


