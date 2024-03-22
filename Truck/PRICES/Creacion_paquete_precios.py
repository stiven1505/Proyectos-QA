from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

try:
    # Inicializar el navegador
    driver = webdriver.Chrome()

    #Funcion para encontrar elementos por id que pasa por parametro un texto 
    def element_id(driver, metodo_locate, identificador, texto = None, tiempo=10, ):
        try:
            element = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((metodo_locate, identificador)))
            if texto is not None:
                element.send_keys(texto)
            return element
        except Exception as e:
            print(f"Funcion element_id, id {identificador} . Error al encontrar elemento : {e}")
            return None
    
    #Funcion para encontrar elementos por id que da click
    def element_id2(driver, identificador, tiempo=10, ):
        try:
            element = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((By.ID, identificador)))
            element.click()
        except Exception as e:
            print(f"Funcion element_id2, id {identificador} . Error al encontrar elemento : {e}")
            return None
            
    # Funcion para encontrar un link por medio del href
    def link_href(driver, href_valor, tiempo=10):
        try:
            xpath = f"//a[@href='{href_valor}']"
            click = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((By.XPATH, xpath)))
            click.click()
        except Exception as e:
            print(f"Función link_href, href '{href_valor}'. Error al encontrar elemento: {e}")
            return None

    #Funcion para encontrar y seleccionar la opcion en un compornente de tipo select
    def selection_option(driver, select_id, opcion_valor, tiempo=10):
        try:
        # Esperar a que el select esté presente y sea clickeable
            select = WebDriverWait(driver, tiempo).until(EC.element_to_be_clickable((By.ID, select_id)))
            # Hacer clic en el select para abrir las opciones
            select.click()
            # Esperar a que las opciones estén disponibles
            WebDriverWait(driver, tiempo).until(EC.presence_of_all_elements_located((By.XPATH, f"//select[@id='{select_id}']/option")))
            # Seleccionar la opción deseada
            opcion = driver.find_element(By.XPATH, f"//select[@id='{select_id}']/option[@value='{opcion_valor}']")
            opcion.click()
        except Exception as e:
            print(f"Función selection_option, ID '{select_id}', valor de opción '{opcion_valor}'. Error al seleccionar la opción: {e}")

    # Función para buscar botones por texto
    def button_text(driver, texto):
        try:
            xpath = f"//button[contains(text(), '{texto}')]"
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            boton.click()
        except Exception as e:
            print(f"Función button_text, texto '{texto}'. Error al hacer clic en el botón: {e}")
    
    
    #Funcion para el manejo de select con span 
    def select_span(driver,path_span,xpath_input,texto,tiempo=10):
        try:
            select = driver.find_element(By.XPATH, path_span)#xPath del primer Span despues del select 
            select.click() 
            time.sleep(1)
            element = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located(('xpath', xpath_input)))
            if texto is not None:
                    element.send_keys(texto)
                    time.sleep(1)
                    element.send_keys(Keys.ENTER)
                    time.sleep(1)
            else:
                print(f"Texto no encontrado: {texto}")
            
        except Exception as e:
            print(f"Error al seleccionar el select_span: {path_span}, e {e}")
  
    #Funcion para encontrar y activar un checkbox por id
    def checkbox_id(driver, id):
        try:
            xpath = f"//input[@id='{id}' and @type='checkbox']"
            checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            if not checkbox.is_selected():
                checkbox.click()
        except Exception as e:
            print(f"Función checkbox_id, id '{id}'. Error al activar el checkbox: {e}")
            
    #Funcion para hacer click a un elemento x por el Xpath
    def click_element(driver, xpath):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()

        except Exception as e:
            print(f"Error al hacer clic en el elemento:xPath {xpath}, e {e}")
    

        
    # Para abrir la pagina 
    driver.get("https://uat.com/accounts/login/")
    
    zoom_factor = 100
    driver.execute_script(f"document.body.style.zoom = '{zoom_factor}%'")
    
    # Encontrar y escribir el componente de ingreso de correo
    element_id(driver, By.ID, "id_username","han_@spam4.me/")
    
    #Encontrar y escribir el componente de ingreso de contraseña
    element_id(driver,By.ID, "id_password","1234567")
   
    # Localizar y hacer clic en el botón ingresar
    click_element(driver,'//*[@id="loginform"]/div/div[4]/div/button')
    
    #Link prices
    element_id2(driver,"/organizations/716/prices/management/")
    
    #Link price bundle
    link_href(driver,"/organizations/716/prices/management/bundle")
    
    #Link new bundle
    link_href(driver,"/organizations/716/prices/management/bundle/create")
    
    
    #---------FOrmulario create price bundle ------------------------
    
    #Bundle Name 
    element_id(driver,By.ID,"id_name","Prueba QA")
    
    #Effective date
    element_id(driver,By.ID,"id_effective_date","8/03/2024")
    
    #End date
    element_id(driver,By.ID,"id_end_date","18/03/2024")
    
    driver.execute_script("window.scrollBy(0, 150);")
    time.sleep(1)
    
    #Main transport 
    selection_option(driver,"id_main_transport","2")
    
    #Type of movement / Door to door default
    
    
    #Currency / USD default
    
    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)
    
    #Origin Country
    xpath_span='//*[@id="wrapper-content"]/div/form/fieldset/div/div[1]/div/div[7]/span[1]'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Colombia"
    select_span(driver,xpath_span,xpath_input,texto)
    
    #Origin city
    xpath_span='//*[@id="wrapper-content"]/div/form/fieldset/div/div[1]/div/div[8]/span[1]'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="COBOG"
    select_span(driver,xpath_span,xpath_input,texto)    
    
    #Provider carrier
    xpath_span='//*[@id="ctc_land_carrier_receipt"]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Bolivariano"
    select_span(driver,xpath_span,xpath_input,texto)
    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)    
    
    #Destination country
    xpath_span='//*[@id="wrapper-content"]/div/form/fieldset/div/div[1]/div/div[10]/span[1]'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Ecuador"
    select_span(driver,xpath_span,xpath_input,texto)    
    
    #Destination city
    xpath_span='//*[@id="wrapper-content"]/div/form/fieldset/div/div[1]/div/div[11]/span[1]'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="ECUIO"
    select_span(driver,xpath_span,xpath_input,texto)    
    
    #Transit time *Hours
    element_id(driver,By.ID,"id_estimated_intransit_receipt","24")
    
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(1)
     
    #first CheckBox
    checkbox_id(driver,"id_is_consolidated")
    
    #Second CheckBox
    checkbox_id(driver,"id_is_carrier_consolidated")
    

    #Boton save
    element_id2(driver,"save_form")

    
    
    
    time.sleep(10)


    # Cerrar el navegador
    driver.quit()
except Exception as e: 
    print("ha ocurrido un error general:", e)
            