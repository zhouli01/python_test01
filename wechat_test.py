# _*_ coding:utf-8 _*_
# __author__='小火'
import re
import time
import itchat
from itchat.content import *


@itchat.msg_register([TEXT])
def text_reply(msg):
	friend = itchat.search_friends(userName=msg['FromUserName'])
	replyContent = "收到您于%s发送的【%s】" % (time.strftime('%m-%d %H:%M', time.localtime()), msg['Type'])


if msg['Type'] == 'Text':
	if re.search(r"快乐", msg['Content']):
		replyContent += "【衷心感谢您的祝福,祝您：新年快乐😊😊😊,开开心心[耶][耶][耶],身体健康[發][發][發],狗年大吉旺旺旺🐶🐶🐶】"
		itchat.send('@img@%s' % '/Users/xxx/moneyGod.jpg', toUserName=msg['FromUserName'])
		itchat.send("好友:【%s（昵称：%s）】于：【%s】发来消息: 【%s】" % (
		friend['NickName'], friend['RemarkName'], time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), msg['Text']),
					toUserName='filehelper')
		itchat.send(replyContent, toUserName=msg['FromUserName'])
print("于【%s】收到好友【%s（昵称：%s）】发来的【%s】: 【%s】" % (
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), friend['NickName'], friend['RemarkName'], msg['Type'],
msg['Content']))
print("于【%s】回复：%s" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), replyContent) + '\n')
itchat.auto_login(hotReload=True)
itchat.run()
