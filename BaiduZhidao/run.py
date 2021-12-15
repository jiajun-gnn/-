import os
from tqdm import *
import requests
from urllib import parse
from bs4 import BeautifulSoup
import time
def get_title(keyword,index):
    print("正在检索关键字“ " + keyword + " ”的数据...")
    url1 = "https://zhidao.baidu.com/search?"
    url2 = parse.urlencode({'word': keyword})
    url = url1 + url2
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Referer': 'https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=%D1%F8%D6%B3+%B2%A1+%D3%E3+%CF%BA',
        'Cookie': 'BAIDUID=C390DB92EF88CFB106F1D057B3A2CCE9:FG=1; BIDUPSID=C390DB92EF88CFB106F1D057B3A2CCE9; PSTM=1539307711; BDUSS=5aY0h4SDdiOHZUZHpVeXZDRWwwaldzVnpnWWtmT0s4NXNoWTdsVWJnfkVZOEZjQVFBQUFBJCQAAAAAAAAAAAEAAAA7tE8MbGl1YW9kaQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMTWmVzE1plcVm; H_WISE_SIDS=114178; MCITY=-131%3A; H_PS_PSSID=1425_21122_29522_29519_29098_29567_29221_26350; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1565265308,1565787543,1566264896,1566283192; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1566302478; ZD_ENTRY=empty; delPer=0; PSINO=2',
        'Connection': 'keep-alive'
    }
    try:
        response = requests.get(url, headers=HEADERS)
        text = response.content.decode('gbk')
        bs = BeautifulSoup(text,"lxml")
        for tag in bs.find_all(class_="dt mb-3 line"):
            with open("./data/query_%s.txt"%str(index),"a+",encoding="utf8")as f:
                f.write(tag.text.strip()+"\n")
    except:
        time.sleep(5)

if __name__ == "__main__":
    f = open("./query.txt",encoding="utf8")
    cnt = 0
    if not os.path.exists("./data"):
        os.mkdir("./data")
    for l in tqdm(f):
        get_title(l.strip(),cnt)
        cnt += 1
        time.sleep(3)