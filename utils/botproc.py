import utils.configs as const
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class BotProc:

    def __init__(self):
        self.portal_url = const.RM_PORTAL
        print(self.portal_url)
        self.configs = const.read_config()
        self.driver = self.get_driver()


    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        driver.get(self.portal_url)
        return driver

    def login(self):
        time.sleep(2)
        self.driver.find_element(by="xpath", value=self.configs['user']).send_keys(const.PORTAL_USER + Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(by="xpath", value=self.configs['pass']).send_keys(
            const.PORTAL_PASS + Keys.RETURN)
        time.sleep(2)
        print(self.driver.current_url)

    def process_search_list(self, search_list):
        self.driver.find_element(by="xpath", value=self.configs['step_one']).click()
        self.driver.find_element(by="xpath", value=self.configs['step_two']).click()

        for s in search_list:
            self.driver.find_element(by="xpath", value=self.configs['search_criteria']).send_keys(s + Keys.RETURN)
            time.sleep(2)
            percentage = self.driver.find_element(by="xpath", value=self.configs['compliance_perc']).text
            comp_status = self.driver.find_element(by="xpath", value=self.configs['compliance_status']).get_attribute("class")
            time.sleep(2)
            self.driver.find_element(by="xpath", value="//*[@id=\"q\"]").clear()
            print(f"Name: {s}  {comp_status}  Percentage: {percentage}")







