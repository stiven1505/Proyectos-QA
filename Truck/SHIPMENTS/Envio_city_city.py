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

    #Funcion para encontrar y seleccionar la opcion en un compornente de tipo select por xpath
    def selection_option_xpath(driver, select_xpath, opcion_valor, tiempo=10):
        try:
            # Esperar a que el select esté presente y sea clickeable
            select = WebDriverWait(driver, tiempo).until(EC.element_to_be_clickable((By.XPATH, select_xpath)))
            # Hacer clic en el select para abrir las opciones
            select.click()
            # Esperar a que las opciones estén disponibles
            WebDriverWait(driver, tiempo).until(EC.presence_of_all_elements_located((By.XPATH, f"{select_xpath}/option")))
            # Seleccionar la opción deseada
            opcion = driver.find_element(By.XPATH, f"{select_xpath}/option[@value='{opcion_valor}']")
            opcion.click()
        except Exception as e:
            print(f"Función selection_option, XPath '{select_xpath}', valor de opción '{opcion_valor}'. Error al seleccionar la opción: {e}")


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
                    time.sleep(3)
                    element.send_keys(Keys.ENTER)
                    time.sleep(1)
            else:
                print(f"Texto no encontrado: {texto}")
            
        except Exception as e:
            print(f"Error al seleccionar el select_span: {path_span}, e {e}")
            
    def select_input(driver, xpath_div, id_input, texto):
        try:
            # Hacer clic en el elemento con el XPath proporcionado
            element = driver.find_element(By.XPATH, xpath_div)
            element.click()
            time.sleep(1)

            # Encontrar el elemento con el ID proporcionado y enviarle texto
            e = element_id(driver, By.ID, id_input, texto)
            time.sleep(1)

            # Enviar la tecla ENTER
            e.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error al seleccionar el select_input: {id_input}, e {e}")
  
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
    
    #Link Shipments
    element_id2(driver,"/organizations/716/shipments/")
    
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)
    
    #Link new Shipment
    link_href(driver,"/organizations/716/fast_shipment_process/")
    
    #Option new Shipment
    link_href(driver,"/organizations/716/quick_shipment/create/")
    
    #Type of shipment 
    element_id2(driver,"type_truck")
    
    #type of pickup 
    element_id2(driver,"type_pickup_city")
    
    #type of deliery
    element_id2(driver,"type_delivery_city")
    
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)
    #ETD*
    element_id(driver, By.ID, "id_departure_datetime", "15/04/002024T16:00")

    #ETA*
    element_id(driver, By.ID, "id_arrival_datetime", "15/04/002024T16:00")
    
    #Check box- Open arrival date 
    #element_id2(driver,"id_open_arrival_datetime")
    
    #--------- Formulario Pickup details ------------------
    
    #Las ciudades tienen unas siglas. se hara la busqueda por texto con estas siglas 
    #Conuntry
    xpath_span='//*[@id="origin_address_fields"]/div[2]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Colombia"
    select_span(driver,xpath_span,xpath_input,texto)

    
    #City 
    xpath_div = '//*[@id="origin_address_fields"]/div[3]/div/div[1]'
    id_input = "id_origin_ts_standardcity-ts-control"
    texto = "Coclo"
    select_input(driver, xpath_div, id_input, texto)
 
        
    #Address
    element_id(driver,By.ID,"id_origin_address1","Direccion Recogida ")
    
    #Postal code
    element_id(driver,By.ID,"id_origin_postal_code","Codigo Recogida")
    
    #additional delivery information
    element_id(driver,By.ID,"id_pickup_observations","pickupo bservations")
    
    #--------- Formulario Delivery details ------------------ 
    
    #Las ciudades tienen unas siglas. se hara la busqueda por texto con estas siglas 
    #Conuntry
    xpath_span='//*[@id="destination_address_fields"]/div[2]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Colombia"
    select_span(driver,xpath_span,xpath_input,texto)

    
    #City
    xpath_div = '//*[@id="destination_address_fields"]/div[3]/div/div[1]'
    id_input = "id_destination_ts_standardcity-ts-control"
    texto = "COMDE"
    select_input(driver, xpath_div, id_input, texto)
        
    #Address
    element_id(driver,By.ID,"id_destination_address1","Direccion llegada ")
    
    #Postal code
    element_id(driver,By.ID,"id_destination_postal_code","Codigo llegada")
    
    #additional delivery information
    element_id(driver,By.ID,"id_delivery_observations","pickupo bservations")
    
    #Shipment observations 
    element_id(driver,By.ID,"id_observations","observations ")
    
    driver.execute_script("window.scrollBy(0, -300);")
    time.sleep(2)
    
    #Boton continuar
    click_element(driver,'//*[@id="save_button"]')
    
    
    #------------ Formulario Set Cargo details ------------------------
    
    #Cargo mode
    element_id2(driver,"cargo_full_container_load")
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    #Commodities
    xpath_span='//*[@id="app"]/div[1]/div[3]/div/div/span'     
    xpath_input='/html/body/div[2]/div/div[2]/div/div[1]/div/form/div[2]/div[3]/div[1]/div[3]/div/div/span/span[1]/span/span/input'
    texto="Aluminum and articles thereof"
    select_span(driver,xpath_span,xpath_input,texto)
    
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(2)
    
    #Po numbers
    element_id(driver,By.ID,"poNumbersSelect-ts-control","12345")
    
    #Select your Container/Truck Type
    selection_option(driver,"selectContainerTruck","TRUCK")
    
    #link select your trucks 
    click_element(driver,'//*[@id="full-truck-section"]/div/div/div[2]/a')
    
    #Select trucks
    click_element(driver,'//*[@id="general_truck_list"]/div[1]/div')
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)
    
    #boton add truck
    click_element(driver,'/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div[4]/button')
    
    #boton editar truck - Flujo aparte 
    #click_element(driver,'//*[@id="full-quote-section"]/div[1]/div[3]/div/div[2]/div[1]/p/a')
    
    #Boton Save And Continue
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(1)
    element_id2(driver,"save_button")
   
    #----------- Formulario client information ---------
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(1)
    #Client*
    xpath_span='//*[@id="form_client"]/div[2]/div[2]/div[2]/div/div[2]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="IMUSA"
    select_span(driver,xpath_span,xpath_input,texto)
    
    #Type
    selection_option(driver,"id_type_of_client_costumer","0")

    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)
    """#Client Contact*
    xpath_span='//*[@id="wrapper-content"]/div/form[1]/div/div[2]/div[2]/div/div[4]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="" #nOMBRE DEL CLIENTE
    select_span(driver,xpath_span,xpath_input,texto)
    
    #Contract number - NO CARGAN LOS NUMEROS 
    xpath_span='//*[@id="pickup_address_fields"]/div[1]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Colombia"
    select_span(driver,xpath_span,xpath_input,texto)"""


    #-------------Warehouse Contacts -----------------
    
    #Contact
    xpath_span='//*[@id="id_container_consignee"]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="IMUSA - LOGISTIC PAY 3"
    select_span(driver,xpath_span,xpath_input,texto)
    
    #Notify To
    xpath_span='//*[@id="form_client"]/div[2]/div[2]/div[2]/div/div[6]/div/div[3]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="IMUSA - LOGISTIC PAY 3"
    select_span(driver,xpath_span,xpath_input,texto)
    
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(1)
    
    #boton see results
    element_id2(driver,"save_button")
    
    #-------------- Ventana Truck Shedules ---------------
    driver.execute_script("window.scrollBy(0, 150);")
    time.sleep(1)
    
    #Boton Review 
    click_element(driver,'/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/div/div/div/div[4]/button')
    
    driver.execute_script("window.scrollBy(0, 1500);")
    time.sleep(3)
    
    #click boton Book Now
    click_element(driver,'//*[@id="submit_form"]')
    
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)
    
    #seleccionar stage
    click_element(driver,"/html/body/div[2]/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div/div/div[3]/button")
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(2)
    
    element_id(driver,By.ID,"id_booking_number","123")
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(2)
    
    #Boton save
    element_id2(driver,"save_button")
    
    time.sleep(10)


    # Cerrar el navegador
    driver.quit()
except Exception as e: 
    print("ha ocurrido un error general:", e)
            