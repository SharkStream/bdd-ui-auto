@UI
Feature: Login feature
	This is a demo feature to illustrate the structure of a feature file.

	Scenario Outline: Login scenario
		Given I am on the input page
		When I enter "<number>" in the "<number_field>" field
		When I enter "<text>" in the "<text_field>" field
		When I enter "<password>" in the "<password_field>" field
		When I enter "<date>" in the "<date_field>" field
		When I click on "<button_text>" button
		Then I can see "<number_field>" with "<number>"
		Then I can see "<text_field>" with "<text>"
		Then I can see "<password_field>" with "<password>"
		Then I can see "<date_field>" with "<date>"

		@wip
		Examples:
			| number_field | text_field | password_field | date_field | button_text | number | text       | password       | date       |
			| number       | text       | password       | date       | Display Inputs      | 123    | example    | mypassword     | 2023-01-01 |