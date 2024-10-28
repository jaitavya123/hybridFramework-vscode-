from selenium import webdriver

from selenium.common.exceptions import WebDriverException
from globe_var import readVar
from web_pages.login_webPage import login1_                          #imported login1_ to create object in before_scenario
from web_pages.home_webPage import Home1_
from allure_commons.types import AttachmentType
import time
import allure

try: 
 
 def before_scenario(context,scenario):
  #context.auto_obj=webdriver.Chrome()
  browser_name= readVar.var1("DOMAIN","browser")
  print(" before scenario start ",browser_name)
  if(browser_name=="chrome"):
    context.auto_obj= webdriver.Chrome()
  elif(browser_name=="edge"):
    context.auto_obj= webdriver.Edge()
  else:
    print("check your browser")  

  #context.auto_obj.maximize_window() 
  context.auto_obj.get(readVar.var1("DOMAIN","url"))                     #context.auto_obj.get("https://www.saucedemo.com/v1/")
  context.login_obj = login1_(context.auto_obj)                          #object of login1_ class from login_webPage.py
  context.hm_obj =Home1_(context.auto_obj) 
  #time.sleep(4)

  def after_scenario(context,scenario):
    #time.sleep(4)
    context.auto_obj.quit()

 def after_step(context,step):
  if step.status=='failed':
    allure.attach(context.auto_obj.get_screenshot_as_png(),name='failed_ss',attachment_type='AttachmentType.PNG')



except Exception as e:
  print(" Exception caught ",e) 
except WebDriverException as e:  
   print(f" Exception caught {e}")