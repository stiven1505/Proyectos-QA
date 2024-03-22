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

    # Función para buscar botones por texto
    def button_text(driver, texto):
        try:
            xpath = f"//button[contains(text(), '{texto}')]"
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            boton.click()
        except Exception as e:
            print(f"Función button_text, texto '{texto}'. Error al hacer clic en el botón: {e}")
    
    #Funcion para la busqueda de un ng_select(Se hace todo este proceso por lo que es un componente mas complejo) y escoger una opcion  
    def seleccionar_opcion_ng_select(driver, ng_select_xpath, option_text):
        try:
        # Hacer clic en el elemento <ng-select>
            ng_select_element = driver.find_element(By.XPATH, ng_select_xpath)
            ng_select_element.click()

            # Esperar a que el panel desplegable esté visible
            dropdown_panel_xpath = ng_select_xpath + "/ng-dropdown-panel"
            dropdown_panel = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, dropdown_panel_xpath)))

            # Buscar la opción por el texto que contiene
            option_xpath = f"{dropdown_panel_xpath}//div[contains(text(), '{option_text}')]"

            # Esperar a que la opción específica esté presente y sea clickeable
            specific_option = WebDriverWait(dropdown_panel, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))

            # Hacer clic en la opción específica
            specific_option.click()
        except Exception as e:
            print(f"Error al seleccionar opción en ng-select: {e}")

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
    
    
    # Localizar opcion Asignacion de rutas a usuarios
    link_href(driver,"/settings/routers")
    
    
    # Localizar link adicionar rutero
    link_href(driver,"/settings/routers/add")
    
    
    #---------- Formulario Agregar nuevo rutero ----------

    #Nombre del rutero
    element_control(driver,"name","Rutero pruebas")
    
    #Seleccione el estado del rutero
    selection_option2(driver, "is_active", "1: true")
     
    #Seleccione el tipo
    selection_option(driver,"exampleFormControlSelect1","1")
    
    #Seleccione la fecha de inicio
    element_control(driver,"cycle_init","28-02-2024")
    
    #Seleccione la fecha de final
    cycle_end = element_control(driver,"cycle_end","29-02-2024")
    
    #Seleccione la ruta

    # XPath Full del elemento ng-select
    ng_select_xpath = "/html/body/app-root/app-layout-menu-left/div/div[2]/app-layout-settings/div/div/div[2]/app-add/form/div[5]/select-http/ng-select"
    seleccionar_opcion_ng_select(driver, ng_select_xpath, "Ruta prueba")
    
    #Boton agregar rutero - Ruta prueba
    button_text(driver," Agregar rutero ")
        
    #Boton confirmar
    #button_text(driver,"CONFIRMAR")  
    
    time.sleep(6)


    # Cerrar el navegador
    driver.quit()
except Exception as e: 
    print("ha ocurrido un error general:", e)