Feature: Upload a file
  As a user
  I want to upload a file
  So that I can store it

  Scenario: Upload File
    When  I visit the path "/"
    Then  I expect the page "div" with "banner-content" to contain the text "Welcome to File Upload Hub"
    When  I upload a "testfile.tgz"
    Then  I expect the page "div" with "alert" to contain the text "File successfully uploaded"


