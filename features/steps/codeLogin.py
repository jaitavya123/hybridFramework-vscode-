from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.web_pages.login_webPage import login1_
import allure


@given('user on login page')
def start_(context):
  print("inside given")
  context.og_url="https://www.saucedemo.com/v1/"                            #url of sauce demo
  context.present_url=context.auto_obj.current_url
  #print("--------->",context.auto_obj.current_url)
  assert context.og_url==context.present_url,"incorrect url"
  
@when('we fill valid credential')
@allure.severity(allure.severity_level.CRITICAL)
def putdata(context):
  context.login_obj.valiData("standard_user","secret_sauce")                         #function call from login_webPage.py
  print("in side when")

@then('login process complete and logout now')
def taskDone(context):
 context.login_obj.logout()
 print("in side then")

@given('user already on login page')
def start_(context):
  print("inside given")
  context.og_url="https://www.saucedemo.com/v1/"                            #url of sauce demo
  context.present_url=context.auto_obj.current_url
  #print("--------->",context.auto_obj.current_url)
  assert context.og_url==context.present_url,"incorrect url"

@when('we fill invalid {username} and {password}')
def putdata(context,username,password):
  #context.login_obj2=login1_(context.auto_obj)
  context.login_obj.valiData(username,password)                         #function call from login_webPage.py
  print("in-side when")

@then('error message appear,process complete')
def taskDone(context):
 context.login_obj.validation_msg()
 print("in-side then")
