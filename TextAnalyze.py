#!/usr/bin/env python
#coding=utf8


'''Author: Zheng Yi
Email: zhengyi.bupt@qq.com'''


def textTransfer(htmlContent):
    "Decode the main part of html"

    line = textExtract(htmlContent)
    print 'line:', line
    if line != None:
        transText = textTransfer(line)
        return transText
    else:
        return None


def textExtract(htmlContent):
    "Extract the main part from html"

    lines = htmlContent.splitlines()
    for line in lines:
        if line.startswith('<script>STK && STK.pageletM && STK.pageletM.view({"pid":"pl_content_[homeFeed|hisFeed]"'):
            return line
        else:
            return None


def textTransfer(line):
    "Decode the main part"
    
    iText = line.find('html":"')
    if iText > 0:
        transText = line[iText + 7: -12].encode("utf-8").decode('unicode_escape').encode("utf-8").replace("\\", "")
        return transText
    else:
        return None

