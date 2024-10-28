from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class login1_:
 def __init__(self,auto_obj):
  self.auto_obj = auto_obj

 username_xpath="//input[@id='user-name']"
 paswd_xpath="//input[@id='password']"
 loginbtn_id="login-button"
 logoutbtn_id='logout_sidebar_link'
 menubtn_xpath="//div[@class='bm-burger-button']"
 errormsg_xpath="//h3[@data-test='error']"                      #validation on invalid credential

 def valiData(self,username,password):
   
   url_login="https://www.saucedemo.com/v1/inventory.html"

   WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH,self.username_xpath))
    ).send_keys(username)
    
    # Wait for the password field and enter the password
   WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.presence_of_element_located((By.XPATH,self.paswd_xpath))
    ).send_keys(password)

    # Wait for the login button to be clickable
   WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.ID,'login-button'))
    ).click()
   
   url_2=self.auto_obj.current_url
   assert url_2==url_login,"  Login failed"
   

 def logout(self):
   url1="https://www.saucedemo.com/v1/inventory.html"
   url2=self.auto_obj.current_url

   if(url1==url2):
    print("----------->",url2)
    WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH,self.menubtn_xpath))
    ).click()
   
   WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.ID,self.logoutbtn_id))
    ).click()
  
 def validation_msg(self):
    time.sleep(7)
    try:  
     a=WebDriverWait(self.auto_obj, 10, poll_frequency=1).until(EC.element_to_be_clickable((By.ID,self.errormsg_xpath))
     ).is_displayed()
     print(a)
     assert a is True,"error msg not appearing "
    except TimeoutException as e:
     print("Error message element was not found or not clickable within the time limit.",e)