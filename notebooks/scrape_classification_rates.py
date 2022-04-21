import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://www.wcirb.com/class-search')

code_to_amount = {}
code_to_phrase = {}
# there are 18 on last page (page 35)

try:
    link_count = 10
    page_count = 36
    # get first element
    for num_page in range(1, 35):
        if num_page == 35:
            link_count = 9
        first_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tr[@class='odd views-row-first']/td[1]/a"))
        )
        first_element_code = first_element.text
        first_element_phrase = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tr[@class='odd views-row-first']/td[2]/a"))
        )
        code_to_phrase[first_element_code] = '"' + first_element_phrase.text + '"'
        # add first element to dictionary
        clickable_element = driver.find_element(By.LINK_TEXT, first_element.text)
        clickable_element.click()
        amount = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[@class='odd']/td[2]"))
        )
        code_to_amount[first_element_code] = amount.text
        driver.back()
        # there are 9 odd links and 9 even links
        for num_element in range(1, link_count):
            # get odd elements and their info *****************************************
            if num_element == 8 and num_page == 35:
                pass
            else:
                pass
                odd_element_code = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody/tr[@class='odd'][" + str(num_element) + "]/td[1]"))
                )
                code_str = odd_element_code.text
                odd_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody/tr[@class='odd'][" + str(num_element) + "]/td[2]"))
                )
                code_to_phrase[code_str] = '"' + odd_element.text + '"'
                # add to dictionary
                clickable_element = driver.find_element(By.LINK_TEXT, odd_element.text)
                clickable_element.click()
                amount_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody/tr[@class='odd']/td[2]"))
                )
                code_to_amount[code_str] = amount_element.text
                driver.back()
            # get even elements and their info *****************************************
            even_element_code = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tbody/tr[@class='even'][" + str(num_element) + "]/td[1]"))
            )
            code_str = even_element_code.text
            even_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tbody/tr[@class='even'][" + str(num_element) + "]/td[2]"))
            )
            code_to_phrase[code_str] = '"'+ even_element.text + '"'
            # get amount and add it to the dictionary
            clickable_element = driver.find_element(By.LINK_TEXT, even_element.text)
            clickable_element.click()
            amount_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tbody/tr[@class='odd']/td[2]"))
            )
            code_to_amount[code_str] = amount_element.text
            driver.back()

            # get last element
            try:
                last_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//tr[@class='even views-row-last']/td[1]/a"))
                )
                last_element_code = last_element.text
                last_element_phrase = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//tr[@class='even views-row-last']/td[2]/a"))
                )
                code_to_phrase[last_element_code] = '"' + last_element_phrase.text + '"'
                # add last element to dictionary
                clickable_element = driver.find_element(By.LINK_TEXT, last_element.text)
                clickable_element.click()
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody/tr[@class='odd']/td[2]"))
                )
                code_to_amount[last_element_code] = element.text
                driver.back()
            except selenium.common.exceptions.TimeoutException:
                pass

        driver.get('https://www.wcirb.com/class-search?page=' + str(num_page))

    file = open('Employee_Classification_Rates.csv', 'w')
    file.write("code, phrase, employee classification rate\n")
    for (key1, value1), (key2, value2) in zip(code_to_phrase.items(), code_to_amount.items()):
        file.write(key1 + "," + value1 + "," + value2 + "\n")

finally:
    driver.quit()


