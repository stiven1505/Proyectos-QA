from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



try:
    # Inicializar el navegador
    driver = webdriver.Chrome()

    def element_id(driver, metodo_locate, identificador, texto = None, tiempo=10, ):
        try:
            element = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((metodo_locate, identificador)))
            if texto is not None:
                element.send_keys(texto)
            return element
        except Exception as e:
            print(f"Funcion element_id, id {identificador} . Error al encontrar elemento : {e}")
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
        try:
            xpath = f"//a[contains(text(), '{texto}')]"
            click = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((By.XPATH, xpath)))
            click.click()
        except Exception as e:
            print(f"Función link_text, texto '{texto}'. Error al encontrar elemento: {e}")
            return None
    
     # Función para esperar hasta que el elemento esté presente por el atributo formCtontrolName 
    def element_control(driver, form_control_name, texto = None, tiempo=10):
        try:
            element = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"[formControlName='{form_control_name}']")))
            if texto is not None:
                    element.send_keys(texto)
            return element
        except Exception as e:
            print(f"Función element_control, formControlName {form_control_name}. Error al encontrar elemento: {e}")
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

    # Función para encontrar y activar el checkbox por texto
    def checkbox_text(driver, texto):
        try:
            xpath = f"//label[text()='{texto}']/input[@type='checkbox']"
            checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            if not checkbox.is_selected():
                checkbox.click()
        except Exception as e:
            print(f"Función checkbox_text, texto '{texto}'. Error al activar el checkbox: {e}")

    # Función para buscar botones por texto
    def button_text(driver, texto):
        try:
            xpath = f"//button[contains(text(), '{texto}')]"
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            boton.click()
        except Exception as e:
            print(f"Función button_text, texto '{texto}'. Error al hacer clic en el botón: {e}")            
        
    # Para abrir la pagina 
    driver.get("https://diydev.com/login")

    # Encontrar y escribir el componente de ingreso de correo
    element_id(driver, By.ID, "email","ejemplos@yahoo.es")
   
    #Encontrar y escribir el componente de ingreso de contraseña
    element_id(driver,By.ID, "exampleInputPassword1","1234*ejemplo")

    # Localizar y hacer clic en el botón ingresar
    button_text(driver," Ingresar a la plataforma")
    
    # Localizar opcion parametrizacion 
    link_href(driver,"/settings/shortcuts")

    # Localizar opcion  Gestión de puntos de venta, rutas y segmentos comerciales
    link_href(driver,"/settings/pdv")
 
    #Localizar link adicionar PDV 
    #Se guarda el id y el nombre del PDV para hacerlo lo mas dinamico.
    name_regional = "1/ANTIOQUIA%20"
    
    link_href(driver,"/settings/pdv/add/"+name_regional)    
    
#--------------- Formulario Nuevo PDV -------------

#------------- Campos obligatorios ---------------
   
    #Nombre del punto de venta
    element_control(driver,"name","PDV QA")
    
    #Pais y Regional se llenan automaticamente
    
    #Departamento
    selection_option(driver, "exampleFormControlSelect1", "3")
    
    #Ciudad - mala practica
    time.sleep(1)
    selection_option(driver, "exampleFormControlSelect1", "258")
    
    #Barrio
    element_control(driver,"district","Centenario")
        
        #Boton Agregar localizacion - API Google
        # Encuentra el botón para agregar localización
    from selenium.webdriver.common.action_chains import ActionChains    
    boton_agregar = driver.find_element(By.CLASS_NAME, 'btn-save')

    # Haz clic en el botón para desplegar el mapa
    boton_agregar.click()

    # Espera a que el mapa esté disponible dentro del iframe
    iframe_mapa = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))

    # Ahora estás dentro del iframe que contiene el mapa
    # Encuentra el mapa (es probable que sea una imagen)
    mapa = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="map"]//img')))

    # Simula arrastrar el mapa (por ejemplo, al centro)
    actions = ActionChains(driver)
    actions.click_and_hold(mapa).move_by_offset(200, 100).release().perform()
    
    
    
    
    
    
    
    
    
    
    
    
    
    time.sleep(7)
   
    #Nivel 1
    selection_option2(driver, "chanel", "1")
    
    #Nivel 2
    selection_option2(driver, "subchanel", "2")
    
    #Nivel 3
    selection_option2(driver, "segmentation", "13")
    
    #Nivel 4
    selection_option2(driver, "tipology", "3")
    
    #Cadena
    selection_option2(driver, "chain", "4")
    
    #Formato
    selection_option2(driver, "format", "5")
    
    #Direccion
    element_id(driver,By.ID, "id_direccion", "Carrera 24 #24-24")
    
    #Estado
    selection_option2(driver, "is_active", "1: true")
    
    #Georeferenciacion obligatoria
    checkbox_text(driver,"Georeferenciación obligatoria ") 
    
    #Seccion desplegable del link agregar otros campos de creacion de PDV
    
    #Link desplegable
   
    for i in range(4):
        link_text(driver," Agregar otros campos de creación de punto de venta ")
        
        #Campo a Agregar
        selection_option2(driver, "field", f"{i+1}: {i+1}")
   
        #Boton agregar campo
        button_text(driver, " Agregar Campo ")
        
        #Boton de confirmacion
        button_text(driver, "CONFIRMAR")

    #Nombre del administrador
    element_control(driver, "manager","Brayan prueba")
    
    
    #Cargo 
    element_control(driver, "manager_position","QA")
    
    #Telefono
    element_control(driver, "phone","123456789")
    
    #Celular
    element_control(driver, "celphone","123456789")
    
    #boton guardar PDV
    button_text(driver, " Guardar punto de venta ")
    
    #Boton confirmar
    button_text(driver,"CONFIRMAR")  
     
    time.sleep(6)


    # Cerrar el navegador
    driver.quit()
except Exception as e: 
    print("ha ocurrido un error:", e)