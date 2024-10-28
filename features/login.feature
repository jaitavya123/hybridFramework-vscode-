Feature: Login panel of saucedemo verify credentials
 @loginvalid
 Scenario: we use valid credential to login
     Given user on login page
     When we fill valid credential
     Then login process complete and logout now
 @logineg
 Scenario Outline: login with invalid credential
      Given user already on login page
      When we fill invalid <username> and <password>
      Then error message appear,process complete
      Examples:
               |username              |password|
               |testuser              |testpass  |
               |#@%@$@$^              |^$#^$Rpass456  |