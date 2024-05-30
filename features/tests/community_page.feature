# Created by kmcha at 5/29/2024
Feature: Community Page Tests

  Scenario: User can open the community page
    Given Open the main page
    When Login to the page
    Then Click on settings option
    Then Click on community option
    Then Verify the right page opens
    Then Verify Contact support button is available and clickable
