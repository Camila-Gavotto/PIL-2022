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

# hacemos click en lo quiero
btnLoQui = driver.find_element(By.XPATH, "//input[contains(@id,'product-add-to-cart')]")
btnLoQui.click()
time.sleep(t)

# hacemos click en ver el carrito
btnVerCa = driver.find_element(By.XPATH, "(//a[@class='btn btn-view-cart'][contains(.,'Ver carrito')])[2]")
btnVerCa.click()
time.sleep(t)

# hacemos click en quitar
remove = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/form/div[1]/ul/li/div/div[2]/div[4]/div[2]/a").click()
time.sleep(t)

# mensaje de validación
msjVal = driver.find_element(By.XPATH, "//p[contains(@class,'alert alert-warning')]").text
time.sleep(t)

# validar carrito vacio
carro = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div/div[2]/div[2]/div/div/div[3]/div[1]/a")
carro.click()
time.sleep(4)
msjCarro = driver.find_element(By.XPATH, "//p[contains(@class,'cart_empty')]").text

# validación
if msjVal == msjCarro:
    print(msjCarro)
    print("TC626 PASS")
else:
    print("TC626 FAIL")


driver.close()
