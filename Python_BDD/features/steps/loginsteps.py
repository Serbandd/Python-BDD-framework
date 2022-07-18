
from behave import *
from selenium import webdriver

@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()



@when('I open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element_by_id("txtUsername").send_keys(username)
    context.driver.find_element_by_id("txtPassword").send_keys(password)
    


@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()
    context.driver.implicitly_wait(5)
      



@then('User must successfully login to the Dasboard page')
def step_impl(context):

    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
        print(text)

    except:
        assert False, "Test Failed"
        context.driver.close()

    if text == "Dashboard":
        assert True, "Test Passed"
        context.driver.close()

 

