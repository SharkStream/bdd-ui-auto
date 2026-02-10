from behave import then


@then('I try to find a non-existent element with "{selector}" and ai can heal the selector to fill in "{value}"')
def step_impl(context, selector, value):
    input_page = context.page_factory.get_input_page(context)
    input_page.navigate_to(context.ENDPOINTS.inputs)
    input_page.fill_input_ai(selector, value)
