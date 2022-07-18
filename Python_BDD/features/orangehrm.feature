
Feature: OrangeHRM Logo

    Scenario: Logo presence on OrangeHRM home Page
        #precondition
        Given launch chrome browser 
        # Some event
        When open orange hrm homepage 
        #Some condition
        Then verify that the logo present on Page 
        And close browser

        
