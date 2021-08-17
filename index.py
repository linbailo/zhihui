import yaml
import requests
import json
import pp
import time

def getYmlConfig():
	file = open('config.yml', 'r', encoding="utf-8")
	file_data = file.read()
	file.close()
	config = yaml.load(file_data, Loader=yaml.FullLoader)
	return dict(config)

def main():
	config = getYmlConfig()
	print(config['zuozhe'])
	for user in config['lin']:
		openId = user['user']['openId']
		qmsg = user['user']['qmsg']
		pingjiao = user['user']['pingjiao']
		zhihui(openId,qmsg,pingjiao)





def zhihui(openId,qmsg,pingjiao):
	datas = {"openId": openId}
	r = requests.post("http://wap.gxxd.net.cn/business/app/sysUser/autoLoginByOpenId", data=datas)
	text = r.text
	data = json.loads(text)
	mz = data['data']['name']
	ttt = data.get("data")
	tttt= ttt.get('token')
	print (tttt)
	
	headers = {'token': tttt}
	roo = requests.get('http://wap.gxxd.net.cn/business/app/stuClassAttend/getStuClassAttend', headers=headers)
	print(roo.text)
	rooo = roo.text
	rojson = json.loads(rooo)
	#id


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

	uurl = 'http://wap.gxxd.net.cn/student/handleSign?signType=0&signStatusName=%E5%BE%85%E7%AD%BE%E5%88%B0&attendId='+str(id)+'&roomId='+str(roomId)+'&location=%E5%B9%BF%E8%A5%BF%E7%8E%B0%E4%BB%A3%E8%81%8C%E4%B8%9A%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2'
	print(uurl)


	headers = {'token': tttt,'Referer': 'http://wap.gxxd.net.cn/student/signRecord','Content-Type': 'application/json'}
	data = {"lat": "24.699269065342","lng": "108.04417468065","roomId": roomId,"attendId": id,"location":"广西现代职业技术学院","signType":0}
	## post的时候，将data字典形式的参数用json包转换成json格式。
	ro = requests.post('http://wap.gxxd.net.cn/business/app/stuClassAttend/codeConfirm', headers=headers, data=json.dumps(data))
	ro1text = ro.text
	rojson = json.loads(ro1text)
	print(rojson)
	headers = {'token': tttt,'Referer': uurl,'Content-Type': 'application/json'} 
	data = {"lat": "24.699201","lng": "108.043722","roomId": roomId,"id": id,"lessonId": lessonId,"signTime": presentTime,"signType": 0,"signRemark": ""}
	## post的时候，将data字典形式的参数用json包转换成json格式。
	ro = requests.post('http://wap.gxxd.net.cn/business/app/stuClassAttend/updateAttendStatus', headers=headers, data=json.dumps(data))
	ro1text = ro.text
	rojson = json.loads(ro1text)
	cg = rojson['msg']
	cgg = rojson["data"]
	print(rojson)
	if(cg == None):
		cggg = mz + '：' + cgg
		sc = f'https://qmsg.zendee.cn/send/{qmsg}?msg={cggg}'
		requests.get(sc)
		print(cggg)

	else:
		cggg = mz + '：' + cg
		sc = f'https://qmsg.zendee.cn/send/{qmsg}?msg={cggg}'
		requests.get(sc)
		print(cggg)
	time.sleep(5)
	pp.pj(tttt,pingjiao)

# 腾讯云函数
def main_handler(event, context):
    main()
    return 'ok'

if __name__ == '__main__':
	main()