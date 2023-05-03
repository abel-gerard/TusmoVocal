from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

from speech import clean, detect
from keyMap import KEY_MAP

def initializeDriver():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    
    driver = Firefox(options=options)
    return driver

def clickOnMode(driver, mode):
    daily = driver.find_element(By.CSS_SELECTOR, ".flex-col > div:nth-child(1)")
    suite = driver.find_element(By.CSS_SELECTOR, ".flex-col > div:nth-child(2)")
    solo = driver.find_element(By.CSS_SELECTOR, ".pl-3")

    match mode:
        case "daily": daily.click()
        case "suite": suite.click()
        case "solo": solo.click()
        case _: raise ValueError
        
def getKeys(driver):
    keys = [driver.find_element(By.CSS_SELECTOR, f"div.key-row:nth-child({KEY_MAP[key][0]}) > div:nth-child({KEY_MAP[key][1]})") for key in KEY_MAP] 
    keys = dict(zip(KEY_MAP.keys(), keys))
    keys["B_SPACE"] = driver.find_element(By.CSS_SELECTOR, ".fa-backspace")
    keys["RETURN"] = driver.find_element(By.CSS_SELECTOR, ".fa-sign-in-alt")
    
    return keys

def sendInput(driver, userInput, keys):
    firstWord = userInput[0]
            
    match firstWord:
        case "OK": 
            keys["RETURN"].click()
            return True  
        
        case "GOOGLE":
            keys["B_SPACE"].click()
            return True
        
        case "KIWI":
            for _ in range(10): keys["B_SPACE"].click()
            return True
        
        case "STOP":
            driver.close()
            return False
    
    for letter in userInput[0]:
        try:
            keys[letter].click()
        except: pass

    return True

def tusmo(mode):
    tusmo = "https://www.tusmo.xyz/"
    
    driver = initializeDriver()
    driver.get(tusmo)   

    clickOnMode(driver, mode)

    time.sleep(1)

    keys = getKeys(driver)
    
    running = True
    while running:
        userInput = clean(detect())
        
        if userInput:
            print((" ".join(userInput)).title())
            
            running = sendInput(driver, userInput, keys)
                
        print('\n')
