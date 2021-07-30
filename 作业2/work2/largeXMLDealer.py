#!/usr/bin/env python
#coding:utf-8


from lxml import etree
from os import path


class largeXMLDealer:


    def __init__(self, func):
        self._func = func
    def __call__(self, *args, **kwargs):
        if len(args) == 2:
            print("执行命令: python3 largeXMLParse.py " + args[0] + " " + args[1])
            print("输出:")
            # lxmld = largeXMLDealer.largeXMLDealer(hi)
            count = self.parse(args[0], args[1])
            print("已经解析了 %d 个XML %s 元素." % (count, args[1]))
        else:
            print("参数错误！")
        return self._func(*args, **kwargs)
        
    #----------------------------------------------------------------------
    def parse(self, fileName, elemTag):
        """"""
        if(not path.isfile(fileName) or not fileName.endswith("xml")):
            raise FileNotFoundError   

        count = 0
        es = ('end',)
        ns = self._getNamespace(fileName)
        ns = "{%s}"%ns

        context = etree.iterparse(fileName,events=es, tag=ns+elemTag)
        
        for event, elem in context:
            # Call the outside function to deal with the element here
            try:
                self.func4Element(elem)

            except Exception:
                raise Exception("Something wrong in function parameter: func4Element")
            finally:
                elem.clear()
                count = count + 1
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
        del context         
        # Return how many elements had been parsed
        return count
          
    #----------------------------------------------------------------------
    def _getNamespace(self, fileName):
        """"""
        if(not path.isfile(fileName) or not fileName.endswith("xml")):
            raise FileNotFoundError 
        result = ''
        es = ('start-ns',)
        context = etree.iterparse(fileName,events=es) 
        for event, elem in context:
            prefix, result = elem
            #print("%s, %d"%(elem, len(elem)))
            break
        del context
        return result

    def func4Element(self, elem):
        if isinstance(elem, object):
            print(elem.text)

    




