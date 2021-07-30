#!/usr/bin/env python
#coding:utf-8

import sys

from largeXMLDealer import largeXMLDealer


@largeXMLDealer
def XMLParsing(fileName, elemTag):
    print("文件解析结束！")

if __name__ == "__main__":

    fileName = input("请输入XML文件名（建议输入P00734.xml）：")
    elemTag = input("请输入解析元素名：（建议从P00734.xml文件中挑选任意一个标签,比如：accession）")
    XMLParsing(fileName, elemTag)

        
