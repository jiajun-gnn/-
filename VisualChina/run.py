import json
import requests
import os
import csv
def get_img(key,out,nums):
    cnt = 0
    for i in range(1,10000):
        payload={
        "editorialPafilter": "all",
        "intlNews": "false",
        "ip": "103.107.216.236",
        "isAsync": "true",
        "page": "1000000",
        "phrase": "姚明",
        "political_access": "true",
        "rand": "68RI93_7cc6e32c7e1c57d4b6898543e8f8b8ba",
        "search": "new",
        "sort": "quality"
        }
        payload["page"] = str(i)
        payload["phrase"] = key
        postUrl = 'https://www.cfp.cn/ajax/search/getEditorialImageList'
        payloadHeader = {
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "70",
                "Content-Type": "application/json;charset=UTF-8",
                'Content-Type': 'application/json;charset=UTF-8'
        }    
        r = requests.post(postUrl, json=payload, headers=payloadHeader)
        res = r.text
        j_res = json.loads(res)
        if j_res["data"]["total_count"] == 0:
            break
        img_list = j_res["data"]["list"]
        for item in img_list:
            id_ = item["id"]
            title = item["title"]
            category = item["category"]
            caption = item["caption"]
            onlinetime = item["onlineTime"]
            uploadtime = item["uploadTime"]
            createdTime = item["createdTime"]
            imgurl = item["url800"]
            cnt += 1
            temp = {
                "id_":str(id_),
                "title":title, #图片标题
                "category":category, #图片分类
                "caption":caption, #图片描述
                "onlinetime":onlinetime, #图片上传时间
                "createdTime":createdTime, #图片发布时间
                "imgurl":imgurl #图片url
            }
            if cnt == nums:
                return 
            img = requests.get("https:"+imgurl)
            if not os.path.exists(os.path.join(out,key)):
                os.mkdir(os.path.join(out,key))
            with open(os.path.join(out,key,"%s.jpg"%(str(cnt))),"wb")as f:
                f.write(img.content)
            with open(os.path.join(out,key,"desc.csv"),"a+",newline = "")as f1:
                a = csv.writer(f1)
                a.writerow(temp.values())
            print(id_,title,category,caption,onlinetime,uploadtime,createdTime,imgurl)
if __name__ == "__main__":
    query = "姚明"
    get_img(query,"./",20)  