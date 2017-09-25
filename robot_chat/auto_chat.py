# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:53:54 2017

@author: Administrator
"""

# 导入模块
from configparser import ConfigParser
from wxpy import *
'''
微信机器人登录有3种模式，
(1)极简模式:robot = Bot()
(2)终端模式:robot = Bot(console_qr=True)
(3)缓存模式(可保持登录状态):robot = Bot(cache_path=True)
'''
# 初始化机器人，选择模式（扫码）登录
robot = Bot(cache_path=True)
robot.enable_puid()
# 获取配置文件中api_key
cf = ConfigParser()
cf.read("api_key")
api_key = cf.get('KEY', 'api_key')
print(api_key)
tuling = Tuling(api_key=api_key)
uid_list = []


# 获取自己的历史消息
# history_msgs = robot.messages.search(sender=robot.self)


# 自动回复所有文字消息
@robot.register(msg_types=TEXT)
def auto_reply_all(msg):
    # print(msg)
    sender_id = msg.sender.puid
    # 如果是群聊，但没有被 @，则不回复
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        if sender_id not in uid_list:
            uid_list.append(sender_id)
            msg.reply('主人不在，我是他的私人小助理。我上知天文下知地理，要不我陪你聊会儿[耶]')
        else:
            tuling.do_reply(msg)


# 自动回复所有图片消息
@robot.register(msg_types=PICTURE)
def auto_repy_pic(msg):
    pass


# 开始运行
robot.join()
