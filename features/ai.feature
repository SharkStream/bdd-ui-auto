Feature: Ai Demo Feature
	This is a demo feature to use ai to heal selectors.

	Scenario Outline: ai fill input scenario
		Given I am on the input page
		Then I try to find a non-existent element with "<selector>" and ai can heal the selector to fill in "<value>"

		Examples:
			| selector   | value |
			| #input-num | 123   |
