#coding=utf8
 
import http.client
import hashlib
import urllib
import random
import json


#Function take three paremeters and return result; Current language type, Content, and result language type
def translate(fromLang , q, toLang):
    '''Take "From Language", "Content", and "To Language"
                                '''
    appid = '20190717000318689'
    secretKey = 'NxxzLemdsPbLBtT2gTGp'

    httpClient = None
    myurl = '/api/trans/vip/translate'
   
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5(sign.encode())
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        obc = response.read()
        obc = json.loads(obc)
        obc = obc["trans_result"][0]
        dst = obc["dst"]
        return dst
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()

