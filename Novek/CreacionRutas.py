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
    
    #Funcion para encontrar un link por medio del texto de esa etiqueta 
    def link_text(driver, texto, tiempo=10):
        try:
            xpath = f"//a[contains(text(), '{texto}')]"
            click = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((By.XPATH, xpath)))
            click.click()
        except Exception as e:
            print(f"Función link_text, texto '{texto}'. Error al encontrar elemento: {e}")
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
    
            
    # Para abrir la pagina 
    driver.get("https://diydev.com/login")

    # Encontrar y escribir el componente de ingreso de correo
    element_id(driver, By.ID, "email","ejemplos@yahoo.es")
   
    #Encontrar y escribir el componente de ingreso de contraseña
    element_id(driver,By.ID, "exampleInputPassword1","1234*ejemplo")

    # Localizar y hacer clic en el botón ingresar
    button_text(driver," Ingresar a la plataforma")
    

    # Localizar opcion parametrizacion 
    link_text(driver," Parametrización ")

    # Localizar opcion  Gestión de puntos de venta, rutas y segmentos 
    link_href(driver,"/settings/pdv")
    
    # Localizar opcion Gestión de rutas
    link_href(driver,"/settings/routes")

    # Localizar link agregar nueva ruta
    link_href(driver,"/settings/routes/add")
    
    #---------- Formulario para creacion de ruta ----------
    
    #Nombre de la ruta
    element_control(driver,"name","Ruta prueba")
    
    #Estado de la ruta
    selection_option2(driver, "is_active", "1: true")
    
    #Boton guardar ruta de labor
    button_text(driver," Guardar ruta de labor")
    
    #Boton confirmar
   # button_text(driver,"CONFIRMAR")  
    
    time.sleep(6)


    # Cerrar el navegador
    driver.quit()
except Exception as e: 
    print("ha ocurrido un error:", e)