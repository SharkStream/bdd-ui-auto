Feature: Login feature
	This is a demo feature to illustrate the structure of a feature file.

	Scenario Outline: Login scenario
		Given I am on the login page by logging in through "<username>" user
		Then I can see the welcome dashboard with "<username>" user
		Then I can see "<link>" link on the page

		Examples:
			| username | link   |
			| practice | Logout |
