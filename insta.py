import random, pickle, selenium, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
acc = input('what is your username\n') + '.pkl'
try:
    PATH = open('path').read()
except Exception:
    PATH = input('where is your chrome driver? you can download it from:\nhttps://chromedriver.chromium.org/downloads \nand paste the path to your file here\n')
    open('path','w').write(PATH)
driver = webdriver.Chrome(PATH, chrome_options=options)
source = input('write the hashtag you want, example: "art", ypu can press 1 for default tho\n')
if source == '1':
    source = 'https://www.instagram.com/explore/tags/art/'
else:
    source = source = 'https://www.instagram.com/explore/tags/' + source


def typed(acc = acc, PATH = PATH):
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(PATH, chrome_options=options)
    driver.get('https://instagram.com')
    print("can you help me by clicking 'Save info' so that you don't really have to type your username and password again?\n")
    username = input('what is your username :  \n')
    pw = input('what is your password :  \n')
    time.sleep(5)
    driver.find_element_by_xpath('./html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
    driver.find_element_by_xpath('./html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(pw)
    driver.find_element_by_xpath('./html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click()
    time.sleep(2)
    time.sleep(10)
    print('can you click save info for me?\n')
    #driver.find_element_by_xpath('./html/body/div[1]/section/main/div/div/div/section/div/button').click()
    pickle.dump(driver.get_cookies(), open(acc, 'wb'))
    driver.quit()
    print('run the program again now and it will work fine.')

def login(driver = driver, acc = acc):
    driver.get('https://instagram.com')
    try:
        for cookies in pickle.load(open(acc, 'rb')):
            driver.add_cookie(cookies)
        driver.get('https://instagram.com')
        time.sleep(5)
    except Exception:
        typed()

def pic(source = source):
    driver.get(source)
    time.sleep(5)
    driver.find_element_by_xpath('./html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('./html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/button').click()
    time.sleep(2)
    for i in range(130):
        try:
            person = './html/body/div[6]/div/div/div[2]/div/div/div[' + str(i) + ']/div[3]/button'
            driver.find_element_by_xpath(person).click()
            time.sleep(random.randint(1,5))
        except Exception:
            continue

login()
pic()
driver.close()
driver.quit()
