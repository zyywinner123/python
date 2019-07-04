# #-*- coding: UTF-8 -*-
# import sys
# import pyttsx
#
# sys.setdefaultencoding("utf-8")
#
# text = u'你好，中文测试'
# engine = pyttsx.init()
# engine.
# engine.say(text)
# engine.runAndWait()


#-*-coding:utf8-*-
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("这是一篇简单的Python文字（汉字）转语音教程，当然对于其他语言工具在实现的方法上也是一样的 。")