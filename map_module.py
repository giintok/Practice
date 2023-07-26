# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:06:56 2023

@author: goldg
"""

def change_values(data, old_value, new_value):
    for k, ele in enumerate(data):
        if ele == old_value:
            data[k] = new_value
        #print(k, ele)
    return data

def change_values2(data, old_value, new_value):
    for k, ele in enumerate(data):
        #print(k, ele)           #재귀 과정 
        if ele == old_value:
            data[k] = new_value
        elif type(ele) == list:
            change_values2(ele, old_value, new_value)
    return data
