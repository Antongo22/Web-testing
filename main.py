from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

browser_choice = input("Выберите браузер (1 - Chrome, 2 - Firefox): ")

if browser_choice == '1':
    driver = webdriver.Chrome()
elif browser_choice == '2':
    driver = webdriver.Firefox()
else:
    print("Неверный выбор. По умолчанию будет использован Chrome.")
    driver = webdriver.Chrome()

driver.set_window_size(1280, 1024)

driver.get('https://konflic.github.io/examples/')

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='hide_with_opacity button']")))
driver.find_element(By.XPATH, "//button[@class='hide_with_opacity button']").click()

print(driver.find_element(By.XPATH, "//p[@id='modal-text']").text)
driver.find_element(By.XPATH, "//span[@class='close']").click()

email_element = driver.find_element(By.XPATH, "//th[contains(text(), 'Email')]")

is_background_gray = lambda element: element.value_of_css_property("background-color") in [
    "rgba(128, 128, 128, 1)",
    "rgb(128, 128, 128)",
    "rgba(128, 128, 128, 0.5)"
]

while not is_background_gray(email_element):
    email_element.click()
    time.sleep(0.5)

print("Цвет - серый!")

driver.find_element(By.XPATH, "//a[@id='dropdownMenuLink']").click()
driver.find_element(By.XPATH, "//a[@class='dropdown-item' and contains(text(), 'Drag and Drop')]").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cardPile')))


def drag_and_drop_card(card_id, zone_id):
    card = driver.find_element(By.ID, card_id)
    zone = driver.find_element(By.ID, zone_id)

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", zone)

    ActionChains(driver).drag_and_drop(card, zone).perform()


time.sleep(0.5)
for i in range(1, 11):
    drag_and_drop_card(f'card{i}', f'zone{i}')

time.sleep(2)
success_message = driver.find_element(By.ID, 'successMessage')
if success_message.is_displayed():
    print("Все карты собраны!")
else:
    print("Ошибка(")

time.sleep(10)
driver.quit()