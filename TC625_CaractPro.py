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

# Seleccionamos la cantidad de productos = 3
plus = driver.find_element(By.XPATH, "(//a[contains(@class,'plus button')])[1]")
plus.click()
time.sleep(t)
plus.click()
time.sleep(t)

# hacemos click en lo quiero
btnLoQui = driver.find_element(By.XPATH, "//input[contains(@id,'product-add-to-cart')]")
btnLoQui.click()
time.sleep(t)

# hacemos click en ver el carrito
btnVerCa = driver.find_element(By.XPATH, "(//a[@class='btn btn-view-cart'][contains(.,'Ver carrito')])[2]")
btnVerCa.click()
time.sleep(t)

# identificamos el producto y extraemos el texto
caractProd = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/form/div[1]/ul/li/div/div[2]/a/span").text

# identificamos la marca y extraemos el texto
marcaSham = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/form/div[1]/ul/li/div/div[2]/div[2]").text

# identificamos cantidad y extraemos su valor
valueCant = driver.find_element(By.XPATH, "//*[@id='updates_43505241293032']")
valueCant3 = valueCant.get_attribute("value")
# print(type(valueCant3))

# identificamos el precio y extraemos su contenido
precio = driver.find_element(By.XPATH, "(//span[contains(@class,'price')])[2]").text

if caractProd == "Shampoo Oro de Argan Bioregulador 400 grs" and marcaSham == "Dorothy Gray" and valueCant3 == "3" and precio == "$2.760,00":
    print("TC625 PASS")
    print(f"El producto seleccionado es: {caractProd}, la marca es: {marcaSham}, la cantidad seleccionada es: {valueCant3} y el precio total de la compra es: {precio}")
else:
    print("TC625 FAIL")


driver.close()