import win32con
import win32gui
import time
import os
from selenium import webdriver


class CommonFunction(object):

    # 对浏览器初始化
    def openChrome(self, url):
        chromedriver = "D:\\Google\\Chrome\\Application\\chromedriver.exe"  # Chromedriver路径
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)  # 打开chrome浏览器
        time.sleep(1)
        self.driver.maximize_window()   # 窗口最大化
        self.driver.get(url)    # 输入URL
        time.sleep(2)

    # 关闭浏览器
    def closeChrome(self):
        time.sleep(3)
        self.driver.quit()

    # 获取元素定位
    def getElement(self, attribute, value):    # xpath和css可以直接在chrome中的检查中copy
        if attribute == "id":  # 根据id属性定位
            element = self.driver.find_element_by_id(value)
        elif attribute == "name":  # 根据name属性定位
            element = self.driver.find_element_by_name(value)
        elif attribute == "class":  # 根据class属性定位
            element = self.driver.find_element_by_class_name(value)
        elif attribute == "link":  # 根据文字链接
            element = self.driver.find_element_by_link_text(value)
        elif attribute == "partial":   # 根据文字链接的一部分
            element = self.driver.find_element_by_partial_link_text(value)
        elif attribute == "xpath":  # 根据xpath定位
            element = self.driver.find_element_by_xpath(value)
        elif attribute == "css":  # 根据css选择器定位
            element = self.driver.find_element_by_css_selector(value)
        elif attribute == "tag":   # 根据标签名称
            element = self.driver.find_elements_by_tag_name(value)
        return element

    # 上传附件功能
    def upAttachment(self, name, filePath):
        dialog = win32gui.FindWindow('#32770', name)  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filePath)  # 往输入框输入附件绝对地址
        time.sleep(1)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button上传

