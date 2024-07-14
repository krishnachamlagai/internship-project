Feature: Signup tests

  Scenario Outline: The user can enter the information into the input fields on the registration page
    Given Open signup page
    Then Enter account information <fullname> <phone> <email> <password> in the text fields
    Then Verify entered account information <fullname> <phone> <email> <password> is present
    Examples:
      | fullname          | phone      | email            | password         |
      | Krishna | 0001112234 | krishna@test.com | MyStrongPassword |


