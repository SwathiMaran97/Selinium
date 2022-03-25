import sys
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://vconnect.net/login")

def create():
    python_button = driver.find_elements_by_xpath("//*[@id='orangeForm-email']")[0]
    python_button.send_keys('swathimaranbe123@gmail.com')
    python_button = driver.find_elements_by_xpath("//*[@id='orangeForm-pass']")[0]
    python_button.send_keys('12378999')
    python_button = driver.find_elements_by_xpath('/html/body/header/section/div/div/div/div[2]/div/div/form/div[4]/button')[0]
    python_button.click()
    python_button = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div/section[2]/div[1]/div[2]/div/div/div[1]/a')[0]
    python_button.click()
    python_button = driver.find_elements_by_xpath("//*[@id='addgeneraltask']/div/div/form/div[1]/div[2]/textarea")[0]
    python_button.send_keys('Binded values for Daily Report fetched from QualityIssue Completed Daily Report.Worked on scar moduleand Discussed about scar process Checked demo tool summery page to 8danalysis.Attended meeting with TL anddiscussed and clarifiedabout scar process with team Fixed issues for Impacted Productsand AffectedComponentsfetch values')
    python_button = driver.find_elements_by_xpath("//*[@id='addgeneraltask']/div/div/form/div[1]/div[3]/input")[0]
    python_button.send_keys('2020-04-20')
    python_button = driver.find_elements_by_xpath("//*[@id='addgeneraltask']/div/div/form/div[1]/div[4]/input")[0]
    python_button.send_keys('2020-04-23')
    python_button = driver.find_elements_by_xpath("//*[@id='addgeneraltask']/div/div/form/div[1]/div[5]/input")[0]
    python_button.send_keys('32')
    python_button = driver.find_elements_by_xpath("//*[@id='addgeneraltask']/div/div/form/div[2]/button[2]")[0]
    python_button.click()
    time.sleep(60)
    driver.close()
    driver.quit()
if __name__ == '__main__':
    create()
    