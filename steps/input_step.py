from behave import then, given, when


@given('I am on the input page')
def step_impl(context):
    input_page = context.page_factory.get_input_page(context)
    input_page.navigate_to(context.ENDPOINTS.inputs)

@when('I enter "{value}" in the "{field_name}" field')
def step_impl(context, field_name, value):
    input_page = context.page_factory.get_input_page(context)
    field_name = field_name.lower()
    if field_name == "number":
        input_page.fill_number_input(value)
    elif field_name == "text":
        input_page.fill_text_input(value)
    elif field_name == "password":
        input_page.fill_password_input(value)
    elif field_name == "date":
        input_page.fill_date_input(value)
    else:
        raise ValueError(f"Unknown field name: {field_name}")
    
@then('I can see "{field_name}" with "{value}"')
def step_impl(context, field_name, value):
    input_page = context.page_factory.get_input_page(context)
    field_name = field_name.lower()
    if field_name == "number":
        input_page.verify_number_output(value)
    elif field_name == "text":
        input_page.verify_text_output(value)
    elif field_name == "password":
        input_page.verify_password_output(value)
    elif field_name == "date":
        input_page.verify_date_output(value)
    else:
        raise ValueError(f"Unknown field name: {field_name}")