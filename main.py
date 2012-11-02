#!/usr/bin/env python
#coding=utf8


'''Author: Zheng Yi
Email: zhengyi.bupt@qq.com'''


import WeiboCrawl

  
if __name__ == '__main__':
    weiboLogin = WeiboCrawl.WeiboLogin('jwang1835@gmail.com', '5663131')
    if weiboLogin.Login() == True:
        print "The WeiboLogin module works well!"

    #start with my blog :)
    webCrawl = WeiboCrawl.WebCrawl('http://weibo.com/wuyanzu')
    webCrawl.Crawl()
    del webCrawl
