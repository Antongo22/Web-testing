from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# anton005go.too@gmail.com
# 12345678

browser_choice = input("Выберите браузер (1 - Chrome, 2 - Firefox): ")

if browser_choice == '1':
    driver = webdriver.Chrome()
elif browser_choice == '2':
    driver = webdriver.Firefox()
else:
    print("Неверный выбор. По умолчанию будет использован Chrome.")
    driver = webdriver.Chrome()

driver.set_window_size(1500, 1024)

driver.get('http://172.22.10.46:8080/')

# Функция для прокрутки к элементу
def scroll_to_element(element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.5)

# Вход
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'My Account')]")))
my_account = driver.find_element(By.XPATH, "//span[contains(text(), 'My Account')]")
scroll_to_element(my_account)
my_account.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Login')]")))
login_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
scroll_to_element(login_link)
login_link.click()

email_input = driver.find_element(By.XPATH, "//input[@id='input-email']")
scroll_to_element(email_input)
email_input.clear()
email_input.send_keys("anton005go.too@gmail.com")

password_input = driver.find_element(By.XPATH, "//input[@id='input-password']")
scroll_to_element(password_input)
password_input.clear()
password_input.send_keys("12345678")

login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
scroll_to_element(login_button)
login_button.click()


time.sleep(1)
logo = driver.find_element(By.XPATH, "//div[@id='logo']/a")
scroll_to_element(logo)
logo.click()

# Вишлист
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='product-thumb']//h4/a[contains(text(), 'iPhone')]")))
iphone_wishlist_button = driver.find_element(By.XPATH, "//div[@class='product-thumb'][.//h4/a[contains(text(), 'iPhone')]]//button[@title='Add to Wish List']")
scroll_to_element(iphone_wishlist_button)
iphone_wishlist_button.click()

# Камера
canon_cart_button = driver.find_element(By.XPATH, "//div[@class='product-thumb'][.//h4/a[contains(text(), 'Canon EOS 5D')]]//button[i[@class='fa-solid fa-shopping-cart']]")
scroll_to_element(canon_cart_button)
canon_cart_button.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//select[@class='form-select']")))


select_canon_product = driver.find_element(By.XPATH, "//select[@class='form-select']")
scroll_to_element(select_canon_product)
select_canon_product.click()

driver.find_element(By.XPATH, "//option[contains(text(), 'Blue')]").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-lg btn-block']").click()

# Планшет

tablets_link = driver.find_element(By.XPATH, "//a[@class='nav-link'][contains(text(), 'Tablets')]")
scroll_to_element(tablets_link)
tablets_link.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='product-thumb']")))
samsung_cart_button = driver.find_element(By.XPATH, "//div[@class='product-thumb'][.//h4/a[contains(text(), 'Samsung Galaxy Tab 10.1')]]//button[i[@class='fa-solid fa-shopping-cart']]")
scroll_to_element(samsung_cart_button)
samsung_cart_button.click()

# Телефон
phones_link = driver.find_element(By.XPATH, "//a[@class='nav-link'][contains(text(), 'Phones & PDAs')]")
scroll_to_element(phones_link)
phones_link.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='product-thumb']")))
htc_cart_button = driver.find_element(By.XPATH, "//div[@class='product-thumb'][.//h4/a[contains(text(), 'HTC Touch HD')]]//button[i[@class='fa-solid fa-shopping-cart']]")
scroll_to_element(htc_cart_button)
htc_cart_button.click()

# Отзыв
htc_product = driver.find_element(By.XPATH, "//div[@class='product-thumb'][.//h4/a[contains(text(), 'HTC Touch HD')]]")
scroll_to_element(htc_product)
htc_product.click()

write_review = driver.find_element(By.XPATH, "//a[contains(text(), 'Write a review')]")
scroll_to_element(write_review)
write_review.click()

write_review_textbox = driver.find_element(By.XPATH, "//textarea[@class='form-control']")
scroll_to_element(write_review_textbox)
write_review_textbox.send_keys("I love this phone!")

write_review_radiobutton = driver.find_element(By.XPATH, "//input[@value='5']")
scroll_to_element(write_review_radiobutton)
write_review_radiobutton.click()

write_review_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
scroll_to_element(write_review_button)
write_review_button.click()



driver.quit()