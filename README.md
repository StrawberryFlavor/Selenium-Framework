# Selenium UI 自动化测试框架（基于python）
框架目录构造：


- **config：**
用来配置浏览器和url



- **framwork：**
	- logger：封装了日志输入，包括文件输出和控制台的输出
	- base_page:封装了selenium库中常用的方法，包括对象查找，截图输出，浏览器的前进后退，清除和输入...
	- browser_engine:通过读取配置文件去选择浏览器和url，并返回浏览器对象实例



- **screenshots：**
接收截图文件的输出



- **logs：**
接收日志文件的输出



- **test_reports：**
测试报告的输出文件夹



- **testsuites：**
集合测试用例



- **tools：**
存放浏览器驱动