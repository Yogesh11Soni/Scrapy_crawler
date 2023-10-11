from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.flipkart.com/search?q=novels&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "s1Q9rs", " " ))]'
link_elements = driver.find_elements(By.XPATH, xpath)
links = []

for link in link_elements:
    href = link.get_attribute("href")
    links.append(href)
print(len(links))
driver.quit()

print(links)