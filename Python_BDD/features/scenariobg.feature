
Feature: OrangeHRM Login

    Background: coomon steps
        Given I launch chrome browser
        # Some event
        When I open application
        And Enter valid username and password
        And Click on login




    Scenario: Login to HRM Application
        #precondition
        #Some condition
        Then User must login to Dashboard page

    Scenario: Search user
        #precondition
        When Navigate to search page
        #Some condition
        Then search page should display

    Scenario: Advanced Search user
        #precondition
        When Navigate to advanced search page
        #Some condition
        Then search page should display

