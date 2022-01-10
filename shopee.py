from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import datetime

alarmH = int(input("masukan jam"))
alarmM = int(input("masukan menit"))


driver = webdriver.Chrome('webdriver/chromedriver.exe')
driver.maximize_window()

     
login = "https://shopee.co.id/buyer/login/qr?from=https%3A%2F%2Fshopee.co.id%2Fproduct-i.218461011.5035997390%3Fsmtt%3D0.218879583-1605157013.9&next=https%3A%2F%2Fshopee.co.id%2Fproduct-i.218461011.5035997390%3Fsmtt%3D0.218879583-1605157013.9&smtt=0.218879583-1605157013.9"


driver.get(login)
time.sleep(10)



print("waiting for alarm",alarmH,alarmM)

while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute):


        btnbeli = driver.find_element(By.XPATH, "//button[contains(text(),'beli sekarang')]")
        btnbeli.click()

        # time.sleep(0.9)
        # btncheckout = driver.find_element_by_css_selector('#main > div > div._1Bj1VS > div.cart-page.cart-page--opc > div:nth-child(3) > div.cart-page-footer.cart-page-footer--overlap > div.cart-page-footer__row._1a6Hgi.cart-page-footer__row5 > div.cart-page-footer__checkout > button')
        # btncheckout.send_keys(Keys.ENTER)

        try:
            element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div > div._1Bj1VS > div.cart-page.cart-page--opc > div:nth-child(3) > div.cart-page-footer.cart-page-footer--overlap > div.cart-page-footer__row._1a6Hgi.cart-page-footer__row5 > div.cart-page-footer__checkout > button"))
        )
        finally:
            btncheckout = driver.find_element_by_css_selector('#main > div > div._1Bj1VS > div.cart-page.cart-page--opc > div:nth-child(3) > div.cart-page-footer.cart-page-footer--overlap > div.cart-page-footer__row._1a6Hgi.cart-page-footer__row5 > div.cart-page-footer__checkout > button')
            btncheckout.send_keys(Keys.ENTER)

        # time.sleep(2.5)
        # btnpilihbank = driver.find_element_by_css_selector('#main > div > div._1Bj1VS > div.page-checkout.container > div.page-checkout__payment-order-wrapper > div.checkout-payment-method-view > div > div.checkout-payment-method-view__current.checkout-payment-setting > div.checkout-payment-setting__payment-methods-tab > span:nth-child(1) > button')
        # btnpilihbank.click()

        # time.sleep(2)
        # btnpesan = driver.find_element_by_css_selector('#main > div > div._1Bj1VS > div.page-checkout.container > div.page-checkout__payment-order-wrapper > div.OR36Xx > div._3S63c5._3IF-9E > button')
        # btnpesan.click()
        try:
            testing1 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div > div._1Bj1VS > div.page-checkout.container > div.page-checkout__payment-order-wrapper > div.checkout-payment-method-view > div > div.checkout-payment-method-view__current.checkout-payment-setting > div.checkout-payment-setting__payment-methods-tab > span:nth-child(1) > button"))
        )
        finally:
            btnpilihbank = driver.find_element_by_css_selector('#main > div > div._1Bj1VS > div.page-checkout.container > div.page-checkout__payment-order-wrapper > div.checkout-payment-method-view > div > div.checkout-payment-method-view__current.checkout-payment-setting > div.checkout-payment-setting__payment-methods-tab > span:nth-child(1) > button')
            btnpilihbank.click()

        try:
            testing = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div > div._1Bj1VS > div.page-checkout.container > div.page-checkout__payment-order-wrapper > div.OR36Xx > div._3S63c5._3IF-9E > button"))
        )
        finally:
            btnpesan = driver.find_element_by_css_selector('#main > div > div._1Bj1VS > div.page-checkout.container > div.page-checkout__payment-order-wrapper > div.OR36Xx > div._3S63c5._3IF-9E > button')
            btnpesan.click()
        break


