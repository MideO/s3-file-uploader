Feature: Not found pages redirected to index
  As a user
  I want to be redirected to the index page when I navigate to a non existent page url
  So that I use the app

  Scenario: Upload File
    When  I visit the path "/404"
    Then  I expect the page "div" with "banner-content" to contain the text "Welcome to File Upload Hub"


