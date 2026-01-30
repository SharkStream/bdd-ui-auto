from .base_page import BasePage
from .input_page import InputPage
from .login_page import LoginPage
from .secure_page import SecurePage

class PageFactory:
    
    @staticmethod
    def get_login_page(context):
        return LoginPage(context.page, context)
    
    @staticmethod
    def get_secure_page(context):
        return SecurePage(context.page, context)
    
    @staticmethod
    def get_input_page(context):
        return InputPage(context.page, context)
    
    @staticmethod
    def get_base_page(context):
        return BasePage(context.page, context)
    
    @staticmethod
    def get_page(page_name: str, context):
        page_map = {
            'base': BasePage,
            'login': LoginPage,
            'secure': SecurePage,
            'input': InputPage
        }
        
        if page_name not in page_map:
            raise ValueError(f"Unknown page: {page_name}")
        
        return page_map[page_name](context.page, context)