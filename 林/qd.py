import requests
import json
import time
from login.denlu import Denlu

class QD:
    # 初始化本地登录类
    def __init__(self, denlu: Denlu, userInfo):
        self.pingjiaorn = userInfo['pingjiaonr']
        self.token = denlu.token
        self.mz = denlu.mz


    def qdlin(self):
    	headers = {'token': self.token}
    	roo = requests.get('http://wap.gxxd.net.cn/business/app/stuClassAttend/getStuClassAttend', headers=headers)
    	print(roo.text)
    	rooo = roo.text
    	rojson = json.loads(rooo)
    	if(rooo == '{"code":0,"msg":"success","data":null}'):
    		print('没有签到')
    		return('没有签到')
    	id = rojson['data']['id']
    	#教室
    	roomId = rojson['data']['roomId']
    	#lessonId
    	lessonId = rojson['data']['lessonId']
    	#时间
    	presentTime = rojson['data']['presentTime']
    	uurl = f'http://wap.gxxd.net.cn/student/handleSign?signType=0&signStatusName=%E5%BE%85%E7%AD%BE%E5%88%B0&attendId={id}&roomId={roomId}&location=%E5%B9%BF%E8%A5%BF%E7%8E%B0%E4%BB%A3%E8%81%8C%E4%B8%9A%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2'
    	headers = {'token': self.token,'Referer': 'http://wap.gxxd.net.cn/student/signRecord','Content-Type': 'application/json'}
    	data = {"lat": "24.699269065342","lng": "108.04417468065","roomId": roomId,"attendId": id,"location":"广西现代职业技术学院","signType":0}
    	ro = requests.post('http://wap.gxxd.net.cn/business/app/stuClassAttend/codeConfirm', headers=headers, data=json.dumps(data))
    	ro1text = ro.text
    	rojson = json.loads(ro1text)
    	print(rojson)
    	headers = {'token': self.token,'Referer': uurl,'Content-Type': 'application/json'} 
    	data = {"lat": "24.699201","lng": "108.043722","roomId": roomId,"id": id,"lessonId": lessonId,"signTime": presentTime,"signType": 0,"signRemark": ""}
    	ro = requests.post('http://wap.gxxd.net.cn/business/app/stuClassAttend/updateAttendStatus', headers=headers, data=json.dumps(data))
    	ro1text = ro.text
    	rojson = json.loads(ro1text)
    	cg = rojson['msg']
    	cgg = rojson["data"]
    	print(rojson)
    	if(cg == None):
    		cggg = self.mz + '：' + cgg
    		sc = f'https://qmsg.zendee.cn/send/{qmsg}?msg={cggg}'
    		requests.get(sc)
    		print(cggg)
    	else:
    		cggg = self.mz + '：' + cg
    		sc = f'https://qmsg.zendee.cn/send/{qmsg}?msg={cggg}'
    		requests.get(sc)
    		print(cggg)
    	time.sleep(5)