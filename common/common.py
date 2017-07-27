import  requests
import json


def method(url,param,method="post"):
    if method=="post":
        res = requests.post(url ,data=param)
        text = json.loads(res.text)
        status_code = res.status_code
        code = text["code"]
    else:
        res = requests.get(url,data=param)
        text = json.loads(res.text)
        status_code = res.status_code
        code = text["code"]

    return code, status_code