Feature: Input feature
	This is a demo feature to illustrate the structure of a feature file.

	Scenario Outline: Input scenario
		Given I am on the input page
		When I enter "<number>" in the label of "<number_label>"
		When I enter "<text>" in the label of "<text_label>"
		When I enter "<password>" in the label of "<password_label>"
		When I enter "<date>" in the label of "<date_label>"
		When I click on "<button_text>" button
		Then I can see "<number_label>" with "<number>"
		Then I can see "<text_label>" with "<text>"
		Then I can see "<password_label>" with "<password>"
		Then I can see "<date_label>" with "<date>"

		@wip
		Examples:
			| number_label | text_label | password_label | date_label | button_text | number | text       | password       | date       |
			| Input: Number | Input: Text  | Input: Password       | Input: Date       | Display Inputs      | 123    | example    | mypassword     | 2023-01-01 |