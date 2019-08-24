# -*- coding: UTF-8 -*-
import os,re,urllib,uuid,httplib

#首先定义云端的网页,以及本地保存的文件夹地址
urlPath='http://gamebar.com/'
localPath='/home/zeng/pythonPath'


#从一个网页url中获取图片的地址，保存在
#一个list中返回
def getUrlList(urlParam):
    urlStream=urllib.urlopen(urlParam)
    htmlString=urlStream.read()
    if( len(htmlString)!=0 ):
        patternString=r'http://.{0,5000}\.gif'
        searchPattern=re.compile(patternString)
        imgUrlList=searchPattern.findall(htmlString)
        return imgUrlList


    #生成一个文件名字符串
def generateFileName():
    return str(uuid.uuid1())


#根据文件名创建文件
def createFileWithFileName(localPathParam,fileName):
    totalPath=localPathParam+'/'+fileName
    if not os.path.exists(totalPath):
        file=open(totalPath,'a+')
        file.close()
        return totalPath


    #根据图片的地址，下载图片并保存在本地
def getAndSaveImg(imgUrl):
    if( len(imgUrl)!= 0 ):
        print imgUrl;
        fileName=generateFileName()+'.jpg';
        urllib.urlretrieve(imgUrl,createFileWithFileName(localPath,fileName));





    #下载函数
def downloadImg(url):
    urlList=getUrlList(url)
    for urlString in urlList:
        print urlString;
        gDownload(urlString,localPath);
    #getAndSaveImg(urlString);

#"""根据url获取文件名"""
def gGetFileName(url):
    if url==None: return None
    if url=="" : return ""
    arr=url.split("/")
    return arr[len(arr)-1]

#"""根据url下载文件，文件名参数指定"""
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
        urlopen=urllib.URLopener()
        fp = urlopen.open(url)
        #data = fp.read()
        #fp.close()

        #conn = httplib.HTTPConnection(url);
        #conn.request("GET", "");
        #fp = conn.getresponse();

        data = fp.read();
        fp.close();
        file=open(savePath + file_para,'w+b');
        file.write(data);
        file.close();
    except IOError, error:
        print "DOWNLOAD %s ERROR!==>>%s" % (url, error);
    except Exception, e:
        print "Exception==>>" + e;


    #"""根据url下载文件，文件名自动从url获取"""
def gDownload(url,savePath):
    #参数检查，现忽略
    fileName = gGetFileName(url);
    #fileName =gRandFilename('jpg')
    gDownloadWithFilename(url,savePath,fileName);

downloadImg('http://www.xieexiu.org/list3-1.html');
