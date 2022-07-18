
Feature: OrangeHRM Login

    Scenario: Logo presence on OrangeHRM with valid parameters
        #precondition
        Given I launch chrome browser
        # Some event
        When I open orange hrm homepage
        And Enter username "admin" and password "admin123"
        And Click on login button
        #Some condition
        Then User must successfully login to the Dasboard page

    Scenario Outline: Login to OrangeHRM with Multiple parameters
        #precondition
        Given I launch chrome browser
        # Some event
        When I open orange hrm homepage
        And Enter username "<username>" and password "<password>"
        And Click on login button
        #Some condition
        Then User must successfully login to the Dasboard page

        Examples:
            | username | password |
            | admin    | admin123 |
            | admin123 | admin    |
            | adminxyz | admin123 |
            | admin    | adminxyz |

