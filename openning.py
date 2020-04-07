from datetime import datetime
import requests
import json


def show_robot():
	print('''
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]''')
	print('------------------------')
	print('''欢迎使用小夏机器人0.9版本''')
	print('------------------------')




def hello(name):
	print(f"你好{name}，我是'小夏'，很高兴认识你啊!")


def ask():
	name=input('我是小夏，我该怎么称呼你？\n')
	age=int(input('你多大了？\n'))

	if (age<=12):
		print('小孩子，要好好学习啊!')
	elif age<=18:
		print('这个年龄会遇到你一生中最难忘的人，要好好珍惜啊！')
	elif age<=30:
		print('买房了吗朋友？')
	elif age<=45:
		print('我喜欢成熟的人')
	else:
		print('你一定很幸福吧')
	return name


def show_time():
		dt=datetime.now()#调取一个现在是时间
		print(f'今天是{dt.year}年{dt.month}月{dt.day}日 现在是{dt.hour}：{dt.minute}：{dt.second}')

def ai_talk(question):
	return question.replace('你','我').replace('不','').replace('吗','').replace('？','！').replace('?','！')

def tianqi():
	print('''作者开发能力有限，目前默认给出北京的天气状况，后续开发将会支持指定城市查询
		大佬勿喷啊嘤嘤嘤~~~''')
	url='http://t.weather.sojson.com/api/weather/city/101010100'
	res=requests.get(url)
	tq_text=res.text
	tq_json=json.loads(tq_text)
	wendu=tq_json['data']['wendu']
	pm25=tq_json['data']['pm25']
	print(f'北京今天{wendu}摄氏度,PM2.5指数为{pm25}')