from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class strong_country(object):

    def __init__(self):
        self.num = 0

        self.option = webdriver.ChromeOptions()

        self.option.add_argument(
            r"user-data-dir=F:\Chrome\User Data")  # 加载前面获取的 个人资料路径

        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.driver = webdriver.Chrome(options=self.option,
                                       executable_path=r"F:\Chrome\Application"r"\chromedriver")

    def solve(self):
        self.num = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/span').text

        print(self.num)

        try:
            tips = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span')
        except NoSuchElementException:
            tips = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[4]/span')

        tips.click()

        time.sleep(2)

        question = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[1]').text

        print(question)

        if question == '填空题':
            j = 1
            # red = self.driver.find_element_by_xpath(
            #     '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font').text
            try:
                # red = self.driver.find_element_by_xpath('//div[@class = "line-feed"]//font[@color = "red"]').text
                red = []
                for i in self.driver.find_elements_by_xpath(
                        '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font'):
                    red.append(self.driver.find_element_by_xpath(
                        '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font[{}]'.format(j)).text)
                    j = j + 1
                content = self.driver.find_element_by_xpath(
                    '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text
            except NoSuchElementException:
                content = self.driver.find_element_by_xpath(
                    '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text
            print(red)
            print(content)
            # if 1:
            if content in '请观看视频':
                return 0

            else:
                tips.click()

                time.sleep(2)

                i = 1
                # block = self.driver.find_element_by_xpath(
                #     '//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input').send_keys(red)
                for item in self.driver.find_elements_by_xpath(
                        '//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input'):
                    self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input[{}]'.format(i)).send_keys(
                        red[i - 1])
                    time.sleep(2)

                    i = i + 1

            return 1
        elif question == '单选题':

            red = self.driver.find_element_by_xpath(
                '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font').text
            content = self.driver.find_element_by_xpath(
                '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text

            print(red)
            print(content)

            tips.click()

            time.sleep(2)

            a = self.driver.find_elements_by_xpath('//div[@class="q-answer choosable"]')

            for tmp in a:
                if tmp.text[3:] == red:
                    tmp.click()
                    time.sleep(1)
                    return 1
            for tmp in a:
                if tmp.text[3:] in content:
                    tmp.click()
                    time.sleep(1)
                    return 1
            return 0
        elif question == '多选题':

            content = self.driver.find_element_by_xpath(
                '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text

            print(content)

            tips.click()

            time.sleep(2)

            a = self.driver.find_elements_by_xpath(
                '//div[@class="q-answer choosable"]')

            for tmp in a:
                if tmp.text[3:] in content:
                    tmp.click()
                    time.sleep(1)

            return 1

    def solve2(self):

        self.num = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/span').text

        print(self.num)

        try:
            tips = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[3]/span')
        except NoSuchElementException:
            tips = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[4]/span')

        tips.click()

        time.sleep(2)

        question = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[1]').text

        print(question)

        if '填空题' in question:
            j = 1
            try:
                # red = self.driver.find_element_by_xpath('//div[@class = "line-feed"]//font[@color = "red"]').text
                red = []
                for i in self.driver.find_elements_by_xpath(
                        '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font'):
                    red.append(self.driver.find_element_by_xpath(
                        '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font[{}]'.format(j)).text)
                    j = j + 1
                content = self.driver.find_element_by_xpath(
                    '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text
            except NoSuchElementException:
                content = self.driver.find_element_by_xpath(
                    '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text

            print(red)
            print(content)
            if content in '请观看视频':
                return 0

            else:
                i = 1
                # block = self.driver.find_element_by_xpath(
                #     '//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input').send_keys(red)
                for item in self.driver.find_elements_by_xpath(
                        '//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[2]/div/input'):
                    self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[2]/div/input[{}]'.format(i)).send_keys(
                        red[i - 1])
                    time.sleep(2)
                    i = i + 1
            return 1

        elif '单选题' in question:

            red = self.driver.find_element_by_xpath(
                '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font').text

            content = self.driver.find_element_by_xpath(
                '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text
            print(red)
            print(content)
            tips.click()

            time.sleep(2)

            a = self.driver.find_elements_by_xpath('//div[@class="q-answer choosable"]')

            for tmp in a:
                if tmp.text[3:] == red:
                    tmp.click()
                    time.sleep(1)
                    return 1
            for tmp in a:
                if tmp.text[3:] in content:
                    tmp.click()
                    time.sleep(1)
                    return 1
            return 0

        elif '多选题' in question:
            content = self.driver.find_element_by_xpath(
                '//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text

            print(content)

            j = 1

            tips.click()

            time.sleep(2)

            a = self.driver.find_elements_by_xpath(
                '//div[@class="q-answer choosable"]')

            for tmp in a:
                if tmp.text[3:] in content:
                    tmp.click()
                    time.sleep(1)

            return 1

    def part_1(self):
        day_question = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[5]/div[1]')

        day_question.click()

        time.sleep(2)

        for i in range(5):

            if self.solve() == 1:

                next_button = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button')

                next_button.click()

                time.sleep(2)
            else:
                while 1:
                    try:
                        if self.driver.find_element_by_xpath(
                                '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/span').text != self.num:
                            break
                    except NoSuchElementException:
                        break

    def part_2(self):

        week_question = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[5]/div[2]')

        week_question.click()

        time.sleep(2)

        flag = 0
        i = 1
        j = 1
        for x in range(2):
            a = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div/div')
            for item in a:
                if flag == 1: break
                b = self.driver.find_elements_by_xpath(
                    '//*[@id="app"]/div/div[2]/div/div[4]/div/div[{}]/div[2]/div'.format(i))
                for item2 in b:
                    week_question = self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div/div[2]/div/div[4]/div/div[{}]/div[2]/div[{}]/button'.format(i, j))
                    if week_question.text == '开始答题' or week_question.text == '继续答题':
                        week_question.click()
                        time.sleep(2)
                        for s in range(5):
                            if self.solve() == 1:

                                next_button = self.driver.find_element_by_xpath(
                                    '//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button')

                                next_button.click()

                                time.sleep(2)
                            else:
                                while 1:
                                    try:
                                        if self.driver.find_element_by_xpath(
                                                '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/span').text != self.num:
                                            break
                                    except NoSuchElementException:
                                        break
                        flag = 1
                        break
                    j = j + 1
                j = 1
                i = i + 1
            i = 1
            if flag == 1: break
            next_button = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div/div[5]/ul/li[5]/a')

            next_button.click()

            time.sleep(3)

    def part_3(self):
        special_question = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[5]/div[3]')

        special_question.click()

        time.sleep(2)

        i = 1
        flag = 0
        a = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div/div/div/div')

        for x in range(7):
            for item in a:
                if flag == 1: break
                special_question = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/div/div[4]/div/div/div/div[{}]/div[2]/button'.format(i))

                if special_question.text == '开始答题' or special_question.text == '继续答题' or special_question.text == '重新答题':

                    special_question.click()

                    time.sleep(2)

                    b = self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div/div[2]/div/div[4]/div[2]/span').text

                    for i in range(10 - int(b, 10) + 1):

                        if self.solve2() == 1:

                            next_button = self.driver.find_element_by_xpath(
                                '//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button')

                            next_button.click()

                            time.sleep(2)

                        else:
                            while 1:
                                try:
                                    if self.driver.find_element_by_xpath(
                                            '//*[@id="app"]/div/div[2]/div/div[4]/div[2]/span').text != self.num:
                                        break
                                except NoSuchElementException:
                                    break

                    try:
                        submit = self.driver.find_element_by_xpath(
                            '//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button[2]')

                        submit.click()

                        time.sleep(2)
                    except NoSuchElementException:
                        while 1:
                            try:
                                if self.driver.find_element_by_xpath(
                                        '//*[@id="app"]/div/div[2]/div/div[4]/div[2]/span').text != self.num:
                                    break
                            except NoSuchElementException:
                                break

                    flag = 1

                else:
                    i = i + 1

            i = 1
            if flag == 1: break
            next_button = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div/div[5]/ul/li[5]/a')

            next_button.click()

            time.sleep(3)

    def main(self):

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

        self.driver.get("https://pc.xuexi.cn/points/exam-index.html")

        time.sleep(2)

        # 每日答题

        self.part_1()

        # 每周答题

        back = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/span[3]/span[1]/a')

        back.click()

        time.sleep(2)

        self.part_2()

        # 专项答题

        back = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/span[3]/span[1]/a')

        back.click()

        time.sleep(2)

        self.part_3()

        print("ok")

        time.sleep(10)

        self.driver.quit()


if __name__ == '__main__':
    ABC = strong_country()
    ABC.main()
