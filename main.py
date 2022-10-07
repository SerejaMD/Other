import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link_1 = "http://suninjuly.github.io/registration1.html"
#Нет второй ссылки. Пишу вам ниже
link_2 = "http://suninjuly.github.io/registration2.html"
driver = webdriver.Chrome()
#executable_path="C:\\Users\\ex\\PycharmProjects\\testAQA\\chromedriver\\chromedriver.exe")
#Не нужно писать абсолютный путь. Это работает только у вас. 
# Positiv test 1
try:
    driver.get(link_1)
    input1 = driver.find_element(By.XPATH, '//div[contains(@class,"first_block")]'
                                           '/div[contains(@class,"first_class")]'
                                           '/input ')
    input1.send_keys("Ivan")

    input2 = driver.find_element(By.XPATH, '//div[contains(@class,"first_block")]'
                                           '/div[contains(@class,"second_class")]'
                                           '/input ')
    input2.send_keys("Petrov")

    input3 = driver.find_element(By.XPATH, '//div[contains(@class,"first_block")]'
                                           '/div[contains(@class,"third_class")]'
                                           '/input ')
    input3.send_keys("Smolensk")
    time.sleep(1)
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
 

    welcom = driver.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcom

# except Exception as e:
#     print(e)
finally:
    time.sleep(3)

# Positive test 2
try:
    driver.get(link_2)
    input1 = driver.find_element(By.XPATH, '//div[contains(@class,"first_block")]'
                                           '/div[contains(@class,"first_class")]'
                                           '/input ')
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.XPATH, '//div[contains(@class,"first_block")]'
                                           '/div[contains(@class,"second_class")]'
                                           '/input ')
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.XPATH, '//div[contains(@class,"first_block")]'
                                           '/div[contains(@class,"third_class")]'
                                           '/input ')
    #Учитывая смысл конкретного задания, ниже код можно было опустить. Обойдясь полями со *
    input3.send_keys("Smolensk")
    phone = driver.find_element(By.XPATH, '//div[contains(@class,"second_block")]'
                                          '/div[contains(@class,"first_class")]'
                                          '/input ')
    phone.send_keys("Petrov")
    address = driver.find_element(By.XPATH, '//div[contains(@class,"second_block")]'
                                            '/div[contains(@class,"second_class")]'
                                            '/input ')
    address.send_keys("Smolensk")
    time.sleep(3)
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()


    welcom = driver.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcom

# except Exception as e:
#     print(e)

finally:
    time.sleep(3)
    driver.quit()

# не забываем оставить пустую строку в конце файла

