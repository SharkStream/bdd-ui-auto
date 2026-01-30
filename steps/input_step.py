from behave import then, given, when


@given('I am on the input page')
def step_impl(context):
    input_page = context.page_factory.get_input_page(context)
    input_page.navigate_to(context.ENDPOINTS.inputs)
