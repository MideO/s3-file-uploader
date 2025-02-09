Feature: Not found pages redirected to index
  As a user
  I want a "metrics" endpoint
  So that I can export metrics to prometheus

  Scenario: Metric Endpoint
    When  I get the path "/metrics"
    Then  I expect the status code to be "200"
    Then  I expect the content to contain the text "# HELP python_gc_objects_collected_total Objects collected during gc"
    And  I expect the content to contain the text "# TYPE python_gc_objects_collected_total counter"
    And  I expect the content to contain the text "http_requests_total"
    And  I expect the content to contain the text "http_requests_created"


