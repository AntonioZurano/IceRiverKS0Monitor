
"""Este script utiliza Selenium para automatizar el proceso de inicio de sesión en una aplicación web y guardar el contenido HTML resultante en un archivo.
Módulos:
    - selenium: Proporciona herramientas para la automatización de navegadores web.
    - time: Proporciona funciones relacionadas con el tiempo.
Configuración:
    - Chrome está configurado para ejecutarse en modo headless (sin interfaz gráfica).
Pasos:
    1. Configurar Selenium con Chrome en modo headless.
    2. Navegar a la página de inicio de sesión.
    3. Rellenar el formulario de inicio de sesión con el nombre de usuario y la contraseña proporcionados.
    4. Hacer clic en el botón de inicio de sesión.
    5. Esperar a que la siguiente página se cargue.
    6. Recuperar el contenido HTML de la página.
    7. Guardar el contenido HTML en un archivo llamado "ks0.log".
    8. Cerrar el navegador.
    - url (str): La URL de la página de inicio de sesión.
    - username_field (WebElement): El campo de entrada del nombre de usuario.
    - password_field (WebElement): El campo de entrada de la contraseña.
    - login_button (WebElement): El botón de inicio de sesión.
    - html_content (str): El contenido HTML de la página después del inicio de sesión.
Excepciones:
    - Asegura que el navegador se cierre correctamente en el bloque 'finally'."""

""" Versin 1.0.0
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configuración de Selenium para usar Chrome en modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")

# URL de inicio de sesión
url = "http://192.168.1.193/user/login"

# Configuración de Selenium para usar Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Acceder a la página de inicio de sesión
    driver.get(url)

    # Rellenar los campos de inicio de sesión
    username_field = driver.find_element(By.NAME, "user")
    password_field = driver.find_element(By.NAME, "pwd")
    username_field.send_keys("admin")
    password_field.send_keys("12345678")

    # Hacer clic en el botón de inicio de sesión
    login_button = driver.find_element(By.CLASS_NAME, "loginBtn")
    login_button.click()

    # Esperar a que la página siguiente se cargue
    time.sleep(5)  # Aumenta este tiempo de espera si es necesario

    # Obtener el código HTML de la página
    html_content = driver.page_source

    # Guardar el contenido HTML en un archivo
    with open("ks0.log", "w", encoding="utf-8") as file:
        file.write(html_content)

finally:
    # Cerrar el navegador al final
    driver.quit()
"""
""" Version mejorada 1.0.1 con ChatGPT"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración de Selenium para usar Chrome en modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")

# URL de inicio de sesión
url = "http://192.168.1.193/user/login"

# Configuración de Selenium para usar Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Acceder a la página de inicio de sesión
    driver.get(url)

    # Rellenar los campos de inicio de sesión
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user"))
    )
    password_field = driver.find_element(By.NAME, "pwd")
    username_field.send_keys("admin")
    password_field.send_keys("12345678")

    # Hacer clic en el botón de inicio de sesión
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "loginBtn"))
    )
    login_button.click()

    # Esperar a que la página siguiente se cargue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Obtener el código HTML de la página
    html_content = driver.page_source

    # Guardar el contenido HTML en un archivo
    with open("ks0.log", "w", encoding="utf-8") as file:
        file.write(html_content)

finally:
    # Cerrar el navegador al final
    driver.quit()
