import selenium
import hide
import os
import wget
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class facebookBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
    def login(self):
        driver=self.driver
        driver.get("http://facebook.com")
        sleep(1)
        username = driver.find_element_by_xpath('//*[@id="email"]')
        username.clear()
        username.send_keys(self.username)
        password = driver.find_element_by_xpath('//*[@id="pass"]')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        sleep(2)

    def profile(self):
        driver=self.driver
        driver.get("http://facebook.com/profile")
        sleep(2)
    def getImg(self):
        driver=self.driver
        images=[]
        for i in ['photos_of','photos_all']:
            driver.get('https://facebook.com/shray.anand.9/'+i+'/')
            sleep(5)
            scroll=2
            for i in range (scroll):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                sleep(5)
                anchors=driver.find_elements_by_tag_name("a")
                anchors=[anchor.get_attribute("href") for anchor in anchors]
                anchors=[a for a in anchors if str(a).startswith("https://www.facebook.com/photo.php")]
                for a in anchors:
                    driver.get(a)
                    sleep(2)
                    img=driver.find_elements_by_tag_name("img")
                    images.append(img[0].get_attribute("src"))
        path=os.getcwd()
        path=os.path.join(path,"facebookPhotos")
        os.mkdir(path)
        counter=0
        for image in images:
              save_as=os.path.join(path,str(counter)+'.jpg')
              wget.download(image,save_as)
              counter+=1

fb=facebookBot("enter-you-username",hide.secret())
fb.login()
fb.profile()
fb.getImg()

