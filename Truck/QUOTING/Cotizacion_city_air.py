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
    
    #Link Quoting
    element_id2(driver,"/organizations/716/requestsquote/")
    
    #Link new Quote
    link_href(driver,"/organizations/716/quick_request_quote/create/")
    
    #Type of shipment 
    element_id2(driver,"type_truck")
    
    #type of pickup 
    element_id2(driver,"type_pickup_city")
    
    #type of deliery
    element_id2(driver,"type_delivery_air")
    
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)
    #ETD*
    element_id(driver, By.ID, "id_departure_datetime", "15/04/002024T16:00")

    #ETA*
    element_id(driver, By.ID, "id_arrival_datetime", "15/04/002024T16:00")
    
    #Check box- Open arrival date 
    #element_id2(driver,"id_open_arrival_datetime")
    
    #--------- Formulario Pick up details ------------------
    
    #Las ciudades tienen unas siglas. se hara la busqueda por texto con estas siglas 
    #Conuntry
    xpath_span='//*[@id="pickup_address_fields"]/div[1]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Colombia"
    select_span(driver,xpath_span,xpath_input,texto)

    
    #City
    xpath_span='//*[@id="pickup_address_fields"]/div[2]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="COCLO"
    select_span(driver,xpath_span,xpath_input,texto)
 
        
    #Address
    element_id(driver,By.ID,"id_origin_address1","Direccion Recogida ")
    
    #Postal code
    element_id(driver,By.ID,"id_origin_postal_code","Codigo Recogida")
    
    #--------- Formulario Delivery details ------------------ 
    
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(1)
    
    #Desplegable - More information
    link_href(driver,"#CollapseMoreInformationDestination")
    
    #Las ciudades tienen unas siglas. se hara la busqueda por texto con estas siglas 
    #Destination Airport
    xpath_span='//*[@id="destination_airport_section_container"]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="MDE"
    select_span(driver,xpath_span,xpath_input,texto)

    
    #Air carrier
    xpath_span='//*[@id="form_extradata_airport_container"]/div[1]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Avianca Cargo (Transportes Aereos Mercantiles Panamericanos S.A. - TAMPA)"
    select_span(driver,xpath_span,xpath_input,texto)
    
    #aircraft_type
    xpath_span='//*[@id="form_extradata_airport_container"]/div[2]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto=""
    select_span(driver,xpath_span,xpath_input,texto)
    
    #flight_number
    element_id(driver,By.ID,"id_flight_number","123")
    
    #airway_bill_number
    element_id(driver,By.ID,"id_airway_bill_number","123")
    
    #tsa_know_id
    element_id(driver,By.ID,"id_tsa_know_id","123")
    
    #Boton continuar
    click_element(driver,'//*[@id="save_button"]')
    
    
    #------------ Formulario Set Cargo details ------------------------
    
    #Cargo mode
    element_id2(driver,"selectFCL")
    
    #Commodities
    xpath_span='//*[@id="cargo-details-template"]/div[1]/div[3]/div/div/span'     
    xpath_input='/html/body/div[2]/div/div[2]/div/div/div/div/form/div/div[3]/div[1]/div[3]/div/div/span/span[1]/span/span/input'
    texto="Aluminum and articles thereof"
    select_span(driver,xpath_span,xpath_input,texto)
    
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(2)
    
    #Po numbers
    element_id(driver,By.NAME,"po_numbers","12345")
    
    #Select your Container/Truck Type
    selection_option_xpath(driver,'//*[@id="cargo-details-template"]/div[1]/div[5]/select',"2")
    
    #link select your trucks 
    click_element(driver,'//*[@id="full-quote-section"]/div[1]/div[2]/a')
    
    #Select trucks
    click_element(driver,'//*[@id="modalContainers"]/div/div/div[2]/div[3]/div/div[1]/div')
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    
    #boton add truck
    click_element(driver,'//*[@id="modalContainers"]/div/div/div[2]/div[4]/button')
    
    #boton editar truck - Flujo aparete 
    #click_element(driver,'//*[@id="full-quote-section"]/div[1]/div[3]/div/div[2]/div[1]/p/a')
    
    #Boton Save And Continue
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(1)
    element_id2(driver,"save_button")
    
    #----------- Formulario client information ---------
    #Client*
    xpath_span='//*[@id="wrapper-content"]/div/form[1]/div/div[2]/div[2]/div/div[2]/span'     
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

    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)
    #-------------Warehouse Contacts -----------------
    
    #Contact
    xpath_span='/html/body/div[2]/div/div[2]/div/form[1]/div/div[2]/div[2]/div/div[6]/div/div[1]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="IMUSA - LOGISTIC PAY 3"
    select_span(driver,xpath_span,xpath_input,texto)
    
    #Notify To
    xpath_span='/html/body/div[2]/div/div[2]/div/form[1]/div/div[2]/div[2]/div/div[6]/div/div[2]/span'     
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
    
    #Boton select 
    click_element(driver,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[4]/button')
    
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(1)
    
    #click boton review quote
    click_element(driver,'//*[@id="app"]/div[4]/div[2]/button')
    
    driver.execute_script("window.scrollBy(0, 3000);")
    time.sleep(2)
    
    #Boton save
    element_id2(driver,"save_review_personalized")
    
    time.sleep(10)


    # Cerrar el navegador
    driver.quit()
except Exception as e: 
    print("ha ocurrido un error general:", e)
            