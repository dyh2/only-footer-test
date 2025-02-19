from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера
driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver
driver.maximize_window()

try:
    # Открытие сайта
    driver.get("https://only.digital/")
    time.sleep(3)  # Даем время для полной загрузки страницы

    # Поиск футера
    footer = driver.find_element(By.TAG_NAME, "footer")
    print("Футер найден!")

    # Проверка наличия элементов в футере
    elements_to_check = {
        "VK": "a[href*='vk.com']",
        "Telegram": "a[href*='t.me']",
        "Behance": "a[href*='behance.net']",
	"Dprofile": "a[href*='dprofile.ru']"
    }

    for element_name, selector in elements_to_check.items():
        try:
            driver.find_element(By.CSS_SELECTOR, selector)
            print(f"Элемент '{element_name}' найден в футере.")
        except Exception as e:
            print(f"Элемент '{element_name}' НЕ найден в футере!")
            raise e

finally:
    # Закрытие браузера
    driver.quit()