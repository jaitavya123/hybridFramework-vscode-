from web_pages.parent_file import Parent_class
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Home1_(Parent_class):                     #inheriting parent_class in home1_   

 def __init__(self,auto_obj):
  super().__init__(auto_obj)

 logoutbtn_id='logout_sidebar_link'
 menubtn_xpath="//div[@class='bm-burger-button']"
 prdt1_xpath="//a[@id='item_4_title_link']" #//div[text()='Sauce Labs Bike Light']"                  # normalize-space() attribute may alsowork here
 prdt2_xpath="//div[normalize-space()='Sauce Labs Bike Light']"
 add2cart_btn_xpath="//button[@class='btn_primary btn_inventory']"
 carticon_xpath="//a[@class='shopping_cart_link fa-layers fa-fw']//*[name()='svg']"
 cart_quantity_xpath="//div[@class='cart_quantity']"
 checkout_btn_xpath="//a[@class='btn_action checkout_button']"
 checkout_fn_xpath="//input[@id='first-name']"
 checkout_ln_xpath="//input[@id='last-name']"
 checkout_postal_xpath="//input[@id='postal-code']"
 checkout_continue_xpath="//input[@type='submit']"
 finish_xpath="//a[@href='./checkout-complete.html']"

 def select_prodt(self):
  self.click_element("prdt1_xpath",self.prdt1_xpath)
  self.click_element("add2cart_btn_xpath",self.add2cart_btn_xpath)
  self.click_element("carticon_xpath",self.carticon_xpath)
  self.click_element("checkout_btn_xpath",self.checkout_btn_xpath)

 def buy1_prodt(self):
  self.click_element("checkout_fn_xpath",self.checkout_fn_xpath)
  self.clear_element("checkout_fn_xpath",self.checkout_fn_xpath)
  self.send_value_element("checkout_fn_xpath",self.checkout_fn_xpath,"test name")
  self.send_value_element("checkout_ln_xpath",self.checkout_ln_xpath,"test last name")
  self.send_value_element("checkout_postal_xpath",self.checkout_postal_xpath,"6576576")
  self.click_element("checkout_continue_xpath",self.checkout_continue_xpath)
  self.click_element("finish_xpath",self.finish_xpath)
  