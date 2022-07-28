from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

url = 'https://bazar-delivery.ru/catalog/frukty_i_yagody/'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)
previous_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)

    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == previous_height:
        break
    previous_height = new_height

fruits = driver.find_elements(By.XPATH, "//div[@class='card__content']")

header = ['Название', 'Ед измерения' ,'Цена']

with open ('prices.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
'''
    for fruit in fruits:
        f_name = fruit.find_element(By.CLASS_NAME, 'card__title')
        f_pr = fruit.find_element(By.CLASS_NAME, 'card__price').find_element(By.CSS_SELECTOR, 'span:first-of-type')
        f_qty = fruit.find_element(By.CLASS_NAME, 'card__price').find_element(By.CSS_SELECTOR, 'span:last-of-type')

        data = [f_name.text, f_qty.text ,f_pr.text]
        writer.writerow(data)
'''
temp_qty = fruits[1].find_element(By.CLASS_NAME, 'card__price').find_element(By.CSS_SELECTOR, 'span:last-of-type').text
print(temp_qty)

def substract(a, b):
    return "".join(a.rsplit(b))

gram = ' г'
if gram in temp_qty:
    weight = int(substract(temp_qty, gram))
    print(weight)