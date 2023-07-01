import os, time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chromedriver is installed: {driver_path}")
else:
    print(f"Install the chromedriver (version: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

search = input("Enter the search keyword: ")

google_search_kr = f"https://www.google.co.kr/search?gl=kr&hl=ko&q={search}"
google_search_us = f"https://www.google.com/search?gl=us&hl=en&q={search}"
google_search_uk = f"https://www.google.co.uk/search?gl=uk&hl=en&q={search}"
naver_search = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={search}"

driver = webdriver.Chrome(driver_path)

links = [google_search_kr, google_search_us, google_search_uk, naver_search]
driver.get(google_search_us)
tab_handles = driver.window_handles

for i in range(len(links)):
    if i > 0:
        driver.execute_script(f"window.open('{links[i]}', '_blank')")

driver.switch_to.window(tab_handles[0])

for handle in tab_handles[1:]:
    driver.switch_to.window(handle)
    driver.close()

driver.switch_to.window(tab_handles[0])

time.sleep(999999999)