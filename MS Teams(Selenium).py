from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome import options
import datetime
import random


def theory(i, j, un, pw, ma):
    t = random.randint(2400, 3000)
    # TOGGLE BROWSER OPTIONS
    opt = options.Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    if ma == 'T':
        opt.add_argument("--mute-audio")
    else:
        pass
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs",
                                {"profile.default_content_setting_values.media_stream_mic": 2,
                                 "profile.default_content_setting_values.media_stream_camera": 2,
                                 "profile.default_content_setting_values.geolocation": 2,
                                 "profile.default_content_setting_values.notifications": 2})
    # OPEN BROWSER
    driver = webdriver.Chrome(options=opt, executable_path=r'C:\Users\user\PycharmProjects\Automation\chromedriver.exe')
    sleep(7)
    # GO TO TEAMS
    driver.get('https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software')
    sleep(12)
    # OPEN SIGN IN PAGE
    driver.find_element_by_id('mectrl_main_trigger').click()
    sleep(7)
    # ENTER USERNAME
    driver.find_element_by_id('i0116').send_keys(un)
    sleep(5)
    # CLICK NEXT
    driver.find_element_by_id('idSIButton9').click()
    sleep(5)
    # ENTER PASSWORD
    driver.find_element_by_id('i0118').send_keys(pw)
    sleep(5)
    # CLICK NEXT
    driver.find_element_by_id('idSIButton9').click()
    sleep(5)
    # CLICK STAY SIGNED IN
    driver.find_element_by_id('idSIButton9').click()
    sleep(12)
    # CLICK A1 SLOT TILE
    driver.find_element_by_xpath(f'//*[@id="favorite-teams-panel"]/div/div[1]/div[{i}]/div[{j}]/div/ng-include/div').click()
    sleep(5)
    # CLICK JOIN MEETING BUTTON
    driver.find_element_by_class_name('ts-calling-join-button').click()
    sleep(5)
    # CLICK ALLOW WITHOUT MIC AND VIDEO
    driver.find_element_by_class_name('ts-btn-fluent-secondary-alternate').click()
    sleep(5)
    # CLICK FINAL JOIN MEETING
    driver.find_element_by_class_name('join-btn').click()
    sleep(t)
    # END MEETING
    driver.find_element_by_id('hangup-button').click()


def condition(d):
    hour = datetime.datetime.now().time().hour
    mnt = datetime.datetime.now().time().minute
    un = input('ENTER USERNAME:')
    pw = input('ENTER PASSWORD')
    mute = input('MUTE AUDIO(T/F)')
    if d == 'Monday' and hour == 8 and mnt == 5:
        i = 2
        j = 2
        theory(i, j, un, pw, mute)
    elif d == 'Tuesday' and hour == 8 and mnt == 5:
        i = 2
        j = 3
        theory(i, j, un, pw, mute)
    elif d == 'Thursday' and hour == 8 and mnt == 5:
        i = 2
        j = 4
        theory(i, j, un, pw, mute)
    elif d == 'Friday' and hour == 8 and mnt == 5:
        i = 2
        j = 5
        theory(i, j, un, pw, mute)
    elif d == 'Monday' and hour == 9 and mnt == 5:
        i = 2
        j = 6
        theory(i, j, un, pw, mute)
    elif d == 'Tuesday' and hour == 9 and mnt == 5:
        i = 3
        j = 2
        theory(i, j, un, pw, mute)
    elif d == 'Wednesday' and hour == 9 and mnt == 5:
        i = 2
        j = 2
        theory(i, j, un, pw, mute)
    elif d == 'Thursday' and hour == 9 and mnt == 5:
        i = 2
        j = 3
        theory(i, j, un, pw, mute)
    elif d == 'Monday' and hour == 10 and mnt == 5:
        i = 2
        j = 4
        theory(i, j, un, pw, mute)
    elif d == 'Tuesday' and hour == 10 and mnt == 5:
        i = 2
        j = 5
        theory(i, j, un, pw, mute)
    elif d == 'Wednesday' and hour == 10 and mnt == 5:
        i = 2
        j = 6
        theory(i, j, un, pw, mute)
    elif d == 'Thursday' and hour == 10 and mnt == 5:
        i = 3
        j = 2
        theory(i, j, un, pw, mute)
    elif d == 'Friday' and hour == 10 and mnt == 5:
        i = 2
        j = 2
        theory(i, j, un, pw, mute)
    elif d == 'Monday' and hour == 11 and mnt == 5:
        i = 2
        j = 3
        theory(i, j, un, pw, mute)
    elif d == 'Wednesday' and hour == 11 and mnt == 5:
        i = 2
        j = 2
        theory(i, j, un, pw, mute)
    elif d == 'Thursday' and hour == 11 and mnt == 5:
        i = 2
        j = 5
        theory(i, j, un, pw, mute)
    elif d == 'Monday' and hour == 12 and mnt == 5:
        i = 3
        j = 2
        theory(i, j, un, pw, mute)
    elif d == 'Tuesday' and hour == 12 and mnt == 5:
        i = 2
        j = 2
        theory(i, j, un, pw, mute)
    elif d == 'Friday' and hour == 12 and mnt == 5:
        i = 3
        j = 3
        theory(i, j, un, pw, mute)
    else:
        print('NO CLASSES')


while True:
    day = datetime.datetime.today().strftime("%A")
    condition(day)
