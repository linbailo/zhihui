import requests
import json
from login.denlu import Denlu

class Pingjiao:
    # 初始化本地登录类
    def __init__(self, denlu: Denlu, userInfo):
        self.pingjiaorn = userInfo['pingjiaonr']
        self.token = denlu.token


    def pj(self):
    	headers = {'token': self.token,'Referer': 'http://wap.gxxd.net.cn/student/signRecord','Content-Type': 'application/json'} 
    	data = {"startDate": "2021-03-1","endDate": "2999-06-26","signStatus": "null","secBegin": "","secEnd": "","content": "","current": 1,"size": 1000000}
    	ro1 = requests.post('http://wap.gxxd.net.cn/business/app/stuClassAttend/getStuClassAttendRecord', headers=headers, data=json.dumps(data))
    	ro1text = ro1.text
    	rojson = json.loads(ro1text)
    	i=0
    	while i <= 1:
    		value = rojson['data']['records'][i]['id']
    		i+=1
    		data = {"id": value,"learnEffect": 0,"interact": 0,"abilityPromote": "0,1,2,3","evaluateComment": self.pingjiaorn,"showNameFlag": 0}
    		headers = {'token': self.token,'Referer': 'http://wap.gxxd.net.cn/student/stuEvaluation?id=2542240','Content-Type': 'application/json'}
    		roo = requests.post('http://wap.gxxd.net.cn/business/app/stuClassAttend/updateAttendScore', headers=headers, data=json.dumps(data))
    		print(roo.text)