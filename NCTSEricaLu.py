
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
#簡易版笑話機器人#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

print('聽個笑話，放鬆一下吧!')
eggs = " " 
while eggs !='笑話': 
    eggs = input('>>')
    if eggs =='bye': 
        print('Bye bye!')#當輸入bye會回覆byebye
    elif'哈哈'in eggs:
        print('喜歡的話，分享出去吧!') #如果輸入哈哈會顯示喜歡的話，分享出去吧!
    else:
        print (random.choice(['有一天有一位型男走在路上，一個阿嬤突然上前搭訕:「帥哥，你超會搭耶」，然後帥哥就冒煙了',
                              '川普壓馬路=壓馬路普',
                              '有一天小明去圖書館，小明：我要一碗牛肉麵;櫃檯：先生 這裡是圖書館，小明：喔喔好 （氣音）我要一碗牛肉麵',
                              '哈利波特裡面誰最有主見？  A:佛地魔， 因為他不會被牽著鼻子走',
                              '液晶的媽媽叫什麼名字？ 液晶螢幕......']))
  #其他回應則是會隨機選出笑話來

