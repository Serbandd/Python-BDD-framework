from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()



@when('open orange hrm homepage')
def openhomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo present on Page')
def verifyLogo(context):

    status = context.driver.find_element_by_xpath("//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]").is_displayed() #returns boolean statements

    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()

