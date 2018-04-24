#_*_ coding:utf-8 _*_

import unittest
import HTMLTestRunner
import os
import time

report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

HtmlFile = report_path+now+"HTMLtemplate.html"

fp = file(HtmlFile, "wb")


if __name__=='__main__':
    suite = unittest.TestLoader().discover("testsuites")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'执行情况')
    runner.run(suite)

