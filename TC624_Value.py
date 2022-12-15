import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# variable para tiempo
t = 2

driver = webdriver.Chrome()
driver.get("https://bertoldi.com.ar/")

driver.find_element(By.XPATH, "//*[@id='sticky-wrapper']/div/div/div[1]/div/div[3]/div[1]/a").click()
time.sleep(t)
driver.maximize_window()
time.sleep(t)

suscriw = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='js-pushowl-no-button pushowl-optin__button pushowl-optin__no-button'][contains(.,'Luego')]")))
suscrif = driver.find_element(By.XPATH, "//button[@class='js-pushowl-no-button pushowl-optin__button pushowl-optin__no-button'][contains(.,'Luego')]")
suscrif.click()
time.sleep(t)

# Login con usuario válido
email = driver.find_element(By.XPATH, "//input[contains(@name,'customer[email]')]")
email.send_keys("cami@gmail.com")
passw = driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
passw.send_keys("admin1234" + Keys.ENTER)
time.sleep(t)

# buscar en la search bar
searchBar = driver.find_element(By.XPATH, "(//input[contains(@type,'search')])[2]")
searchBar.click()
searchBar.send_keys("Shampoo dorothy gray argan" + Keys.ENTER)
time.sleep(t)

# seleccionar el producto
shampoo = driver.find_element(By.XPATH, "//span[contains(.,'Shampoo Oro de Argan Bioregulador 400 grs')]")
shampoo.click()

# encontrar el botón al que le voy a realizar las validaciones
value = driver.find_element(By.XPATH, "//input[contains(@id,'product-add-to-cart')]")
valueLq = value.get_attribute("value")

# validación del value del botón encontrado
if valueLq == "Agregar al carrito":
    print("TC624 PASS")
else:
    print("TC624 FAIL")
    print("El value actual del botón es: ", valueLq)
    print("El value correcto del botón debe ser: Agregar al carrito ")

time.sleep(t)
driver.close()
