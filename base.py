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
    
    #Funcion para encontrar elementos por id que da click
    def element_id2(driver, identificador, tiempo=10, ):
        try:
            element = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((By.ID, identificador)))
            element.click()
        except Exception as e:
            print(f"Funcion element_id2, id {identificador} . Error al encontrar elemento : {e}")
            return None 
          
    # Función para esperar hasta que el elemento esté presente por CLASS del DOM
    def element_class(driver, clase, texto = None, tiempo=10):
        try:
            element = WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((By.CLASS_NAME, clase)))
            if texto is not None:
                    element.send_keys(texto)
            return element
        except Exception as e:
            print(f"Función element_class, clase {clase}. Error al encontrar elemento: {e}")
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

    #Funcion para encontrar y activar un checkbox por id
    def checkbox_id(driver, id):
        try:
            xpath = f"//input[@id='{id}' and @type='checkbox']"
            checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            if not checkbox.is_selected():
                checkbox.click()
        except Exception as e:
            print(f"Función checkbox_id, id '{id}'. Error al activar el checkbox: {e}")

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


   
    time.sleep(6)


    # Cerrar el navegador
    driver.quit()
except Exception as e: 
    print("ha ocurrido un error general:", e)
            
            
            