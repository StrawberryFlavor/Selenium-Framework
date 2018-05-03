# Selenium UI 自动化测试框架（基于python）
## 框架目录构造： ##


- ###**config：**
用来配置浏览器和url



- ###**framwork：**
	- **logger**：封装了日志输入，包括文件输出和控制台的输出
		![logger封装](http://p4uuxwp7i.bkt.clouddn.com/logger%E8%B4%B4%E5%9B%BE.png)
	- **base_page**:封装了selenium库中常用的方法，包括对象查找，截图输出，浏览器的前进后退，清除和输入...
		![基础方法的二次封装](http://p4uuxwp7i.bkt.clouddn.com/bage%E6%98%BE%E7%A4%BA.png)
	- **browser_engine**:通过读取配置文件去选择浏览器和url，并返回浏览器对象实例
		![浏览器引擎类封装](http://p4uuxwp7i.bkt.clouddn.com/browser%E6%98%BE%E7%A4%BA.png)


- ###**screenshots：**
接收截图文件的输出



- ###**logs：**
接收日志文件的输出



- ###**test_reports：**
测试报告的输出文件夹



- ###**testsuites：**
集合测试用例
	![测试集合](http://p4uuxwp7i.bkt.clouddn.com/%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A%E6%98%BE%E7%A4%BA.png)


- ###**tools：**
存放浏览器驱动
	