from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('incognito')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url='https://www.google.com/')

driver.quit()

