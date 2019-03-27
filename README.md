# Selenium UI 自动化测试框架（基于python）
## 框架目录构造： ##


- **[config](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/config)**： 用来存储配置文件，如 [config.ini](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/config/config.ini) 文件，配种了所需浏览器方式及被测地址

- **[framwork](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/framework)**：框架底层封装层，可以根据自己的想法封装底层方法
  - *[logger.py](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/framework/logger.py)*：封装了日志输入，包括文件输出和控制台的输出
  - *[base_page](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/framework/base_page.py)*：封装了selenium库中常用的方法，包括对象查找，截图输出，浏览器的前进后退，清除和输入
  - *[browser_engine](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/framework/browser_engine.py)*：通过读取配置文件去选择浏览器和url，并返回浏览器对象实例


- **[screenshots](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/screenshots)**：用于接收测试过程中错误截图文件

- **[logs](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/logs)**：用于接收日志文件的输出 


- **[pageobjects](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/pageobjects)**：用于封装页面对象，[百度首页示例](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/pageobjects/baidu_homepage.py)

- **[test_report](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/test_report)**：用于接收测试报告文件的输出


- **[testsuites](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/testsuites)**：用于测试用例的存放和用例集合套件 ，示例：*[TestRunner.py](https://github.com/StrawberryFlavor/Selenium-Framework/blob/master/testsuites/TestRunner.py)*


- **[tools](https://github.com/StrawberryFlavor/Selenium-Framework/tree/master/tools)**：用于存放浏览器的 selenium 驱动

