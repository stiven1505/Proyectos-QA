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

    
    #-----------------------------------

    # Localizar opcion Gestión de usuarios, roles y permisos
    link_href(driver,"/settings/users")
    
    #-----------------------------------

    # Localizar link adicionar usuario
    link_href(driver,"/settings/users/add")
    
    #-----------------------------------

    #Llenado del formulario para ingreso de nuevo usuario

    #------------- Campos Obligatorios -------------------

    #Nombre
    element_id(driver, By.ID, "first_name","Brayan")

    #Apellido
    element_id(driver, By.ID, "last_name","Garcia")
    
    time.sleep(1)
    #Tipo identificacion
    selection_option(driver, "user_id_type","1: 1")

    #Numero identificacion
    element_id(driver, By.ID, "user_id_number","1234567899")
    
    #Correo
    element_id(driver, By.ID, "email","ejemplo@gmail.com")

    #Numero Telefono
    element_id(driver, By.ID, "mobile_phone","12356789")
   

    time.sleep(1)
    #------------- Campos No Obligatorios -------------------

    #Pais
    selection_option(driver, "country", "10: 1")
    time.sleep(1)
    
    #Regional
    selection_option(driver, "regional", "8: 10")
    time.sleep(1)
    
    #Departamento
    selection_option(driver, "state", "31: 3")
    time.sleep(1)
    
    #Ciudad
    selection_option(driver, "city", "7: 258")
    time.sleep(1)
    
    #Estado del usuario
    selection_option(driver, "is_active", "1")

    #------------- Campos No Obligatorios -------------------

    element_id(driver, By.ID, "assigned_cel","123456789")

    #------------- Campos Obligatorios -------------------
    #Roles
    checkbox_text(driver, " Tiene rol web *")
    
    #Rol Web
    selection_option2(driver,"role_web","1: 1")
    
    #Rol del jefe
    selection_option(driver,"role_boss","1: 6")
    
    #Jefe directo 
    selection_option(driver,"user_boss", "")

    #------------- Campos No Obligatorios -------------------
    #Rol del jefe

    selection_option(driver, "role_boss", "6: 12")
    time.sleep(1)


    #Jefe directo / Falta asignacion
    #selection_option(driver, "user_boss", "1: 1")
    #time.sleep(1)

    #Boton agregar otros campos de creacion de usuario

    button_text(driver, " Agregar otros campos de creación de usuario ")

    #-------------Seccion desplegable ---------------------

    #Tipo de georeferenciación
    selection_option(driver,"georeferencing","3")

    #Tipo de horario
    selection_option(driver,"flexible_schedule","1")

    #Código externo
    element_id(driver,By.ID, "external_code","123456")
    
    #¿Tiene cupo asignado?
    selection_option(driver, "assigned_quota", "true")

    #¿Es asesor asociado?
    selection_option(driver,"associate_advisor", "true")

    #Boton guardar
    button_text(driver," Guardar Usuario ")

    time.sleep(5)


    # Cerrar el navegador
    driver.quit()
except Exception as e: 
    print("ha ocurrido un error:", e)
