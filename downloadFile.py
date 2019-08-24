# -*- coding: UTF-8 -*-
import os,re,urllib,uuid,http.client,urllib.request,ssl

#首先定义云端的网页,以及本地保存的文件夹地址
localPath='/home/zeng/线性代数/'


ssl._create_default_https_context =ssl._create_unverified_context
def gGetFileName(line):
    matchObj = re.search( r'\S+(?=\t)', line, re.I)
    if matchObj:return matchObj.group() + '.mp4'
    
def gGetUrl(line):
    matchObj = re.search( r'http\S+', line,re.I)
    if matchObj:return matchObj.group()

def gDownloadWithFilename(url,savePath,file_para):
    #参数检查，现忽略
    try:
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'If-Modified-Since':'Mon, 08 Jul 2013 18:06:40 GMT',
            'Upgrade-Insecure-Requests':1,
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'}
        # urlopen=urllib.URLopener()
        print("开始下载：" + savePath + file_para)
        fp =urllib.request.urlopen(url)
        data = fp.read()
        fp.close()
        file=open(savePath + file_para,'w+b')
        file.write(data)
        file.close()
        print("完成下载：" + savePath + file_para)
    except IOError as error:
        print("DOWNLOAD {0} ERROR!==>> {1}".format(url, error));
    except Exception as e:
        print("Exception==>>" + e);



f = open("线性代数.txt")             
line = f.readline()
while line:
    # print(line,end = '')
    print(gGetFileName(line))
    print(gGetUrl(line))
    gDownloadWithFilename(gGetUrl(line),localPath,gGetFileName(line))
    line = f.readline()
f.close()




