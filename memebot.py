import selenium, time, pickle, random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options=Options()
options.headless = True
prefs = {"profile.default_content.setting.values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
PATH = "/home/chakib37/bot/chromedriver"
newpath = input("where is your chrome driver located? press 1 if it's hard coded:    ")
if newpath != '1':
    PATH = newpath
else:
    print('hi, all good')
acc = input('choose a username\n') + '.pkl'


driver = webdriver.Chrome(PATH, chrome_options=options)
driver.close()
driver.quit()

def src(source):
    #CHOOSE SOURCE
    if source == 20:
        src = 'https://www.reddit.com/r/aww/rising/'
    elif source == 27:
        src = 'https://www.reddit.com/r/im14andthisisdeep/rising'
    elif source == 26:
        src = 'https://www.reddit.com/r/MapPorn/rising'
    elif source == 25:
        src = 'https://www.reddit.com/r/Algeria/new'
    elif source == 24:
        src = 'https://www.reddit.com/r/c137/rising'
    elif source == 23:
        src = 'https://www.reddit.com/r/BoJackHorseman/new/'
    elif source == 22:
        src = 'https://www.reddit.com/foodporn/rising'
    elif source == 21:
        src = 'https://www.reddit.com/r/oldpeoplefacebook/new/'
    elif source == 12:
        src = 'https://www.reddit.com/r/iamverybadass/rising/'
    elif source == 18:
        src = 'https://www.reddit.com/r/okbuddylinux/rising'
    elif source == 13:
        src = 'https://www.reddit.com/r/spaceporn/new/'
    elif source == 17:
        src = 'https://www.reddit.com/r/earthporn/new/'
    elif source == 15:
        src = 'https://www.reddit.com/r/holup/new/'
    elif source == 16:
        src = 'https://www.reddit.com/r/askreddit/new/'
    elif source % 2 == 0:
        src = 'https://www.reddit.com/r/memes/new/'
    elif source % 7 == 0:
        src = 'https://www.reddit.com/r/askscience/new/'
    elif source % 3 == 0:
        src = 'https://www.reddit.com/r/technicallythetruth/new/'
    elif source == 1:
        src = 'https://www.reddit.com/r/cursedcomments/new/'
    elif source == 11:
        src = 'https://www.reddit.com/r/linuxmemes/new/'
    else :
        src = 'https://www.reddit.com/r/amongus/new/' 
    
    print(src)
    return src

def wait(delay):
    print(delay)
    for i in range(0, delay):
        if (delay-i) % 600 == 0:
            print(str((delay-i)/60) + ' minutes left to post')
        time.sleep(1)

def get_meme(src, driver):
    #STEAL MEMES
    try :
        driver.get(src)
        time.sleep(1)
        meme = driver.find_element_by_xpath('.//*[contains(@id,"t3_")]')
        meme.click()
        time.sleep(10)
        title = driver.find_element_by_xpath('./html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]/div[1]/div/h1').text
        meme = driver.find_element_by_xpath('./html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]/a/img')
        meme.click()
        time.sleep(10)
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(10)
        meme = driver.find_element_by_xpath('./html/body/img')
        meme.screenshot('memes.png')
        return title
    except Exception:
        try :
            driver.get(src)
            time.sleep(1)
            meme = driver.find_element_by_xpath('.//*[contains(@id,"t3_")]')
            meme.click()
            time.sleep(5)
            title = driver.find_element_by_xpath('./html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]/div[1]/div/h1').text
            meme = driver.find_element_by_xpath('./html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]/div').text
            title = str(title) + '     \n' + str(meme)
            return title
        except Exception:
            title = 'none'

def login_cookies(driver, acc):
    driver.get('https://www.facebook.com')
    #LOGIN BY COOKIES
    try:
        account = open(acc, 'rb')
        cookies = pickle.load(account)
        print('logged in using cookies, welcome back!')
        for cookie in cookies:
            driver.add_cookie(cookie)
        time.sleep(3)
        account.close()
    except Exception:
        login_type(driver, acc)

def login_type(driver, acc):
    #LOGIN
    email = input('this is only needed for the first time\n what is your email?\n')
    password = input('what is your password?\n')
    driver.get('https://facebook.com')
    email = driver.find_element_by_xpath('.//*[@id="email"]')
    passwd = driver.find_element_by_xpath('.//*[@id="pass"]')
    login = driver.find_element_by_xpath('.//*[@id="u_0_b"]')
    email.send_keys(email)
    passwd.send_keys(password)
    login.click()
    time.sleep(6)
    #save_cookies
    account = open(acc, 'rb')
    pickle.dump(driver.get_cookies(), account)
    account.close()

def posttxt(txt, driver):
    #POST TEXT
    driver.get('https://facebook.com')
    time.sleep(2)
    post = driver.find_element_by_css_selector('div.a5q79mjw:nth-child(1) > span:nth-child(1)')
    post.click()
    time.sleep(5)
    post = driver.find_element_by_xpath('./html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')
    for word in txt:
        time.sleep(random.randint(230,1042)/1000)
        post.send_keys(word)
    time.sleep(1)
    btn = driver.find_element_by_xpath('./html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div')
    btn.click()

def post_pic(title, driver):
    #UPLOAD
    driver.get("https://mbasic.facebook.com/")
    memes = driver.find_element_by_xpath('./html/body/div/div/div[2]/div/div[2]/div/form/div[2]/span/div[1]/table/tbody/tr/td[2]/input')
    memes.click()
    time.sleep(2)

    memes = driver.find_element_by_xpath('./html/body/div/div/div[2]/div/table/tbody/tr/td/form/div[1]/div/input[1]')
    memes.send_keys('/home/chakib37/fb_posting_bot/memes.png')

    post = driver.find_element_by_xpath('./html/body/div/div/div[2]/div/table/tbody/tr/td/form/div[3]/input[1]')
    post.click()
    time.sleep(5)

    text = driver.find_element_by_xpath('.//*[@id="u_0_0"]')
    cap = title
    for letter in str(cap):
        time.sleep(random.randint(230,1042)/1000)
        text.send_keys(letter)
    post = driver.find_element_by_xpath('./html/body/div/div/div[2]/div/table/tbody/tr/td/div/form/input[19]')
    post.click()
    #UPLOAD DONE

def memebot(driver, sauce, acc, delay = random.randint(1800, 5000)):
    wait(delay)
    driver = webdriver.Chrome(PATH, chrome_options=options)
    caption = get_meme(sauce, driver)
    time.sleep(2)
    if caption == 'none' or caption.find('/u') != -1 or caption.find('/r') != -1:
        print('none')
        driver.quit()
    elif caption.find('     \n') != -1:
        login_cookies(driver, acc)
        posttxt(caption, driver)
        driver.quit()
    else:
        login_cookies(driver, acc)
        post_pic(caption, driver)
        driver.quit()

def memeit(acc, driver = driver):

    while True:
        try:
            try:
                ran = random.randint(1,30)
                sauce = src(ran)
                memebot(driver, sauce, acc)
            except Exception:
                ran = random.randint(1,30)
                sauce = src(ran)
                memebot(driver, sauce, acc, 0)
        except:
            continue

def mock(source, acc):
    sent = ''
    received = 'bot is in'
    def send(driver, received):
        if sent == received:
            received = receive(driver, sent)
        else:
            driver.get(source)
            field = driver.find_element_by_id("composerInput")
            field.send_keys(received)
            driver.find_element_by_xpath('./html/body/div/div/div[2]/div/div[1]/div[3]/div/div/form/table/tbody/tr/td[2]/input').click()
            return sent

    def receive(driver, sent):
        driver.get(source)
        received = driver.find_element_by_css_selector('#fua > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)').text
        return received

    driver = webdriver.Chrome(PATH, chrome_options=options)
    login_cookies(driver, acc)
    while True:
        test = ''
        try:
            received = receive(driver, sent)
            if 'bela3' in received:
                break
            else :
                for i in range(len(received)):
                    if i % 2 == 0:
                        test += received[i].lower()
                    else :
                        test += received[i].upper()
                if test in received:
                    continue
                else:
                    received = test
            sent = send(driver, received)
            time.sleep(10)
        except Exception:
            continue

choice = input('what do you want to do? press 1 for memes, anything else for mocking\n\n')

if choice == '1':
    print("stop this program if the XPATH isn't hard coded, I'll try to fix that issue soon")
    memeit(acc)
else:
    source = input('paste the messages adress in here using mbasic facebook version.\n')
    print('use "bela3" to make the bot stop')
    mock(source, acc)