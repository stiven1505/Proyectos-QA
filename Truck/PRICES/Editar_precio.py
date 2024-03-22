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
        
    
    #Funcion para encontrar un link por medio del texto de esa etiqueta 
    def link_text(driver, texto, tiempo=10):
        try:
            xpath = f"//a[contains(text(), '{texto}')]"
            click = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((By.XPATH, xpath)))
            click.click()
        except Exception as e:
            print(f"Función link_text, texto '{texto}'. Error al encontrar elemento: {e}")
            return None
    # Funcion para encontrar un link por medio del id 
    
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

    #Funcion para encontrar y seleccionar la opcion en un compornente de tipo select (con el atributo formControlName)    
    def selection_option2(driver, form_control_name, opcion_valor, tiempo=10):
        try:
        # Esperar a que el select esté presente y sea clickeable
            select = WebDriverWait(driver, tiempo).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"select[formControlName='{form_control_name}']"))
            )
            # Hacer clic en el select para abrir las opciones
            select.click()
            # Esperar a que las opciones estén disponibles
            WebDriverWait(driver, tiempo).until(
                EC.presence_of_all_elements_located((By.XPATH, f"//select[@formControlName='{form_control_name}']/option"))
            )
            # Seleccionar la opción deseada
            opcion = select.find_element(By.XPATH, f"//select[@formControlName='{form_control_name}']/option[@value='{opcion_valor}']")
            opcion.click()
        except Exception as e:
            print(f"Función selection_option2, formControlName '{form_control_name}', valor de opción '{opcion_valor}'. Error al seleccionar la opción: {e}")

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
    
    # Encontrar y escribir el componente de ingreso de correo
    element_id(driver, By.ID, "id_username","han_@spam4.me/")
    
    #Encontrar y escribir el componente de ingreso de contraseña
    element_id(driver,By.ID, "id_password","1234567")
   
    # Localizar y hacer clic en el botón ingresar
    click_element(driver,'//*[@id="loginform"]/div/div[4]/div/button')
    
    #Link prices
    element_id2(driver,"/organizations/716/prices/management/")
    
    #Click en menu de tres puntos 
    driver.execute_script("window.scrollBy(0, 1100);") #Para cada precio que se desee editar, toca darle scroll por un comportamiento estraño que tiene a la hora de llegar a esta etiqueta 
    time.sleep(1)
    click_element(driver,'/html/body/div[2]/div/div[2]/div/div[2]/div/div/table/tbody/tr[23]/td[12]/div/a')
    
    
    #Link Add Price
 
    link_href(driver,"/organizations/716/prices/management/edit/41693")
    
    #---------- Formulario Create Price --------------
    """"
    #Effective Date*
    element_id(driver, By.ID, "id_effective_date", "15/03/002024T16:00")
    driver.execute_script("window.scrollBy(0, 150);")
    
    #End Date*
    element_id(driver, By.ID, "id_end_date", "18/03/002024T18:00")
    driver.execute_script("window.scrollBy(0, 150);")
   
    #Provider Organization 
    xpath_span ='//*[@id="idPriceForm"]/div[1]/div[1]/div[1]/div/div[3]/span'  
    xpath_input ='/html/body/span/span/span[1]/input'  
    texto="Mf Freight Forwarders"
    select_span(driver,xpath_span,xpath_input,texto)
    driver.execute_script("window.scrollBy(0, 150);")
    
    #Provider's Line Item*
    xpath_span='//*[@id="idPriceForm"]/div[1]/div[1]/div[1]/div/div[4]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Gasolina"
    select_span(driver,xpath_span,xpath_input,texto)
    
    
    #Currency*
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(1)
    currency = click_element(driver,'//*[@id="idPriceForm"]/div[1]/div[1]/div[1]/div/div[5]/div[1]')   
    time.sleep(1)
    element_id2(driver,"id_currency-opt-1")
    
    
    
    #Stage Type*
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -500);")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -500);")
    click_element(driver,'//*[@id="idPriceForm"]/div[1]/div[2]/div/div/div[2]/div[3]/label')
    
    #General price - check box"""
    """element_id2(driver,"general_price_switch")
    
    
    #---------------Chech box ativado--------------------

    #Land Carrier*
    path_span='//*[@id="land_mode"]/div[1]/span'     
    path_option='//*[@id="select2-id_land_carrier-results"]/li[7]'
    select_span(driver,path_span,path_option)
    
    #Unit type*
    selection_option(driver,"id_unit_type","7")"""
    """
    #---------------Chech box desactivado--------------------
    #Land Carrier*
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(1)
    xpath_span='//*[@id="land_mode"]/div[1]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="Bolivariano"
    select_span(driver,xpath_span,xpath_input,texto)
    driver.execute_script("window.scrollBy(0, 150);")
    
    
    #Las ciudades tienen unas siglas. se hara la busqueda por texto con estas siglas 
    #Origin City*
    xpath_span='//*[@id="origin_destination_land"]/div/div[1]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="COCLO"
    select_span(driver,xpath_span,xpath_input,texto)
    driver.execute_script("window.scrollBy(0, 150);")
    
    time.sleep(1)
    #Destination City*
    xpath_span='//*[@id="origin_destination_land"]/div/div[2]/span'     
    xpath_input='/html/body/span/span/span[1]/input'
    texto="COMDE"
    select_span(driver,xpath_span,xpath_input,texto)
    driver.execute_script("window.scrollBy(0, 150);")   
    
    #Unit type*
    selection_option(driver,"id_unit_type","7")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    #Boton save
    click_element(driver,'//*[@id="save_button_empty"]')
    
    """

    #--------- Conditions ---------------------
    
    # Boton add conditions
    driver.execute_script("window.scrollBy(0, 600);") #Puede variar los pixeles hacer scroll 
    time.sleep(1)
    click_element(driver,'/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[2]/div/div/button')
    
    
    for i in range(3):
        
        selection_option(driver,"id_condition_type",i+1)
        
        if i == 0:
            element_id(driver,By.ID,"free-days-off","2")
            element_id2(driver,"save-condition-button")
            driver.execute_script("window.scrollBy(0, 600);") #Puede variar los pixeles hacer scroll 
            time.sleep(1)
            click_element(driver,'/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/button')
        
        if i == 1:
            element_id(driver,By.ID,"free-days-off","2")
            element_id2(driver,"save-condition-button")
            driver.execute_script("window.scrollBy(0, 600);") #Puede variar los pixeles hacer scroll 
            time.sleep(1)
            click_element(driver,'/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/button')
           
        if i == 2:
            element_id(driver,By.ID,"textarea_othercondition","Prueba")
            element_id2(driver,"save-condition-button")
            

    #--------- Price Values -------------------
    #Boton price values
    # Boton add conditions
    driver.execute_script("window.scrollBy(0, 1000);") #Puede variar los pixeles hacer scroll 
    time.sleep(1)
    click_element(driver,'/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div/div/div[3]/div/div[1]/button')
    
    #-------- Formulario set value ---------
    #Boton Set Value
    click_element(driver,'/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[3]/form/div[1]/div/div[1]/div')
    
    for i in range (4):
            
            #Truck Type
            selection_option(driver,"id_truck_type",i+1)
            
            #Primer caso con solo el -value- digitado
            if i == 0 :
                element_id(driver,By.ID,"id_value","123")
                
                element_id2(driver,"button-save")
                driver.execute_script("window.scrollBy(0, 1200);") #Puede variar los pixeles hacer scroll 
                time.sleep(1)
                click_element(driver,'/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div/div/div[3]/div/div[1]/button')
            
            #Segundo caso -Value, Min range, CheckBox - digitado
            if i == 1:
                #Value
                element_id(driver,By.ID,"id_value","1234")
                #Min Range
                element_id(driver,By.ID,"id_min_units_per_fee","5")
                #Max Range - Check
                element_id2(driver,"lable_id_undefined_max_range")
                
                element_id2(driver,"button-save")
                driver.execute_script("window.scrollBy(0, 1200);") #Puede variar los pixeles hacer scroll 
                time.sleep(1)
                click_element(driver,'/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div/div/div[3]/div/div[1]/button')
           
            #Tercer caso - Value, Min Range, Max Range,Default Profit - digitado
            if i == 2:
                #Value
                element_id(driver,By.ID,"id_value","12345")
                #Min Range
                element_id(driver,By.ID,"id_min_units_per_fee","5")
                time.sleep(2)
                #Max Range
                element_id(driver,By.ID,"id_max_range","10")
                #Default Profit
                element_id(driver,By.ID,"id_profit_value","123")
                
                element_id2(driver,"button-save")
                driver.execute_script("window.scrollBy(0, 1200);") #Puede variar los pixeles hacer scroll 
                time.sleep(1)
                click_element(driver,'/html/body/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div/div/div[3]/div/div[1]/button')
            
            #Cuarto Caso - Value, Min Range, Max Range,Default Profit, Porcentaje - digitado
            if i == 3:
                #Value
                element_id(driver,By.ID,"id_value","123456")
                #Min Range
                element_id(driver,By.ID,"id_min_units_per_fee","5")
                #Max Range
                element_id(driver,By.ID,"id_max_range","10")
                #Default Profit
                element_id(driver,By.ID,"id_profit_value","123")
                #Select en Porcentaje
                selection_option(driver,"id_profit_type","0")
                
                element_id2(driver,"button-save")
                
            
        #Value
        
        #Min range
        
        #Max range
        
        #Default Profit
        
        #
        
        
        
    
    
    #---------- Formulario Sum of cost ------------
    
    
    #---------- Formula
    
    time.sleep(10)


    # Cerrar el navegador
    driver.quit()
except Exception as e: 
    print("ha ocurrido un error general:", e)
            
            
            