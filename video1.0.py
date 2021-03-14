from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class strong_country(object):

    def __init__(self):
        self.option = webdriver.ChromeOptions()

        self.option.add_argument(
            r"user-data-dir=F:\Chrome\User Data")  # 加载前面获取的 个人资料路径

        # self.option.add_argument(
        #     r"user-data-dir=C:\Users\DMJ\AppData\Local\Google\Chrome\User Data")  # 加载前面获取的 个人资料路径

        # self.option.add_argument(
        #     r"user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")  # 加载前面获取的 个人资料路径

        # self.option.add_argument(
        #     r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")

        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.driver = webdriver.Chrome(options=self.option,
                                       executable_path=r"F:\Chrome\Application"r"\chromedriver")

        # self.driver = webdriver.Chrome(options=self.option,
        #                                executable_path=r"C:\Users\DMJ\AppData\Local\Google\Chrome\Application"r"\chromedriver")

        # self.driver = webdriver.Chrome(options=self.option,
        #                               executable_path=r"C:\Program Files\Google\Chrome\Application"r"\chromedriver")

        # self.driver = webdriver.Chrome(options=self.option,
        #                                executable_path=r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application"r"\chromedriver")

    def video(self):

        self.driver.get("https://pc.xuexi.cn/points/login.html?ref=https%3A%2F%2Fwww.xuexi.cn%2F")
        while 1:
            try:
                if self.driver.find_element_by_xpath(
                        '//*[@id="root"]/div/header/div[2]/div[2]/span/span').text == '您好，欢迎您':
                    break
            except NoSuchElementException:
                print("请登录")

        self.driver.quit()

        self.driver = webdriver.Chrome(options=self.option,
                                       executable_path=r"F:\Chrome\Application"r"\chromedriver")

        # self.driver.get("https://www.xuexi.cn/xxqg.html?id=c7c3b74e1887422c9733b0d22bf25498")
        #
        # time.sleep(5)
        #
        # start = int(time.time())
        #
        # flag = 0
        #
        # Sum = 0
        #
        # for i in range(4):
        #     if flag == 0:
        #         for j in range(4):
        #             if flag == 0:
        #                 now = int(time.time())
        #                 # 6分钟 360s 打开网页会耽误点时间所以给400s
        #                 if now - start <= 400 or Sum < 6:
        #                     video = self.driver.find_element_by_xpath(
        #                         '//*[@id="6231cc81a4"]/div/div/div/div/div/div/section/div/div/div/div[{}]/div[{}]/div/div[1]/div[1]/span/div'.format(
        #                             i + 1, j + 1))
        #                     video_length = self.driver.find_element_by_xpath(
        #                         '//*[@id="6231cc81a4"]/div/div/div/div/div/div/section/div/div/div/div[{}]/div[{}]/div/div[1]/div[2]/span[2]'.format(
        #                             i + 1, j + 1)).text
        #                     m, s = video_length.strip().split(':')
        #                     seconds = int(m) * 60 + int(s)
        #                     video.click()
        #                     time.sleep(seconds+5)
        #                     Sum = Sum + 1
        #                 else:
        #                     flag = 1
        # 
        # self.driver.quit()

        # time.sleep(3)
        #
        # self.driver = webdriver.Chrome(options=self.option,
        #                                executable_path=r"F:\Chrome\Application"r"\chromedriver")

        self.driver.get("https://www.xuexi.cn/7097477a9643eacffe4cc101e4906fdb/9a3668c13f6e303932b5e0e100fc248b.html")

        time.sleep(3)

        for i in range(10):
            handle = self.driver.window_handles
            self.driver.switch_to.window(handle[0])
            time.sleep(1)

            read = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/section/div/div/div/div/div/section/div/div/div'
                '/div[1]/div/section/div/div/div/div/div/section/div/div/div/div/div['
                '3]/section/div/div/div/div/div/section/div/div/div[1]/div/div[{}]/div/div/div[1]/span'.format(
                    i + 1))
            read.click()

            handle = self.driver.window_handles
            self.driver.switch_to.window(handle[i + 1])
            for j in range(20):
                if j % 2 == 0:
                    js = "window.scrollTo(0,0)"
                else:
                    js = "window.scrollTo(0,document.body.scrollHeight)"
                self.driver.execute_script(js)
                time.sleep(3)

        time.sleep(20)
        self.driver.quit()

    def main(self):

        self.video()


if __name__ == '__main__':
    ABC = strong_country()
    ABC.main()
