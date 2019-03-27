# coding=utf-8
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    # input_box = "id=>kw"
    # search_submit_btn = "xpath=>//*[@id='su']"
    # # 百度新闻入口
    # news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"
    # 更改了封装查找元素的方法
    input_box = (By.ID,'kw')
    search_submit_btn = (By.XPATH,'//*[@id="su"]')
    news_link =(By.XPATH,'//*[@id="u1"]/a[@name="tj_trnews"]')

    def type_search(self, text):
        self.type(*self.input_box, text)

    def send_submit_btn(self):
        self.click(*self.search_submit_btn)

    def click_news(self):
        self.click(*self.news_link)
        self.sleep(2)