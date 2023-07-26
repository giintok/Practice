# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:07:18 2023

@author: goldg
"""

import map_module as fun
L = [3, 2, [3, [[3], 4]]]
result = fun.change_values(L, 3, 5)
print(result)
print('===='*10)

result2 = fun.change_values2(L, 3, 5)
print(result2)
