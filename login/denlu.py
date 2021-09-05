import json
import re
import requests
from bs4 import BeautifulSoup


class Denlu:
    # 初始化本地登录类
    def __init__(self, userInfo):
        self.username = userInfo['username']
        self.password = userInfo['password']
        self.openId = userInfo['openId']
        self.log = userInfo['log']
        self.mz = None
        self.token = None


    def opid(self):
    	datas = {"openId": self.openId}
    	r = requests.post("http://wap.gxxd.net.cn/business/app/sysUser/autoLoginByOpenId", data=datas).text
    	data = json.loads(r)
    	self.mz = data['data']['name']
    	print(self.mz)
    	self.token = data['data']['token']



    def zhanghao(self):
    	xc = requests.session()
    	yz = xc.get(f'http://authserver.gxxd.net.cn/authserver/needCaptcha.html?username={self.username}').text
    	if yz == 'true' :
    		return '账号登录无法登录'
    	qw = xc.get('http://authserver.gxxd.net.cn/authserver/login?service=http://pc.gxxd.net.cn').text
    	soup = BeautifulSoup(qw, 'lxml')
    	xcv = soup.select('input')
    	params={}
    	for oo in xcv:
    		params[oo.get('name')] = oo.get('value') 
    	params['username'] = self.username
    	params['password'] = self.password
    	de = xc.post('http://authserver.gxxd.net.cn/authserver/login?service=http%3A%2F%2Fpc.gxxd.net.cn', params=params, allow_redirects=False)
    	if de.status_code == 302 :
    		jump_url = de.headers['Location']
    		host = re.findall('ticket=.*',jump_url)[0]
    		cvcv = f'http://pc.gxxd.net.cn/business/cas/client/validateLogin/pc?{host}&service=http:%2F%2Fpc.gxxd.net.cn'
    		qwe = xc.get(cvcv).json()
    		self.mz = qwe['data']['name']
    		self.token = qwe['data']['token']
    		return f'{self.mz}:登陆成功'
    	else:
    		return '登录失败'
    

    # 本地化登陆
    def login(self):
        # 获取登录方式
        if self.log == 1 :
        	msg = self.zhanghao()
        	return msg
        elif self.log == 2 :
        	msg = self.opid()
        	return msg
        else:
        	print('获取登录方式失败')
