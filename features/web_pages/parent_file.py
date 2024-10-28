from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Parent_class:

 def __init__(self,auto_obj):
  self.auto_obj=auto_obj

 def click_element(self,locator_type,locator_value):
  web_element=None

  if(locator_type.endswith("_xpath")):
     web_element=WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH,locator_value))
     )

  elif(locator_type.endswith("_id")):
     web_element=WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.ID,locator_value))
     )
  elif(locator_type.endswith("_name")):
     web_element=WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.NAME,locator_value))
     )
  elif(locator_type.endswith("_class_name")):
     web_element=WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.CLASS_NAME,locator_value))
     )
  elif(locator_type.endswith("_link_text")):
     web_element=WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.LINK_TEXT,locator_value))
     )
  elif(locator_type.endswith("_css")):
     web_element=WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.CSS_SELECTOR,locator_value))
     )  
  web_element.click()     
  return web_element             

 def clear_element(self,locator_type,locator_value): 
    web_element =self.click_element(locator_type,locator_value)
    web_element.clear()

 def send_value_element(self,locator_type,locator_value,data_): 
    web_element =self.click_element(locator_type,locator_value)
    web_element.send_keys(data_)
 