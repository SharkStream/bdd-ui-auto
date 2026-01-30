from behave import then, given, when


@when('I click on "{button_name}" button')
def step_impl(context, button_name):
    base_page = context.page_factory.get_base_page(context)
    base_page.click_button_by_exact_text(button_name)

@when('I enter "{value}" in the label of "{label_name}"')
def step_impl(context, label_name, value):
    base_page = context.page_factory.get_base_page(context)
    base_page.fill_label_input(label_name, value)

@then('I can see "{label_name}" with "{value}"')
def step_impl(context, label_name, value):
    base_page = context.page_factory.get_base_page(context)
    base_page.verify_label_value(label_name, value)