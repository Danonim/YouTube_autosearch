from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

title = input("Введіть назву відео: ")

driver = webdriver.Chrome()

def main():

    try:
        driver.maximize_window()
        driver.get("https://www.youtube.com")
        driver.find_element(By.NAME, "search_query").send_keys(title)
        driver.find_element(By.CSS_SELECTOR, "#search-icon-legacy.ytd-searchbox").click()

        wait = WebDriverWait(driver, 100)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]/yt-formatted-string')))
        driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string').click()
    except:
        print("Купи інтернет клоун")


if __name__ == "__main__":
    main()
