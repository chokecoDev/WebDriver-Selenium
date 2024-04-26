import time
import datetime
import locale

from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Variables
locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')
print( datetime.date(2024,4,25).strftime("%A") )

# Selenium Configuration
service=Service(executable_path='driver\\chromedriver.exe')
options=webdriver.ChromeOptions()

driver=webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.latamairlines.com/")

# Origen
driver.find_element("xpath","//input[contains(@id,'txtInputOrigin_field')]").send_keys('Piura, PIU - Perú')
driver.find_element("xpath", "//button[contains(@id, 'btnItemAutoComplete_0')]").click()

# Destino
driver.find_element("xpath","//input[contains(@id,'txtInputDestination_field')]").send_keys('Lima, LIM - Perú')
driver.find_element("xpath", "//button[contains(@id, 'btnItemAutoComplete_0')]").click()

time.sleep(10)
driver.close()