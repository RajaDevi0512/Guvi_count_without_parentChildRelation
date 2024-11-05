from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Data:
    url = 'https://www.instagram.com/guviofficial/'
    

class Locator:
    Followers_locator = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/button'
    Following_Locator = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/div'
    close_window = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/svg'
class Count_check(Data,Locator):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element(by=By.XPATH, value = self.close_window).click()
        sleep(5)

    def Count_fetching(self):
        followers = self.driver.find_element(by=By.XPATH, value = self.Followers_locator).text
        print("Followers: ",followers)
        following = self.driver.find_element(by=By.XPATH, value = self.Following_Locator).text
        print("Following: ",following)

    def shutdown(self):
        self.driver.quit()

myCount = Count_check()
myCount.start()
myCount.Count_fetching()
myCount.shutdown()