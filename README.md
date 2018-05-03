# Selenium UI 自动化测试框架（基于python）
## 框架目录构造： ##


- **[config](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/config)：** 
*[config.ini](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/config/config.ini)*：文件用来配置浏览器和url



- **[framwork](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/framework)：**
	- *[logger.py](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/framework/logger.py)*：封装了日志输入，包括文件输出和控制台的输出
		![logger封装](http://p4uuxwp7i.bkt.clouddn.com/logger%E8%B4%B4%E5%9B%BE.png)
	- *[base_page](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/framework/base_page.py)*:封装了selenium库中常用的方法，包括对象查找，截图输出，浏览器的前进后退，清除和输入...
		![基础方法的二次封装](http://p4uuxwp7i.bkt.clouddn.com/bage%E6%98%BE%E7%A4%BA.png)
	- *[browser_engine](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/framework/browser_engine.py)*:通过读取配置文件去选择浏览器和url，并返回浏览器对象实例
		![浏览器引擎类封装](http://p4uuxwp7i.bkt.clouddn.com/browser%E6%98%BE%E7%A4%BA.png)


- **[screenshots](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/screenshots)：**
接收截图文件的输出



- **[logs](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/logs)：**
接收日志文件的输出


- **[pageobjects](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/pageobjects):**
用于封装页面对象，百度首页示例：*[baidu_homepage.py](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/pageobjects/baidu_homepage.py)*

- **[test_report](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/test_report)：**
测试报告的输出文件夹


- **[testsuites](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/testsuites)：**
用于测试用例的存放和测试用例集合，示例：*[TestRunner.py](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/testsuites/TestRunner.py)*
	![测试集合](http://p4uuxwp7i.bkt.clouddn.com/%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A%E6%98%BE%E7%A4%BA.png)


- **[tools](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/tools)：**
存放浏览器驱动
	