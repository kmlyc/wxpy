# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:30:00 2017

@author: Administrator
"""

# 导入模块
import time
from wxpy import *
'''
微信机器人登录有3种模式，
(1)极简模式:robot = Bot()
(2)终端模式:robot = Bot(console_qr=True)
(3)缓存模式(可保持登录状态):robot = Bot(cache_path=True)
'''
# 初始化机器人，选择模式（扫码）登录
robot = Bot()

# 获取好友、群、公众号信息
# robot.chats()

# 获取好友的统计信息
friends = robot.friends()
# print(Friends.stats_text())

with open('stats.txt', 'w', encoding='utf8') as f:
    f.write(friends.stats_text())

time.sleep(1)
robot.logout()
