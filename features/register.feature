Feature: Register feature
    
	Scenario Outline: Register scenario
		Given I am on the register page
		When I enter "<username>" in the "<username_field>" field
		When I enter "<password>" in the "<password_field>" field
		When I enter "<password>" in the "<confirm_field>" field
		When I click on "<Register>" button
		Then I can see "<number_field>" with "<number>"
		Then I can see "<text_field>" with "<text>"
		Then I can see "<password_field>" with "<password>"
		Then I can see "<date_field>" with "<date>"

		Examples:
			| number_field | text_field | password_field | date_field | button_text | number | text       | password       | date       |
			| number  | text       | password       | date       | Display Inputs      | 123    | example    | mypassword     | 2023-01-01 |