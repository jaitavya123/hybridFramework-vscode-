from behave import given, when, then
from web_pages.login_webPage import login1_
from web_pages.home_webPage import Home1_
#import allure
from allure import severity, severity_level


@severity(severity_level.CRITICAL)
@given('user is already logged in')
def ss1(context):
    context.login_obj.valiData("standard_user","secret_sauce")
    

@when('we add single product with one nos in cart')

def ss2(context):
   context.hm_obj.select_prodt()

@when('fill checkout information and buy product')
def ss3(context):
    context.hm_obj.buy1_prodt()

@then('verify success message and logout')
def ss4(context):
    pass #call logout() here