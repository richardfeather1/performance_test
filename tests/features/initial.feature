Feature: User input
  Scenario: User enters name on form
    Given User enters Jeffery
    Then Browser returns Hello Jeffery

  Scenario: User fails to enter anything
    Given User leaves input form blank
    Then Error is displayed