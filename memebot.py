import selenium, time, pickle, random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options=Options()
options.headless = True
prefs = {"profile.default_content.setting.values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
try:
    PATH = open('path', 'r').read()
except Exception:
    PATH = input("where is your chrome driver located :    ")
    open('path', 'w').write(PATH)

acc = input('choose a username\n') + '.pkl'
received = 'bot is in'


driver = webdriver.Chrome(PATH, chrome_options=options)
driver.close()
driver.quit()

def src():
    src=open('source', 'r').read().splitlines()
    rand = random.randint(0, len(src))
    src = 'https://www.reddit.com/' + src[rand]
    nr = random.randint(0, 4)
    if nr == 3:
        src += '/rising'
    else :
        src+= '/new'
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
    driver.get('https://www.facebook.com')
    time.sleep(5)
    emailat = driver.find_element_by_id("email")
    passwd = driver.find_element_by_id("pass")
    login = driver.find_element_by_id("u_0_b")
    emailat.send_keys(email)
    passwd.send_keys(password)
    login.click()
    time.sleep(6)
    #save_cookies
    account = open(acc, 'wb')
    pickle.dump(driver.get_cookies(), account)
    account.close()

def posttxt(txt, driver):
    #POST TEXT
    driver.get('https://mbasic.facebook.com')
    time.sleep(2)
    post = driver.find_element_by_xpath('./html/body/div/div/div[2]/div/div[2]/div/form/table/tbody/tr/td[2]/div/textarea')
    for word in txt:
        time.sleep(random.randint(230,1042)/1000)
        post.send_keys(word)
    time.sleep(1)
    btn = driver.find_element_by_xpath('./html/body/div/div/div[2]/div/div[2]/div/form/table/tbody/tr/td[3]/div/input')
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

def memebot(driver, sauce, acc, delay):
    wait(delay)
    driver = webdriver.Chrome(PATH, chrome_options=options)
    caption = get_meme(sauce, driver)
    time.sleep(2)
    if caption == 'none' or caption.find('u/') != -1 or caption.find('r/') != -1:
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

def memeit(acc, x, y, driver = driver):

    while True:
        try:
            try:
                sauce = src()
                memebot(driver, sauce, acc, random.randint(x, y))
            except Exception:
                sauce = src()
                memebot(driver, sauce, acc, 0)
        except:
            driver.quit()
            continue


def send(driver, received, sent):
    if sent == received:
        received = receive(driver, sent)
    else:
        driver.get(source)
        field = driver.find_element_by_id("composerInput")
        field.send_keys(received)
        driver.find_element_by_xpath('./html/body/div/div/div[2]/div/div[1]/div[3]/div/div/form/table/tbody/tr/td[2]/input').click()
        sent = received
        return sent

def receive(driver, sent):
    driver.get(source)
    received = driver.find_element_by_css_selector('#fua > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)').text
    return received

def search(command, driver = driver):
    try:
        driver = webdriver.Chrome(PATH, chrome_options=options)
        driver.get('https://www.google.dz/imghp?hl=fr&tab=wi&ogbl')
        command = command[6::]
        driver.find_element_by_xpath('./html/body/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(command)
        driver.find_element_by_xpath('./html/body/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('./html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]/img').click()
        time.sleep(5)
        driver.find_element_by_xpath('./html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').screenshot('memes.png')
    except Exception:
        print('error')
    finally:
        driver.close()
        driver.quit()

def send_pic(source, acc, driver = driver):
    driver = webdriver.Chrome(PATH, chrome_options=options)
    login_cookies(driver, acc)
    driver.get(source)
    driver.find_element_by_xpath('./html/body/div/div/div[2]/div/div[1]/div[3]/div/div/form/span/input[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('./html/body/div/div/div[2]/div/table/tbody/tr/td/section/form/div[1]/input[1]').send_keys('/home/chakib37/fb_posting_bot/memes.png')
    driver.find_element_by_xpath('./html/body/div/div/div[2]/div/table/tbody/tr/td/section/form/div[2]/input').click()
    time.sleep(5)
    driver.quit()


def mock(source, acc, mes, sent = ''):
    driver = webdriver.Chrome(PATH, chrome_options=options)
    login_cookies(driver, acc)
    while True:
        test = ''
        try:
            time.sleep(random.randint(3,9))
            received = receive(driver, sent)
            if sent == received:
                continue
            elif 'bela3' in received:
                mes = '1'
            elif 'search' in received:
                search(received)
                send_pic(source, acc)
                sent = 'pic'
                time.sleep(10)
                received = 'trying to get pic'
            elif 'memebot' in received:
                sauce = src()
                caption = get_meme(sauce, driver)
                if caption == 'none' or caption.find('/u') != -1 or caption.find('/r') != -1:
                    print('none')
                elif caption.find('     \n') != -1:
                    sent = send(driver, caption, sent)
                    time.sleep(10)
                else:
                    send_pic(source, acc)
                    sent = 'pic'
                    time.sleep(10)
            elif ' is ' in received:
                received = received.lower()
                diff = received.find(' is ')
                wo = received[diff + 4::].lower()
                rd = received[:diff:].lower()
                received = wo + ' is ' + rd
                sent = send(driver, received, sent)
                sent = received
                time.sleep(5)
            elif 'high five' in received.lower():
                sent = send(driver, 'HIGH FIVE BUDDY', sent)
            elif 'say ' in received.lower():
                received = received[3::]
                sent = send(driver, received, sent)
            elif mes == '1':
                continue
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
                sent = send(driver, received, sent)
                time.sleep(10)
        except Exception:
            continue

choice = input('what do you want to do? press 1 for memes, anything else for mocking or messenger search help\n\n')

if choice == '1':
    x = int(input('what is the minimum time you want between posts in seconds?\n'))
    y = int(input('what is the maximum time you want between posts in seconds?\n'))
    memeit(acc, x, y)
else:
    mes=input('press 1 for messenger feature without mocking   ')
    source = input('paste the messages adress in here using mbasic facebook version.\n')
    print('use "bela3" to make the bot stop mocking, "seach" to make it send the first google images result, and "memebot" to make it send something from the subreddits in source')
    mock(source, acc, mes)