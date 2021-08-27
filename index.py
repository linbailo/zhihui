import yaml
import requests
import json
from bs4 import BeautifulSoup
from login.denlu import Denlu
from lin.pingjiao import Pingjiao
from lin.qd import QD

def getYmlConfig():
	file = open('config.yml', 'r', encoding="utf-8")
	file_data = file.read()
	file.close()
	config = yaml.load(file_data, Loader=yaml.FullLoader)
	return dict(config)

def main():
	config = getYmlConfig()
	print(config['zuozhe'])
	for den in config['lin']:
		try:
			li(den)
		except Exception as e:
			print(e)


def li(den):
	denlu = Denlu(den['user'])
	denlu.login()
	print(denlu.login())
	if denlu.login() == '登录失败' :
		return '登录失败'
	qing = QD(denlu, den['user'])
	qing.qdlin()
	if den['user']['pjpj'] == 1 :
		ping = Pingjiao(denlu, den['user'])
		ping.pj()
	else:
		return '已设置不评教'
		

# 阿里云的入口函数
def handler(event, context):
    main()

# 腾讯云函数
def main_handler(event, context):
    main()
    return 'ok'

if __name__ == '__main__':
	main()