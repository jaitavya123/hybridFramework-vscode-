Feature: Purchase product
 @buyprd @smoke
 Scenario: we buy one product
     Given user is already logged in
     When we add single product with one nos in cart
     And fill checkout information and buy product
     Then verify success message and logout