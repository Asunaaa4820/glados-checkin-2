import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]
# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]
#'SCT85922TmcoDs8rBfknBAv407MUW3oqb'
# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]
#'__cfduid=d3459ec306384ca67a65170f8e2a5bd561593049467;_ga=GA1.2.1902388494.1629209614; koa:sess=eyJ1c2VySWQiOjU4NzYyLCJfZXhwaXJlIjoxNjU1MTI5NjM3MjAwLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=wVmTzQYg-C-24tCqDbShd3CWWaI; _gid=GA1.2.612119786.1641618794; _gat_gtag_UA_104464600_2=1'



def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()

    
