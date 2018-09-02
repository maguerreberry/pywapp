from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import autoit
import random

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# all_names = ['Yo', 'Juan Cavanagh', 'Mati Kleiner', 'Andy']
all_names = ['Achi']

raw_input('Enter anything after scanning QR code')

def find_by_xpath_click(xpath):
    while True:
        try:
            driver.find_element_by_xpath(xpath).click()
            break
        except:
            sleep(random.randrange(1,3))


def find_by_xpath_send_keys(xpath, keys):
    while True:
        try:
            driver.find_element_by_xpath(xpath).send_keys(keys)
            break
        except:
            sleep(random.randrange(1,3))


def search_contact(name):
    find_by_xpath_send_keys('//*[@id="side"]/div[2]/div/label/input', name)
    find_by_xpath_click('//span[@title = "'+name+'"]')

    
def send_text(text):
    find_by_xpath_send_keys('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', text+Keys.ENTER)


def send_image(image_path):
    find_by_xpath_click('//*[@id="main"]/header/div[3]/div/div[2]/div')
    find_by_xpath_click('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
    
    while True:
        try:
            autoit.control_focus("Open","Edit1")
            autoit.control_set_text("Open","Edit1",(image_path) )
            autoit.control_click("Open","Button1")
            break
        except:
            sleep(random.randrange(1,3))

    find_by_xpath_click('//*[@id="app"]/div/div/div[1]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
   
    
for name in all_names:
    search_contact(name)
    send_text('holis')
    send_text('https://m.youtube.com/watch?v=FpNPSuHhgfI')
    send_image('C:\Users\matt_\Downloads\macri-dollar.jpg')
    sleep(random.randrange(1,3))
    
    