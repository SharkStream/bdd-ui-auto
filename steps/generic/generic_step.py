from behave import then, given, when


@when('I click on "{button_name}" button')
def step_impl(context, button_name):
    base_page = context.page_factory.get_base_page(context)
    base_page.click_button_by_exact_text(button_name)