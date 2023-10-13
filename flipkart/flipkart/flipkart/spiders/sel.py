from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.flipkart.com/complete-novel-sherlock-holmes/p/itm297f1df03db51?pid=9788175994317&lid=LSTBOK9788175994317H3GNJG&marketplace=FLIPKART&q=novels&store=bks&spotlightTagId=BestsellerId_bks&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=5ba09817-52a2-440f-b671-62fd2144ceb0.9788175994317.SEARCH&ppt=sp&ppn=sp&ssid=f4yl3dpzzk0000001697007159142&qH=f3221bc44ebd23a6")

xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "s1Q9rs", " " ))]'
link_elements = driver.find_elements(By.XPATH, xpath)
links = []

for link in link_elements:
    href = link.get_attribute("href")
    links.append(href)
print(len(links))
driver.quit()

print(links)