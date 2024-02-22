from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://127.0.0.1:8000/'

credentials_list = []
with open("credentials.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(",")
        credentials_list.append({"username": username, "password": password})

successful_logins = []

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_login = browser.find_element(By.ID, "login")
    button_login.click()

    for credentials in credentials_list:
        input_username = browser.find_element(By.ID, "id_username")
        input_username.send_keys(credentials["username"])

        input_password = browser.find_element(By.ID, "id_password")
        input_password.send_keys(credentials["password"])

        button_submit = browser.find_element(By.ID, "signin")
        button_submit.click()

        if "Витрина товаров" in browser.page_source:
            print(f"Успешный вход для пользователя {credentials['username']}!")
            successful_logins.append(credentials)
            break

        time.sleep(2)
finally:
    time.sleep(4)
    browser.quit()

with open("successful_logins.txt", "w") as file:
    for login in successful_logins:
        file.write(f"Username: {login['username']}, Password: {login['password']}\n")
